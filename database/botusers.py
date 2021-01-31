from database import db

botusers = db['botusers']

def new_user(from_user):

    from database import tgusers
    tgusers.update_user(from_user)

    botusers.update_one(
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


def remove_user(userid):
    botusers.delete_one({"id": userid})

def bot_users():
    return list(botusers.find())
