from telegram.ext import CommandHandler, Filters


def start_group(update, context):
    update.message.reply_text("I am Alive! 🤖")


__handlers__ = [
    [
        CommandHandler(
            "start",
            start_group,
            filters=Filters.chat_type.groups,
            run_async=True
        )
    ]
]
