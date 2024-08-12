#!/usr/bin/env python3
"""
Module for finding schools by topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic
    :param mongo_collection: pymongo collection object
    :param topic: topic searched
    :return: list of schools having the specified topic
    """
    return list(mongo_collection.find({"topics": topic}))


if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = schools_by_topic(school_collection, "Python")
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'),
                                  school.get('topics', "")))
