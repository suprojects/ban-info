from secrets import SUDO_USERS
from telegram.ext import CommandHandler, Filters

def eval_cmd(update, context):
    msg = update.message

    if msg.text == '/run':
        return

    command = msg.text.replace('/run ', '')
    exec(command)


__handlers__ = [
    [CommandHandler("run", eval_cmd, filters=Filters.user(SUDO_USERS), run_async=True)],
]