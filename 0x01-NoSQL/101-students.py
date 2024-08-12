#!/usr/bin/env python3
"""
Module for finding top students
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    :param mongo_collection: pymongo collection object
    :return: list of students sorted by average score
    """
    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ]
    return list(mongo_collection.aggregate(pipeline))


if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient('mongodb://127.0.0.1:27017')
    students_collection = client.my_db.students
    top_students = top_students(students_collection)
    for student in top_students:
        print("[{}] {} => {}".format(student.get('_id'),
                                     student.get('name'),
                                     student.get('averageScore')))
