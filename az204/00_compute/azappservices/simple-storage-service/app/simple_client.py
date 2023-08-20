
from dotenv import load_dotenv
import os

from azure.storage.blob import BlobClient

# init local env
load_dotenv()
CONN_STR = os.getenv('CONN_STR')

# upload a blob
CONTAINER_NAME='my-blob-conatiner'
blob = BlobClient.from_connection_string(conn_str=CONN_STR, container_name=CONTAINER_NAME, blob_name="testdata2")

with open("./SampleSource.txt", "rb") as data:
    blob.upload_blob(data)

print("blob upload finished")

#######################################################################

# 1) use SAS token to create a connection
#from azure.storage.blob import BlobServiceClient
#from azure.storage.blob import BlobServiceClient, generate_account_sas, ResourceTypes, AccountSasPermissions
#from datetime import datetime, timedelta

# ACCOUNT_NAME=os.getenv('ACCOUNT_NAME')
# ACCOUNT_KEY=os.getenv('ACCOUNT_KEY')
# ACCOUNT_URL=os.getenv('ACCOUNT_URL')

# print(ACCOUNT_NAME)
# print(ACCOUNT_KEY)
# print(ACCOUNT_URL)


# sas_token = generate_account_sas(
#     account_name=ACCOUNT_NAME,
#     account_key=ACCOUNT_KEY,
#     resource_types=ResourceTypes(service=True),
#     permission=AccountSasPermissions(read=True),
#     expiry=datetime.utcnow() + timedelta(hours=1)
# )

# blob_service_client = BlobServiceClient(account_url=ACCOUNT_URL, credential=sas_token)

#CONTAINER_NAME="mycontainer"

# blob_service_client.create_container(BLOB_CONTAINER_NAME)

#############################

# create a container (first step not requ. SAS-token is included)
# from azure.storage.blob import ContainerClient

#CONN_STR="DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=sasimpleappservice;AccountKey=XVrZfffMrWFLr7BBvxTyycgihETutNdoA1Jm7hjqRb06TzHMXWP8E7bH0S6XrXR1dSuK2lL0GkF3+AStgwujcw==;BlobEndpoint=https://sasimpleappservice.blob.core.windows.net/;FileEndpoint=https://sasimpleappservice.file.core.windows.net/;QueueEndpoint=https://sasimpleappservice.queue.core.windows.net/;TableEndpoint=https://sasimpleappservice.table.core.windows.net/"

# container_client = ContainerClient.from_connection_string(conn_str=CONN_STR, container_name=CONTAINER_NAME)

# # # uncomment to create a new container -> shouldn't be called twice
# container_client.create_container()