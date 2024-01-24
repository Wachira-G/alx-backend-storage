#!/usr/bin/env python3

"""Has function for listing documents."""


def list_all(mongo_collection):
    """Lists all documents in a collection."""
    documents = [i for i in mongo_collection.find()]
    return documents
