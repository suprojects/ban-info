from secrets import LOG_ID

def error(update, context):

    context.bot.send_message(chat_id = LOG_ID, text=("""

#{username}

Error:
{error}

""").format(username = context.bot.username, error = context.error))

    try:
        if context.error.message == "Have no rights to send a message":
            update.message.chat.leave()

        else:
            update.message.reply_text("An unexpected error occured ⚠. Error report forwarded.")
        
    except:
        pass

__handlers__ = [["error", error, run_async= True]]