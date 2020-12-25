from telegram.ext import CommandHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def start(update, context):
    usr = update.message.from_user

    BUTTON_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="➕ Add me to your group ➕",url="http://t.me/{botusername}?startgroup=start".format(botusername=context.bot.username))
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
    4️⃣ <a href="https://t.me/AntiSpamInc">AntiSpamInc</a>

Send /help to learn more about me and my commands.
""").format(id = usr.id, firstname = usr.first_name, botname = context.bot.first_name), parse_mode= 'HTML', reply_markup= BUTTON_MARKUP, disable_web_page_preview=True)

__handlers__ = [
    [CommandHandler("start", start, filters=Filters.chat_type.private, run_async= True)]
]