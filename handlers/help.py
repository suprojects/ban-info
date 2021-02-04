from database.botusers import new_user
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, Filters


def help_text(update, context):

    BUTTON_MARKUP = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(text="Our Channel 🔈",
                                 url="https://t.me/su_Bots"),
            InlineKeyboardButton(text="Discussion group 👥",
                                 url="https://t.me/su_Chats")
        ]
    ])

    update.message.reply_text("""
As you would have read in the /start, I can scan members against Telegram"s leading Anti-Spam databases.

👥 <b>Group Commands:</b>

1️⃣ /check - Send /check as a reply to a user"s message to check the ban info of the user.
2️⃣ /check @username - Check the ban info of the user by passing the username.
3️⃣ /check <code>userid</code> - Check the info by passing the userid.

👤 <b>Private Commands:</b>

1️⃣ /start - Sends the introductory start message.
2️⃣ /help - Sends this Help message.
3️⃣ /checkme - Check the ban info of yourself.
4️⃣ Forward me any user"s message to check the info.
5️⃣ /check @username - Check the ban info of the user by passing the username.
6️⃣ /check <code>userid</code> - Check the info by passing the userid.

""".format(botusername=context.bot.username), parse_mode="HTML", disable_web_page_preview=True, reply_markup=BUTTON_MARKUP)

    new_user(update.message.from_user)

__handlers__ = [
    [CommandHandler("help", help_text, filters=Filters.chat_type.private, run_async=True)],
]
