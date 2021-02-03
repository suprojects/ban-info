import html

import utils.advinfo as advinfo
from database import botusers
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (CallbackQueryHandler, CommandHandler, Filters,
                          MessageHandler)
from telegram.utils import helpers


def checkme(update, context):

    msg = update.message
    userinfo = update.message.from_user

    message = msg.reply_text(text="🔄")
    

    text = f"""
👤 Name: {(html.escape("" if userinfo.first_name == None else userinfo.first_name) + html.escape("" if userinfo.last_name == None else userinfo.last_name))}
📛 Username: @{html.escape("" if userinfo.username == None else userinfo.username)}
🆔 ID: {userinfo.id}

{advinfo.check(userinfo.id)}
"""

    message.edit_text(text=text, parse_mode="HTML", disable_web_page_preview=True)

    botusers.new_user(update.message.from_user)


def checkme_group(update, context):

    delete_button = InlineKeyboardButton("OK", callback_data=(
        "delete_{userid}").format(userid=update.message.from_user.id))

    checkme_button = InlineKeyboardButton(
        "Check my ban info", url=helpers.create_deep_linked_url(context.bot.username, "checkme"))

    keyboard = InlineKeyboardMarkup(
        [
            [checkme_button],
            [delete_button]
        ]
    )

    update.message.reply_text(
        text="Check your ban info by clicking on this button. Anyone can check their own ban info by using this button.", reply_markup=keyboard, quote=True)


def checkme_callback(update, context):
    update.callback_query.answer(
        url=helpers.create_deep_linked_url(context.bot.username, "checkme"))


__handlers__ = [

    [CommandHandler("checkme", checkme, filters=Filters.chat_type.private, run_async=True)],
    [CallbackQueryHandler(callback=checkme_callback, pattern="^checkme_$", run_async=True)],
    [CommandHandler("start", checkme, filters=Filters.regex(pattern="^/start checkme$"), run_async=True)],
    [CommandHandler("checkme", checkme_group, filters=Filters.chat_type.groups, run_async=True)],
]
