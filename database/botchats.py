from database import db

chats = db["chats"]

def update_chat(chat_entity):
    chats.update_one(
        {"id": chat_entity.id},
        {
            "$set": {
                "title": chat_entity.title,
                "username": chat_entity.username,
                "type": chat_entity.type,
            }
        },
        upsert=True,
    )

def remove_chat(chatid):
    chats.delete_one({"id": chatid})

def all_chats():
    return list(chats.find({}, {'title': 1, 'id': 1, 'username': 1, 'type': 1}))
