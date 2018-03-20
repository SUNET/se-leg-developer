#!/usr/bin/env python

from __future__ import absolute_import

import argparse
import yaml
from pymongo import MongoClient

##
## Reads users and collections from a yaml file.
##
## User passwords will be set to [username]_pw.
##

def create_users(client, databases):
    for db_name, conf in databases.items():
	print('Adding users for {}'.format(db_name))
	access_conf = conf.get('access', dict())
	for rw_user in access_conf.get('readWrite', list()):
	    print('Added rw user: {}'.format(rw_user))
	    client[db_name].add_user(rw_user, '{}_pw'.format(rw_user), roles=[{'role':'readWrite', 'db': db_name}])
	for ro_user in access_conf.get('read', list()):
	    print('Added ro user: {}'.format(ro_user))
	    client[db_name].add_user(ro_user, '{}_pw'.format(ro_user), roles=[{'role':'read', 'db': db_name}])
	print('---')

def init_collections(client, databases):
    for db_name, conf in databases.items():
        print('Init collections for {}'.format(db_name))
        collections = conf.get('collections', list())
        for collection in collections:
            doc = client[db_name][collection].insert({'init': True})
            client[db_name][collection].remove(doc)
	    print('Created {}'.format(collection))

def init_data(client, databases):
    for db_name, conf in databases.items():
        print('Inserting initial data for {}'.format(db_name))
        init_data = conf.get('initial_data', dict())
        for collection, data in init_data.items():
            for item in data:
                doc = client[db_name][collection].replace_one(item, item, upsert=True)
                print('Added {} to {}'.format(item, collection))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help="YAML file (/opt/eduid/db-scripts/local.yaml)", type=str, default="/opt/eduid/db-scripts/local.yaml")
    parser.add_argument('-d', '--database', help="Mongo database adress (localhost)", type=str, default="localhost")
    args = parser.parse_args()
    
    with open(args.file) as f:
	data = yaml.load(f)

    client = MongoClient(args.database)
    databases = data['mongo_databases']
    
    create_users(client, databases)
    init_collections(client, databases)
    init_data(client, databases)

if __name__ == "__main__":
    main()
