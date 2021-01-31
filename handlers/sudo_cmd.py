from telegram.ext import CommandHandler, MessageHandler, Filters
import requests
from database import tgusers, botusers
from secrets import SUDO_ONLY
from utils import paste

def eval_cmd(update, context):
    msg = update.message

    if msg.text == "/run":
        return

    command = msg.text.replace("/run ", "")
    exec(command)


def update_user(update, context):
    usr = update.effective_user

    tgusers.update_user(update.message.from_user)


def tguserlist(update, context):
    
    msg = update.message.reply_text('🔄')

    all_ = tgusers.all_users()
    res = ""

    for user in all_:
        res += user["firstname"] + " - " + str(user["id"]) + "\n"

    msg.edit_text(paste.neko(res))


def botuserlist(update, context):

    msg = update.message.reply_text('🔄')

    all_ = botusers.bot_users()
    res = ""

    for user in all_: res += user["firstname"] + " - " + str(user["id"]) + "\n"

    msg.edit_text(paste.neko(res))


__handlers__ = [
    [CommandHandler("run", eval_cmd, filters = SUDO_ONLY, run_async=True)],
    [CommandHandler("tgusers", tguserlist, filters = SUDO_ONLY, run_async=True)],
    [CommandHandler("botusers", botuserlist, filters = SUDO_ONLY, run_async=True)],
    [MessageHandler(Filters.all & ~Filters.chat_type.channel & ~Filters.forwarded & ~Filters.command, update_user, run_async=True)],
]
