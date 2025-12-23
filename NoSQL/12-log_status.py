#!/usr/bin/env python3

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.logs

clc = db.nginx

print("{} logs".format(clc.count_documents({})))
print("Methods:")
for i in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    print("method {}: {}".format(i, clc.count_documents({"method": i})))
print("{} {}".format(clc.count_documents({"method": "GET"}), clc.count_documents({"path": "/status"})))
