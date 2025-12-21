#!/usr/bin/env python3
"""
This module updates the document
"""

def update_topics(mongo_collection, name, topics):
    """
    To change all topics of a school document based on name
    """

    mongo_collection.update({}, {$set: {name: topics}}, false, true)
