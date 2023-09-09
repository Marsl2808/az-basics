import os
from dotenv import load_dotenv

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

load_dotenv()
keyVaultName = os.getenv("KEY_VAULT_NAME")
KVUri = f"https://{keyVaultName}.vault.azure.net"

# identity from current login shell is used
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

# create
secretName = input("Input a name for your secret > ")
secretValue = input("Input a value for your secret > ")
print(f"Creating a secret in {keyVaultName} called '{secretName}' with the value '{secretValue}' ...")

client.set_secret(secretName, secretValue)
print(" done.")

# read
print(f"Retrieving your secret from {keyVaultName}.")
retrieved_secret = client.get_secret(secretName)

print(f"Your secret is '{retrieved_secret.value}'.")
print(f"Deleting your secret from {keyVaultName} ...")

# delete
poller = client.begin_delete_secret(secretName)
deleted_secret = poller.result()
print(" done.")
