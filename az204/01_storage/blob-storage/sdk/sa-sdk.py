from dotenv import load_dotenv
from azure.storage.blob import BlobClient, ContainerClient, BlobServiceClient
import random
import os
import uuid

# Quickstart tutorial
# https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python


def get_random_name(prefix: str, postfix: str) -> str:
  return prefix+str(uuid.uuid4())+postfix

# init local env
load_dotenv()
CONN_STR = os.getenv('CONN_STR')

# Create a  container
container_name=get_random_name("test-container-", "")
blob_service_client = BlobServiceClient.from_connection_string(conn_str=CONN_STR)
container_client = blob_service_client.get_container_client(container=container_name)
container_client = blob_service_client.create_container(name=container_name)

# upload blob
blob = BlobClient.from_connection_string(conn_str=CONN_STR, container_name=container_name, blob_name=get_random_name("testdata", ".txt"))
with open("./SampleSource.txt", "rb") as data:
    blob.upload_blob(data)

# Create a read-only snapshot of the blob at this point in time
snapshot_blob = blob.create_snapshot()

# get blobs
print("\nListing blobs...")

# List the blobs in the container
blobs = container_client.list_blobs()
for blob in blobs:
    print("\t" + blob.name)

# download blobs
download_file_path = os.path.join("./", get_random_name("download-", ".txt"))
print("\nDownloading blob to \n\t" + download_file_path)

with open(file=download_file_path, mode="wb") as download_file:
 download_file.write(container_client.download_blob(blob).readall())

# delete container
blob_service_client.delete_container(container=container_name)