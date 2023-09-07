#!/bin/bash

RG='myrg-az204'
# az account list-locations -o table
LOC='westeurope'
KV='mykv-az204'


#######
az group create -n $RG -l $LOC

az keyvault create -n $KV -g $RG -l $LOC



