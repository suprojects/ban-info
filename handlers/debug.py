from secrets import SUDO_USERS
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, Filters
from helpers import asi, cas, sp, sw


def debug(update, context):

    usr, msg = update.message.reply_to_message.from_user, update.message

    SpamWatch = sw.check(usr.id)
    CAS = cas.check(usr.id)
    SpamProtection = sp.check(usr.id)
    AntiSpamInc = asi.check(usr.id)

    delete_button = InlineKeyboardButton("OK", callback_data="delete")
    keyboard = InlineKeyboardMarkup([[delete_button]])

    msg.reply_text(
        """Name: {name}
ID: {id}

SpamWatch:
{SW}

CAS:
{CAS}

Spam Protection:
{SP}

Anti Spam Inc:
{ASI}
        """.format(
            name=usr.first_name,
            id=usr.id,
            SW=SpamWatch,
            CAS=CAS,
            SP=SpamProtection,
            ASI=AntiSpamInc
        ),
        reply_markup=keyboard
    )


__handlers__ = [
    [
        CommandHandler(
            "debug",
            debug,
            filters=Filters.user(SUDO_USERS)
            & Filters.chat_type.groups
            & Filters.reply,
            run_async=True
        )
    ]
]
