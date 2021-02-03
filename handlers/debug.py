from html import escape
from secrets import SUDO_ONLY

from apis import cas, nsp, sb, sp, sw
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, Filters
from telegram.utils import helpers


def debug(update, context):

    usr, msg = update.message.reply_to_message.from_user, update.message

    message = msg.reply_text("🔄 Sending Debug Message...")

    SpamWatch = sw.check(usr.id)
    CAS = cas.check(usr.id)
    SpamProtection = sp.check(usr.id)
    NoSpamPlus = nsp.check(usr.id)
    SpamBlockers = sb.check(usr.id)

    delete_button = InlineKeyboardButton("OK", callback_data=(
        "delete_{userid}").format(userid=update.message.from_user.id))
    more_info = InlineKeyboardButton("Detailed Ban Info", helpers.create_deep_linked_url(
        context.bot.username, "check_{id}".format(id=usr.id)))

    keyboard = InlineKeyboardMarkup([[delete_button], [more_info]])

    message.edit_text(text=("""

First Name: {first}
Last Name: {last}
ID: {id}

SpamWatch: {SW}

CAS: {CAS}

Spam Protection: {SP}

No Spam Plus: {NSP}

SpamBlockers: {SB}

""").format(
        first=escape("" if usr.first_name == None else usr.first_name),
        last=escape("" if usr.last_name == None else usr.last_name),
        id=usr.id,
        SW=SpamWatch,
        CAS=CAS,
        SP=SpamProtection,
        NSP=NoSpamPlus,
        SB=SpamBlockers,
    ), reply_markup=keyboard, disable_web_page_preview=True)


__handlers__ = [
    [CommandHandler("debug", debug, filters=SUDO_ONLY &
                    Filters.chat_type.groups & Filters.reply, run_async=True)]
]
