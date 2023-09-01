import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
import azure.cosmos.partition_key as partition_key
from azure.cosmos import CosmosClient
import uuid

from dotenv import load_dotenv
import os

load_dotenv()
PK = os.getenv("PK")
ENDPOINT = os.getenv("ENDPOINT")
DATABASE_NAME = 'testDatabase'
CONTAINER_ID='changefeedContainer'

def create_items(container, num_items):

    for i in range(1, num_items):
        c = str(uuid.uuid4())
        item = {'id': 'item' + c,
                                'address': {'street': '1 Microsoft Way'+c,
                                        'city': 'Redmond'+c,
                                        'state': 'WA',
                                        'zip code': 98052
                                        }
                                }

        created_item = container.create_item(body=item)


def read_change_feed(container):
    print('\nReading Change Feed from the beginning\n')
    # For a particular Partition Key Range we can use partition_key_range_id]
    # 'is_start_from_beginning = True' will read from the beginning of the history of the container
    # If no is_start_from_beginning is specified, the read change feed loop will pickup the items that happen while the loop / process is active
    response = container.query_items_change_feed(is_start_from_beginning=True)
    for doc in response:
        print(doc)

    print('\nFinished reading all the change feed\n')


def run_sample():
    client = CosmosClient(ENDPOINT, credential = PK)
    try:
        # setup database for this sample
        try:
            db = client.create_database(id=DATABASE_NAME)
        except exceptions.CosmosResourceExistsError:
            db = client.get_database_client(DATABASE_NAME)

        # setup container for this sample
        try:
            container = db.create_container(
                id=CONTAINER_ID,
                partition_key=partition_key.PartitionKey(path='/address/state', kind=documents.PartitionKind.Hash)
            )
            print('Container with id \'{0}\' created'.format(CONTAINER_ID))
        except exceptions.CosmosResourceExistsError:
            container = db.get_container_client(CONTAINER_ID)
            print("Container with id '{}' already exists".format(CONTAINER_ID))

        create_items(container, 100)
        read_change_feed(container)

    except exceptions.CosmosHttpResponseError as e:
        print('\nrun_sample has caught an error. {0}'.format(e.message))

    finally:
        print("\nrun_sample done")


if __name__ == '__main__':
    run_sample()