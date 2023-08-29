from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
import os

load_dotenv()
sub_id = os.getenv("SUBSCRIPTION_ID")
client = StorageManagementClient(credential=DefaultAzureCredential(), subscription_id=sub_id)

# examples
# https://github.com/Azure-Samples/azure-samples-python-management/tree/main/samples/storage