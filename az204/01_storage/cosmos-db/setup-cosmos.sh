#!/bin/bash

RG="cosmos-rg"
LOCATION="westeurope"
COSMOS_NAME="my-cosmos-db-marcel"
# "BoundedStaleness", "ConsistentPrefix", "Eventual", "Session", "Strong"
CONSISTENCY_LEVEL_DEFAULT="Session"

# create resource group
az group create -l $LOCATION -n $RG

# create cosmos db
az cosmosdb create -n $COSMOS_NAME -g $RG --default-consistency-level $CONSISTENCY_LEVEL_DEFAULT

# output PK and endpoint for python connection
echo $(az cosmosdb show -g $RG -n $COSMOS_NAME --query documentEndpoint --output tsv)
echo $(az cosmosdb keys list -n $COSMOS_NAME -g $RG --query primaryMasterKey --output tsv)

# update an existing accounts default consistency level
# az cosmosdb update -n $COSMOS_NAME -g $RG --default-consistency-level "Strong"
