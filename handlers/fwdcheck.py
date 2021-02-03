import html

from utils import advinfo
from database import botusers
from telegram.ext import Filters, MessageHandler


def fwdcheck(update, context):

    msg, userinfo = update.message, update.message.forward_from

    if update.message.forward_sender_name:
        msg.reply_text(f"{update.message.forward_sender_name} has hidden forwards linking ⏩🔗. Hence, details cannot be displayed")
        return

    message = msg.reply_text(text="🔄")


    text = f"""
👤 Name: {(html.escape("" if userinfo.first_name == None else userinfo.first_name) + html.escape("" if userinfo.last_name == None else userinfo.last_name))}
📛 Username: @{html.escape("" if userinfo.username == None else userinfo.username)}
🆔 ID: {userinfo.id}

{advinfo.check(userinfo.id)}
"""

    message.edit_text(text=text, parse_mode="HTML", disable_web_page_preview=True)

    botusers.new_user(userinfo)
    botusers.new_user(update.message.from_user)


__handlers__ = [
    [MessageHandler(callback=fwdcheck, filters=Filters.chat_type.private & Filters.forwarded, run_async=True)],
]