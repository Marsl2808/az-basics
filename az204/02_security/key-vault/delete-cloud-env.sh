#!/bin/bash

RG='myrg-az204'
KV='mykv-az204'

az group delete -n $RG -y

sleep 10

az keyvault purge --name $KV

# az keyvault list-deleted --subscription {SUBSCRIPTION ID} --resource-type vault
# az keyvault recover --subscription {SUBSCRIPTION ID} -n {VAULT NAME}
# az keyvault update --subscription {SUBSCRIPTION ID} -g {RESOURCE GROUP} -n {VAULT NAME} --enable-purge-protection true
