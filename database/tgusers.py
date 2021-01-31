from database import db

users = db["users"]


def update_user(from_user):

    users.update_one(
        {"id": from_user.id},
        {
            "$set": {
                "username": from_user.username if from_user.username else None,
                "firstname": from_user.first_name,
                "lastname": from_user.last_name if from_user.last_name else None,
            }
        },
        upsert=True,
    )


def all_users():
    return list(users.find())


def get_id_by_username(username):
    username = username.lower()

    find = users.find_one({"username": username}, {'_id': 0})

    return find["userid"]


def get_username_by_id(userid):
    find = users.find_one({"userid": userid}, {'_id': 0})

    return find["username"]