#!/usr/bin/env python3
'''
This module returns list of school having specific topic
'''

def schools_by_topic(mongo_collection, topic):
    '''
    To return school that has specific topic
    '''

    ls = []
    for school in mongo_collection.find():
        if topic is in school.get('topics', ""):
            ls.append(school)
    return ls
