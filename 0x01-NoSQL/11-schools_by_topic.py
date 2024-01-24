#!/usr/bin/env python3

"""Module for listing based on specific topic."""


def schools_by_topic(mongo_collection, topic):
    """Return list of school having a the specific 'topic'."""
    return [i for i in mongo_collection.find({"topics": topic})]
