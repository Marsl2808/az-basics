#!/bin/bash

# login: az login
# view available locations: az functionapp list-consumption-locations
# check supported runtimes: az functionapp list-runtimes

GROUP_NAME="fct-rg"
LOCATION="westeurope"
STORAGE_NAME="fctsa"
APP_NAME="fct-app"

echo "---- create rg ----"
az group create -n $GROUP_NAME -l $LOCATION

echo "---- create sa ----"
az storage account create -g $GROUP_NAME -n $STORAGE_NAME -l $LOCATION --sku "Standard_LRS"

echo "---- create function app ----"
az functionapp create -n $APP_NAME -s $STORAGE_NAME -c $LOCATION -g $GROUP_NAME --functions-version 4 --os-type "linux" --runtime "python" --runtime-version 3.9
