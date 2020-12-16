def error(update, context):
    if context.error.message == "Have no rights to send a message":
        update.message.chat.leave()

__handlers__ = [["error", error]]