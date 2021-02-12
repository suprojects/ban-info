from secrets import SUDO_ONLY

from database import botchats, botusers, tgusers
from telegram.ext import CommandHandler, Filters, MessageHandler
from utils import paste


def update_entities(update, context):
    tgusers.update_user(update.effective_user)
    botchats.update_chat(update.effective_chat)
    

def tguserlist(update, context):
    
    msg = update.message.reply_text('🔄')

    all_ = tgusers.all_users()
    res = ""

    for user in all_: 
        if user["firstname"] != "":
            res += user["firstname"] + " - " + str(user["id"]) + f' - @{user["username"]}' if user.get('username') else '' + "\n"
        else:
            res += user["firstname"] + " - " + str(user["id"]) + "\n"

    msg.edit_text(paste.neko(res))


def botuserlist(update, context):

    msg = update.message.reply_text('🔄')

    all_ = botusers.bot_users()
    res = ""

    for user in all_: res += user["firstname"] + " - " + str(user["id"]) + f' - @{user["username"]}' if user.get('username') else '' + "\n"

    msg.edit_text(paste.neko(res))


def chatlist(update, context):

    msg = update.message.reply_text('🔄')

    all_ = botchats.all_chats()
    res = ""

    for chat in all_: res += chat["title"] + " - " + str(chat["id"]) + f' - @{chat["username"]}' if chat.get('username') else '' + f' - {chat["type"]}' if chat.get('type') + "\n"

    msg.edit_text(paste.neko(res))


def stats(update, context):
    msg = update.message.reply_text('🔄')

    msg.edit_text(text = f'''
Stats of {context.bot.first_name}

👤 @{context.bot.username}
🆔 <code>{context.bot.id}</code>

👀 Users seen: <code>{len(tgusers.all_users())}</code>
🤖 Bot users: <code>{len(botusers.bot_users())}</code>
👥 Groups: <code>{len(botchats.all_chats())}</code>

''', parse_mode = 'HTML')


__handlers__ = [
    [CommandHandler("tgusers", tguserlist, filters = SUDO_ONLY, run_async=True)],
    [CommandHandler("botusers", botuserlist, filters = SUDO_ONLY, run_async=True)],
    [CommandHandler("botchats", chatlist, filters = SUDO_ONLY, run_async=True)],
    [CommandHandler("botstats", stats, filters = SUDO_ONLY, run_async=True)],

    [MessageHandler(Filters.all & Filters.chat_type.supergroup & ~Filters.forwarded & ~Filters.command, update_entities, run_async=True)],
]
