#!/usr/bin/env python3
"""This scripts counts all document in a collection along with some attr"""
from pymongo import MongoClient


conn = MongoClient()
collection = conn.logs.nginx

count = collection.count_document({})
get = col.count_documents({"method": "GET"})
post = col.count_documents({"method": "POST"})
put = col.count_documents({"method": "PUT"})
patch = col.count_documents({"method": "PATCH"})
delete = col.count_documents({"method": "DELETE"})
status = col.count_documents({"method": "GET", "path": "/status"})


if __name__ == "__main__":
    """Print all variable"""
    print(f"{count} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{status} status check")