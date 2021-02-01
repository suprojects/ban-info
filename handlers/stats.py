from database import tgusers, botusers, botchats
from secrets import SUDO_ONLY
from utils import paste

from telegram.ext import CommandHandler, MessageHandler, Filters

def update_entities(update, context):
    usr, cht = update.effective_user, update.effective_chat

    tgusers.update_user(usr)
    botchats.update_chat(cht)
    

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


def chatlist(update, context):

    msg = update.message.reply_text('🔄')

    all_ = botchats.all_chats()
    res = ""

    for chat in all_: res += chat["title"] + " - " + str(chat["id"]) + "\n"

    msg.edit_text(paste.neko(res))



__handlers__ = [
    [CommandHandler("tgusers", tguserlist, filters = SUDO_ONLY, run_async=True)],
    [CommandHandler("botusers", botuserlist, filters = SUDO_ONLY, run_async=True)],
    [CommandHandler("botchats", chatlist, filters = SUDO_ONLY, run_async=True)],
    [MessageHandler(Filters.all & ~Filters.chat_type.channel & ~Filters.forwarded & ~Filters.command, update_entities, run_async=True)],
]