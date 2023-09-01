from azure.cosmos import CosmosClient, exceptions, PartitionKey

from dotenv import load_dotenv
import os

load_dotenv()
PK = os.getenv("PK")
ENDPOINT = os.getenv("ENDPOINT")

# Consistency level can be set on a per request basis by a client, which overrides the default consistency level set at the cosmos-db-account level
client = CosmosClient(url=ENDPOINT, credential=PK, consistency_level='Session')

# create database (Databaseproxy)
DATABASE_NAME = 'testDatabase'
try:
    database = client.create_database(DATABASE_NAME)
except exceptions.CosmosResourceExistsError:
    database = client.get_database_client(DATABASE_NAME)

# create container (ContainerProxy)
CONTAINER_NAME = 'products'
PARTITION_KEY="/productName"
try:
    container = database.create_container(id=CONTAINER_NAME, partition_key=PartitionKey(path=PARTITION_KEY))
except exceptions.CosmosResourceExistsError:
    container = database.get_container_client(CONTAINER_NAME)
except exceptions.CosmosHttpResponseError:
    raise

container.query_items_change_feed

# insert data
# id key is mandatory and needs to be unique inside the container
for i in range(1, 10):
    container.upsert_item({
            'id': 'item{0}'.format(i),
            'productName': 'Widget',
            'productModel': 'Model {0}'.format(i)
        }
    )

# delete item
for item in container.query_items(
        query='SELECT * FROM products p WHERE p.productModel = "Model 2"',
        enable_cross_partition_query=True):
    container.delete_item(item, partition_key='Widget')

#query the db
# Enumerate the returned items
import json
for item in container.query_items(
        query='SELECT * FROM mycontainer r WHERE r.id="item3"',
        enable_cross_partition_query=True):
    print(json.dumps(item, indent=True))

# or parameterized query 
discontinued_items = container.query_items(
    query='SELECT * FROM products p WHERE p.productModel = @model',
    parameters=[
        dict(name='@model', value='Model 7')
    ],
    enable_cross_partition_query=True
)
for item in discontinued_items:
    print(json.dumps(item, indent=True))

######################
# get db properties
properties = database.read()
print(json.dumps(properties))
# throughput
#db_offer = database.read_offer()
#print('Found Offer \'{0}\' for Database \'{1}\' and its throughput is \'{2}\''.format(db_offer.properties['id'], database.id, db_offer.properties['content']['offerThroughput']))
#container_offer = container.read_offer()
#print('Found Offer \'{0}\' for Container \'{1}\' and its throughput is \'{2}\''.format(container_offer.properties['id'], container.id, container_offer.properties['content']['offerThroughput']))

# modify properties, (here time to live = 10s)
database.replace_container(
    container,
    partition_key=PartitionKey(path=PARTITION_KEY),
    default_ttl=10,
)
# Display the new TTL setting for the container
container_props = container.read()
print(json.dumps(container_props['defaultTtl']))