from database import db
from database import tgusers

botusers = db["botusers"]


def new_user(from_user):
    tgusers.update_user(from_user)
    botusers.update_one(
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


def remove_user(userid):
    botusers.delete_one({"id": userid})


def bot_users():
    return list(botusers.find({}, {'_id': 0}))
