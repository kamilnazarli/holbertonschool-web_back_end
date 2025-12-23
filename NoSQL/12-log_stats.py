#!/usr/bin/env python3
"""
Provides statistics about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def log_stats():
    """
    Provides statistics about Nginx logs stored in MongoDB.

    Displays:
    - Total number of logs
    - Number of logs for each HTTP method: GET, POST, PUT, PATCH, DELETE
    - Number of GET requests to the /status path
    """
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.logs
    collection = db.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("{} logs".format(collection.count_documents({})))

    print("Methods:")
    for method in methods:
        print(
            "\tmethod {}: {}".format(
                method,
                collection.count_documents({"method": method})
            )
        )

    print(
        "{} status check".format(
            collection.count_documents(
                {"method": "GET", "path": "/status"}
            )
        )
    )


if __name__ == "__main__":
    log_stats()

