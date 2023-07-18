#!/usr/bin/env python3
"""Update topic of document in a collection base on its name"""


def update_topics(mongo_collection, name, topics):
    """Update the topic of all document with name = name in collection"""

    name_field = {"name": name}
    topic_field = {"$set": {"topics" : topics}}
    mongo_collection.update_many(name_field, topic_field)
