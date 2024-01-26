#!/usr/bin/env python3

"""Module to get all students ordered by avg score."""


def top_students(mongo_collection):
    """Returns all students sorted by average score."""
    return mongo_collection.aggregate(
        [
            {"$addFields": {"averageScore": {"$avg": "$topics.score"}}},
            {"$sort": {"averageScore": -1}},
        ]
    )
