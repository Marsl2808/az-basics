#!/bin/bash

SA="saazstorage"
RG="storage-service-rg"

az storage account management-policy create \
    --account-name $SA \
    --policy @policy.json \
    --resource-group $RG