#!/bin/bash

SA_NAME='saazstorage'
RG='storage-service-rg'
CONTAINER_NAME='my-blob-conatiner'

# an executable of azcopy is needed to run this script
# add azcopy-binary to search path
azcopy_path=${PWD%/*/*/*/*}
PATH="$azcopy_path:$PATH"

# set principal for role assignment
if [ $# -eq 0 ]; then
    >&2 echo "Please provide Azure-Principal"
    exit 1
fi
PRINCIPAL=$1

# login with principal account (Azure-AD)
azcopy login

echo "---- add roles to principal for data upload----"
principal_id=$(az ad user show --id $PRINCIPAL --query "id" --output tsv)
az role assignment create --assignee $principal_id --role "Storage Blob Data Contributor" --resource-group $RG
az role assignment create --assignee $principal_id --role "Storage Blob Data Owner" --resource-group $RG

echo "----- upload sample file, using azcopy -----"
FILENAME="SampleSource-"$RANDOM".txt"
UPLOAD_URL="https://"$SA_NAME".blob.core.windows.net/"$CONTAINER_NAME"/"$FILENAME

azcopy copy SampleSource.txt $UPLOAD_URL

azcopy logout

# alternative: use azcopy without AD-login, by providing SAS-URL (-> SAS needs to be created before)
# azcopy copy <local_file> <remote_SAS_url> 
