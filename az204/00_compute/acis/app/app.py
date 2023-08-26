
import os
import random

from flask import Flask
#from azure.storage.blob import BlobClient

# init local env
#load_dotenv()
#ONN_STR = os.getenv('CONN_STR')
#CONTAINER_NAME=os.getenv('CONTAINER_NAME')

# init webapp
app = Flask(__name__)

@app.route("/")
def main_page():
    return f"<h1>Hello from Flask!<h1>"

@app.route("/<name>")
def main_page_named(name):
    return f"<h1>Hello {name}!<h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
