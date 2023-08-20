#!/bin/bash

# set principal for role assignment
if [ $# -eq 0 ]; then
    >&2 echo "Please provide Azure-Principal"
    exit 1
fi
PRINCIPAL=$1

# resource names
RG='storage-service-rg'
LOCATION='westeurope'
SA_NAME='sasimpleappservice'
CONTAINER_NAME='my-blob-conatiner'
ASP_NAME='my-app-service-plan'
AS_NAME='simple-webapp-'$RANDOM


echo "----- creating resource group -----"
az group create --name $RG --location $LOCATION

echo "----- creating storage account -----"
az storage account create -n $SA_NAME -g $RG --access-tier 'Hot' --allow-blob-public-access 'true'

echo "---- conn string ----"
connection_string=$(az storage account show-connection-string -g $RG -n $SA_NAME --query "connectionString")
echo $connection_string

## plot account meta
echo "Account URL:"
echo $(az storage account show -n $SA_NAME -g $RG --query "primaryEndpoints.blob")

echo "SAS-Token:"
echo $(az storage account keys list -g $RG -n $SA_NAME)
####

echo "----- creating container -----"
az storage container create --name $CONTAINER_NAME --account-name $SA_NAME --connection-string $connection_string --public-access 'container'
echo $CONTAINER_NAME

echo "---- add role ----"
principal_id=$(az ad user show --id $PRINCIPAL --query "id" --output tsv)
az role assignment create --assignee $principal_id --role "Storage Blob Data Contributor" --resource-group $RG

echo "----- upload sample file -----"
SAMPLE_FILE='SampleSource.txt'
az storage blob upload --account-name $SA_NAME --container-name $CONTAINER_NAME --name $SAMPLE_FILE --file "./app/"$SAMPLE_FILE

echo "----- create app service plan -----"
az appservice plan create -g $RG -n $ASP_NAME --sku 'B1' --is-linux

echo "----- upload webapp -----"
cd ./app
az webapp up -p $ASP_NAME -n $AS_NAME -g $RG -l $LOCATION --runtime PYTHON:3.9 --logs

echo "---- set App configuration ----"
az webapp config appsettings set -g $RG -n $AS_NAME --settings CONN_STR=$connection_string
az webapp config appsettings set -g $RG -n $AS_NAME --settings CONTAINER_NAME=$CONTAINER_NAME
