from helpers import advinfo
import html
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, Filters, CallbackQueryHandler
from telegram.utils import helpers



def checkme(update, context):

    userinfo, msg = update.message.from_user, update.message

    context.bot.send_chat_action(update.message.chat.id, "typing")

    BanInfo = advinfo.check(userinfo.id)

    msg.reply_text(text = ("""

👤 Name: {firstname} {lastname}
🆔 ID: <code>{id}</code>
🔗 Permanent Link: <a href="tg://user?id={id}">{firstname} {lastname}</a>

{SpamWatch}
{CAS}
{SpamProtection}
{NoSpamPlus}

""").format(
    firstname= html.escape("" if userinfo.first_name == None else userinfo.first_name),
    lastname= html.escape("" if userinfo.last_name == None else userinfo.last_name),
    id=userinfo.id,
    SpamWatch = BanInfo['SpamWatch'],
    CAS = BanInfo['CAS'],
    SpamProtection = BanInfo['SpamProtection'],
    NoSpamPlus = BanInfo['NoSpamPlus'],

), parse_mode = "HTML", disable_web_page_preview = True, quote = False)


def checkme_group(update, context):

    delete_button = InlineKeyboardButton("OK", callback_data=("delete_{userid}").format(userid = update.message.from_user.id))

    checkme_button = InlineKeyboardButton("Check my ban info", url = helpers.create_deep_linked_url(context.bot.username, "checkme"))

    keyboard = InlineKeyboardMarkup(
        [
            [checkme_button],
            [delete_button]
        ]
    )

    update.message.reply_text(text = "Check your ban info by clicking on this button. Anyone can check their own ban info by using this button.", reply_markup=keyboard, quote = True)

def checkme_callback(update, context):
    update.callback_query.answer(url = helpers.create_deep_linked_url(context.bot.username, "checkme"))


__handlers__ = [

    [CommandHandler("checkme", checkme, filters=Filters.chat_type.private, run_async=True)],
    [CallbackQueryHandler(callback = checkme_callback, pattern = "^checkme_$", run_async=True)],  
    [CommandHandler('start', checkme, filters = Filters.regex(pattern = "^/start checkme$"), run_async = True)],
    [CommandHandler("checkme", checkme_group, filters=Filters.chat_type.groups, run_async=True)], 
]
