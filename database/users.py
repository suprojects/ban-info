from database import db

users = db["users"]


def update_user(id, username, firstname, lastname):
    username = username.lower()

    users.update_one(
        {"id": id},
        {
            "$set": {
                "username": username,
                "firstname": firstname,
                "lastname": lastname,
            }
        },
        upsert=True,
    )


def remove_user(id):
    if users.find_one({"id": id}):
        users.delete_one({"id": id})


def all_users():
    return list(users.find())


def get_id_by_username(username):
    username = username.lower()

    find = users.find_one({"username": username})

    if find:
        return find["id"]


def get_username_by_id(id):
    find = users.find_one({"id": id})

    if find:
        return find["username"]
