#!/usr/bin/env python3

"""Module for stats of nginx logs stored in mongodb."""

import pymongo

client = pymongo.MongoClient()
db = client["logs"]
collection = db["nginx"]

print(f"{collection.count_documents({})} logs")
print("Methods:")
print(f"    method GET: {collection.count_documents({'method': 'GET'})}")
print(f"    method POST: {collection.count_documents({'method': 'POST'})}")
print(f"    method PUT: {collection.count_documents({'method': 'PUT'})}")
print(f"    method PATCH: {collection.count_documents({'method': 'PATCH'})}")
print(f"    method DELETE: {collection.count_documents({'method': 'DELETE'})}")
filter = collection.count_documents({'method': 'GET', 'path': '/status'})
print(f"{filter} status check")
