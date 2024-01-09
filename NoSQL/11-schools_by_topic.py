#!/usr/bin/env python3
"""function that returns the list of school having a specific topic"""


from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    function that changes all topics of a school document based on the name
    """
    return mongo_collection.find({"topics": topic})
