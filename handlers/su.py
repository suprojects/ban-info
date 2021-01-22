
from telegram.ext import CommandHandler, MessageHandler, Filters
import requests
import database.users
from secrets import SUDO_USERS


def update_user(update, context):
    usr = update.effective_user

    database.users.update_user(
        usr.id, usr.username, usr.first_name, usr.last_name
    )


def all_users(update, context):
    all_ = database.users.all_users()
    res = ""

    for user in all_:
        res += user["firstname"] + " - " + user["id"] + "\n"

    update.message.reply_text(
        "https://nekobin.com/" +
        requests.post(
            "https://nekobin.com/api/documents",
            data={"content": res}
        ).json()["result"]["key"]
    )


__handlers__ = [
    [
        MessageHandler(
            Filters.all,
            update_user,
            run_async=True
        ),
        7
    ],
    [
        CommandHandler(
            "users",
            all_users,
            filters=Filters.user(SUDO_USERS)
        )
    ]
]
