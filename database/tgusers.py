from database import db
import re

users = db["users"]


def update_user(from_user):
    users.update_one(
        {"id": from_user.id},
        {
            "$set": {
                "username": from_user.username,
                "firstname": from_user.first_name,
                "lastname": from_user.last_name,
            }
        },
        upsert=True,
    )


def all_users():
    return list(users.find({}, {'_id': 0}))


def get_by_username(username):
    return users.find_one({"username": re.compile(username, re.IGNORECASE)}, {'_id': 0})


def get_by_id(userid):
    return users.find_one({"id": userid}, {'_id': 0})
