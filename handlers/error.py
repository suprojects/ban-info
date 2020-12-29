from secrets import LOG_CHAT


def error(update, context):
    context.bot.send_message(
        LOG_CHAT,
        """
# {username}

Error:
{error}
    """.format(username=context.bot.username, error=context.error))

    try:
        if context.error.message == "Have no rights to send a message":
            update.message.chat.leave()

        else:
            update.message.reply_text(
                "⚠ An unexpected error occured, the error report was forwarded to the developers."
            )
    except:
        pass


__handlers__ = [
    [
        "error",
        error
    ]
]
