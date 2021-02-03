from database import db

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
    return list(users.find({}, {'id': 1, 'username': 1, 'firstname': 1, 'lastname': 1}))


def get_id_by_username(username):
    username = username.lower()

    return users.find_one({"username": username}, {'id': 1, 'username': 1, 'firstname': 1, 'lastname': 1})


def get_username_by_id(userid):
    return users.find_one({"userid": userid}, {'id': 1, 'username': 1, 'firstname': 1, 'lastname': 1})
