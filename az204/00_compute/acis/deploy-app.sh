#!/bin/bash

# az acr credential show --name [--resource-group]
# <service-principal-ID> --registry-password <service-principal-password>
# -> acr create (?)

REGISTRY_PW='v3bIVHfQRMXkzSrRtIDjUIW4BkJ2kbn3gwiUiwoV5S+ACRDMn+Fr'
RANDOM_POSTFIX='19019'

RG='aci-rg'
ACR='myexampleacr'$RANDOM_POSTFIX
LOCATION=westeurope
CONTAINER_GROUP_NAME='flask-test-group'
ACR_LOGIN_SERVER='myexampleacr'$RANDOM_POSTFIX'.azurecr.io'
IMG=$ACR_LOGIN_SERVER'/flask-test:v1'
ACI_DNS_LABEL='myexampleaci'$RANDOM_POSTFIX

az container create -g $RG -n $CONTAINER_GROUP_NAME --image $IMG --cpu 1 --memory 1 --registry-login-server $ACR_LOGIN_SERVER --registry-username $ACR --registry-password $REGISTRY_PW --ip-address Public --dns-name-label $ACI_DNS_LABEL --ports 5000

# verify deployment
az container show --resource-group $RG --name $CONTAINER_GROUP_NAME --query instanceView.state
az container show --resource-group $RG --name $CONTAINER_GROUP_NAME --query ipAddress.fqdn

# show container logs
az container logs --resource-group $RG --name $CONTAINER_GROUP_NAME