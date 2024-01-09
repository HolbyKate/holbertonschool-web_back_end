#!/usr/bin/env python3
"""function that inserts a new document in a collection based on kwargs"""


from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document"""
    return mongo_collection.insert_new_id
