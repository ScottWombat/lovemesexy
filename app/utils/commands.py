import click
import json   
from pathlib import Path
import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from app.utils.date_time import get_current_utc_datetime
import datetime

@click.command()
@click.option('--catalog_name', prompt='Catalog Name',
             help='Your mongodb collection')
def mongodb_find_all(catalog_name):
    db = get_db("love_me_sexy")
    collection = db[catalog_name]
    d = collection.find({}, {'name':1, '_id':0})
    for document in d:
        print(document)

@click.command()
@click.option('--collection_name', prompt='Collection Name',
             help='Your mongodb collection')
@click.option('--catalog_id', prompt='Catalog Id',
             help='Your mongodb collection')
def mongodb_query(collection_name,catalog_id):
    db = get_db("love_me_sexy")
    collection = db[collection_name]
    d = collection.find({'catalog_id': catalog_id},{ 'name': 1, '_id': 0 } )
    a = list(d)
    ret = []
    for l in a:
        ret.append(l['name'])

    print(ret)

@click.command()
def mongodb_bulk_upload():
    print(get_current_utc_datetime())
    
    full_json_path = os.path.join(Path(__file__).parent.parent.parent, "data","bulk.json")
    print(full_json_path)
    print(ObjectId())
    with open(full_json_path) as json_file:
        json_data = json.load(json_file)
       #for index, x in enumerate(json_data):
       #     print(index,x)
    
    for i, val in enumerate(json_data):
        val["created_at"] = get_current_utc_datetime()
        val["updated_at"] = get_current_utc_datetime()

   
    client = MongoClient('mongodb://%s:%s@127.0.0.1' % ("root", "password"))
    dbnames = client.list_database_names()
    if 'mymongo' in dbnames:
        print ("It's there!")
        client.drop_database('mymongo')
    catalog_coll = client['love_me_sexy']['catalogs']
    collection = client['love_me_sexy']['products']
    
    #product = collection.insert_many(json_data) #collection.insert_one(data)
    #print(product.inserted_ids)

@click.command()
#@click.option('--db_name', prompt='DB Name',
#              help='Your mongodb collection')
@click.option('--collection_name', prompt='Collection',
              help='Your mongodb collection')
def upload(collection_name):
    db_name="love_me_sexy"
    json_data = get_json_data(collection_name)

    for i, val in enumerate(json_data):
        val["created_at"] = get_current_utc_datetime()
        val["updated_at"] = get_current_utc_datetime()

    db = get_db(db_name)
    collection = db[collection_name]
    results = collection.insert_many(json_data)
    print(results.inserted_ids)

def get_db(name):
    client = MongoClient('mongodb://%s:%s@127.0.0.1' % ("root", "password"))   
    db= client[name]
    return db


def get_json_data(name):
    file_name = f'data/{name}.json'
    full_json_path = os.path.join(Path(__file__).parent.parent.parent, file_name)
    with open(full_json_path) as json_file:
        json_data = json.load(json_file)
    return json_data
    
@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

    