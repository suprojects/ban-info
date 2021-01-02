from html import escape

from telegram.ext import CommandHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.utils import helpers


def start(update, context):
    usr = update.message.from_user

    BUTTON_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="➕ Add me to your group ➕", url=helpers.create_deep_linked_url(context.bot.username, "start", True))
        ],
    ]
)

    update.message.reply_text(text=("""

Hey there <a href="tg://user?id={id}">{firstname}</a> 👋. I am {botname} 🤖.

I can scan members in your group against Telegram's biggest Anti-Spam Databases like <a href="https://t.me/SpamWatch">SpamWatch</a>, so that you can know if they are spammers or not 😁.

I can currently search in:

    1️⃣ <a href="https://t.me/SpamWatch">SpamWatch</a>
    2️⃣ <a href="https://cas.chat/">Combot Anti-Spam System</a>
    3️⃣ <a href="https://t.me/SpamProtectionBot">Spam Protection</a> (by <a href="https://intellivoid.net/">Intellivoid</a>)
    4️⃣ <a href="https://t.me/NoSpamPlus">NoSpam+</a>
    5️⃣ <a href="https://t.me/SpamBlockers">SpamBlockers</a>

Send /help to learn more about me and my commands.
""").format(id = usr.id, firstname = escape(usr.first_name), botname = context.bot.first_name), parse_mode= 'HTML', reply_markup= BUTTON_MARKUP, disable_web_page_preview=True)


def start_group(update, context):
    delete_button = InlineKeyboardButton("OK", callback_data=("delete_{userid}").format(userid = update.message.from_user.id))
    update.message.reply_text("I am Alive! 🤖", reply_markup = InlineKeyboardMarkup([[delete_button]]))


__handlers__ = [
    [CommandHandler("start", start, filters=Filters.chat_type.private & Filters.regex('^/start$'), run_async=True)],
    [CommandHandler("start", start_group, filters=Filters.chat_type.groups, run_async=True)]
]   