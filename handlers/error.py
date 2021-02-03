from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from secrets import LOG_CHAT


def error(update, context):

    try:
        if context.error.message == "Have no rights to send a message":
            update.message.chat.leave()
            return

        elif context.error.message == "Conflict: terminated by other getUpdates request; make sure that only one bot instance is running":
            return

        else:
            update.message.reply_text("⚠ An unexpected error occured, the error report was forwarded to the developers.", reply_markup=(
                [[InlineKeyboardButton("OK", callback_data=f"delete_{update.message.from_user.id}")]]))
    except:
        pass

    context.bot.send_message(
        LOG_CHAT, f"#{context.bot.username}\n\n\nError:\n{context.error}\n\nUpdate:\n{update}"
    )


__handlers__ = [
    ["error", error]
]
