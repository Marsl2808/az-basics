#!/bin/bash

RG='aci-rg'
LOCATION=westeurope
ACR='myexampleacr'$RANDOM
ACR_SKU='Basic'
IMG_NAME='flask-test'
REPO_NAME=$IMG_NAME

echo "----- create RG -----"
az group create -n $RG -l $LOCATION

echo "----- create ACR -----"
az acr create -g $RG -n $ACR --sku $ACR_SKU --admin-enabled

echo "----- login -----"
az acr login -n $ACR

echo "----- full name of ACR server (-> img-tag) ------"
acr_full_name=$(az acr show -n $ACR --query loginServer --output table | tail -1)
echo $acr_full_name

# build and push images (local docker operations)
echo "---- ----"
tagged_img=$acr_full_name/$IMG_NAME:v1
docker tag $IMG_NAME $tagged_img
docker push $tagged_img

echo "----- show imgs and tags -----"
az acr repository list --name $ACR --output table
az acr repository show-tags -n $ACR --repository $REPO_NAME --output table
