
from telegram.ext import CommandHandler, MessageHandler, Filters
import requests
import database.users
from secrets import SUDO_ONLY


def update_user(update, context):
    usr = update.effective_user

    database.users.update_user(
        usr.id, usr.username, usr.first_name, usr.last_name
    )


def users(update, context):
    all_ = database.users.all_users()
    res = ""

    for user in all_:
        res += user["firstname"] + " - " + str(user["id"]) + "\n"

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
            Filters.all & ~ Filters.chat_type.channel,
            update_user,
            run_async=True
        ),
        7
    ],
    [
        CommandHandler(
            "uzerz",
            users,
            filters=SUDO_ONLY,
            run_async=True
        )
    ]
]
