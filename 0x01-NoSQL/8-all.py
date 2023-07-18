#!/usr/bin/env python3
"""This script uses pymongo to list all document in a collection"""
from typing import List


def list_all(mongo_collection):
    """Return list of all document in collection"""
    
    collection: list = []

    documents = mongo_collection.find()
    if documents:
        for doc in documents:
            collection.append(doc)

    return collection
