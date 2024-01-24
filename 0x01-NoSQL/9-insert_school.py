#!/usr/bin/env python3

"""Module for function to insert new doc."""


def insert_school(mongo_collection, **kwargs):
    """insert a new document in a collection based on kwargs."""
    mongo_collection.insert_one(kwargs)
