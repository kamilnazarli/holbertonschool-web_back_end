#!/usr/bin/env python3
"""
To insert a new document in a collection
"""

def insert_school(mongo_collection, **kwargs):
    """
    This function inserts anew document in a collection
    """

    mongo_collection.insert(kwargs)
    return kwargs.get('_id')
