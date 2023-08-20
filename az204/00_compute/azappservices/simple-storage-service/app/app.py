
#from dotenv import load_dotenv
import os
import random

from flask import Flask
from azure.storage.blob import BlobClient

# init local env
# TODO: set remote config
#load_dotenv()
CONN_STR = os.getenv('CONN_STR')
CONTAINER_NAME=os.getenv('CONTAINER_NAME')

# init webapp
app = Flask(__name__)

@app.route("/")
def main_page():
    return f"<h1>Hello from Flask!<h1>"

@app.route("/<name>")
def main_page_named(name):
    return f"<h1>Hello {name}!<h1>"

@app.route("/upload_blob")
def upload_blob():

    blob = BlobClient.from_connection_string(conn_str=CONN_STR, container_name=CONTAINER_NAME, blob_name=get_random_name())

    while(not blob.exists()):
        blob = BlobClient.from_connection_string(conn_str=CONN_STR, container_name=CONTAINER_NAME, blob_name=get_random_name())

    with open("./SampleSource.txt", "rb") as data:
        blob.upload_blob(data)

    return "<h2>blob upload finished<h2>"

def get_random_name() -> str:
    return "testdata"+str(random.randint(0,10000))

if __name__ == "__main__":
    app.run()
