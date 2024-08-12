#!/usr/bin/env python3
"""
Module for inserting a new document in a MongoDB collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    :param mongo_collection: pymongo collection object
    :param kwargs: keyword arguments to be inserted as a document
    :return: new _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id


if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    new_school_id = insert_school(school_collection, name="UCSF",
                                  address="505 Parnassus Ave")
    print("New school created: {}".format(new_school_id))
