#!/bin/bash
KV="mykv-az204"

SECRET_NAME="mysecret"
SECRET_VALUE="a1b2c3d4e5f6"

KEY_NAME="mykey-az204"

CERT_NAME="mycert-az204"

# create and retrieve secrets
az keyvault secret set --vault-name $KV --name $SECRET_NAME --value $SECRET_VALUE

az keyvault secret show --name $SECRET_NAME --vault-name $KV

# create and retrieve keys
az keyvault key create --kty "RSA" --curve "Ed25519" --size "2048" -n $KEY_NAME --vault-name $KV

az keyvault key list --vault-name $KV

# create and retrieve certificates (with default policy)
az keyvault certificate create --vault-name $KV -n $CERT_NAME -p "$(az keyvault certificate get-default-policy)"

az keyvault certificate list --vault-name $KV