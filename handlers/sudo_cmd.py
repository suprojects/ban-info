from telegram.ext import CommandHandler
from secrets import SUDO_ONLY


def eval_cmd(update, context):
    msg = update.message

    if msg.text == "/run":
        return

    command = msg.text.replace("/run ", "")
    exec(command)


__handlers__ = [
    [CommandHandler("run", eval_cmd, filters=SUDO_ONLY, run_async=True)],
]
