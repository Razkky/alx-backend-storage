#!/usr/bin/env python3
"""Return list of schools having a specific  topic"""


def schools_by_topic(mongo_collection, topic) -> list:
    """Return list of all schools having a specific topic"""

    return [item for item in mongo_collection.find({"topics": topic})]
