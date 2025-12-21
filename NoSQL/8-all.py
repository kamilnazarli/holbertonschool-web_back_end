#!/usr/bin/env python3
'''
This module creates a function which return list of documents in a collection
'''

def list_all(mongo_collection):
    '''
    This function returns list of documents
    '''

    return mongo_collection.find()
