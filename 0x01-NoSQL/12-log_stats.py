#!/usr/bin/env python3

"""Module for stats of nginx logs stored in mongodb."""
if __name__ == "__main__":
    import pymongo

    client = pymongo.MongoClient()
    db = client["logs"]
    coll = db["nginx"]

    print(f"{coll.count_documents({})} logs")
    print("Methods:")
    print(
        f"    method GET: {coll.count_documents({'method': 'GET'})}"
        )
    print(
        f"    method POST: {coll.count_documents({'method': 'POST'})}"
        )
    print(
        f"    method PUT: {coll.count_documents({'method': 'PUT'})}"
        )
    print(
        f"    method PATCH: {coll.count_documents({'method': 'PATCH'})}"
        )
    print(
        f"    method DELETE: {coll.count_documents({'method': 'DELETE'})}"
        )
    filter = coll.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{filter} status check")
