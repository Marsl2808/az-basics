from azure.cosmos.aio import CosmosClient

from dotenv import load_dotenv
import os
import sys
import asyncio
import json
import logging

enable_logging = False

if(enable_logging):
    # Create a logger for the 'azure' SDK
    logger = logging.getLogger('azure')
    logger.setLevel(logging.DEBUG)

    # Configure a console output
    handler = logging.StreamHandler(stream=sys.stdout)
    logger.addHandler(handler)

load_dotenv()
PK = os.getenv("PK")
ENDPOINT = os.getenv("ENDPOINT")

DATABASE_NAME = 'testDatabase'
CONTAINER_NAME = 'products'



async def create_products():
    async with CosmosClient(url=ENDPOINT, credential=PK) as client: # with statement will automatically initialize and close the async client
        database = client.get_database_client(DATABASE_NAME)
        container = database.get_container_client(CONTAINER_NAME)
        for i in range(10):
            await container.upsert_item({
                    'id': 'item{0}'.format(i),
                    'productName': 'Widget',
                    'productModel': 'Model {0}'.format(i)
                    })


async def query_products():
    client = CosmosClient(url=ENDPOINT, credential=PK)
    database = client.get_database_client(DATABASE_NAME)
    container = database.get_container_client(CONTAINER_NAME)
    results = container.query_items(
            query='SELECT * FROM products p WHERE p.productModel = "Model 2"')

    # iterates on "results" iterator to asynchronously create a complete list of the actual query results
    item_list = []
    async for item in results:
        item_list.append(item)
    # Asynchronously creates a complete list of the actual query results. This code performs the same action as the for-loop example above.
    #item_list = [item async for item in results]

    for x in range(len(item_list)):
        print(json.dumps(item_list[x], indent=True))
    #print(*item_list, sep = "\n")
    await client.close()

asyncio.run(create_products())
asyncio.run(query_products())