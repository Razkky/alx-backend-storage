#!/usr/bin/env python3
"""Insert new document to a collection"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document to a collection and return its id"""

    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id