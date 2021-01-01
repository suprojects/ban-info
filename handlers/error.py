from secrets import LOG_CHAT
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

delete_button = InlineKeyboardButton("OK", callback_data="delete")

def error(update, context):

    context.bot.send_message(chat_id = LOG_CHAT, text = ("""

#{username}

User ID: {userid}
Chat ID: {chatid}

Error:
{error}

Update:
{update}

""").format(username=context.bot.username, userid = "" if update.message.from_user.id == None else update.message.from_user.id, chatid = "" if update.message.chat.id == None else update.message.chat.id, error=context.error, update = update))

    try:
        if context.error.message == "Have no rights to send a message":
            update.message.chat.leave()

        else:
            update.message.reply_text("⚠ An unexpected error occured, the error report was forwarded to the developers.", reply_markup = ([[delete_button]]))  
    except:
        pass


__handlers__ = [
    ["error",error]
]