from telegram.ext import CommandHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def help_text(update, context):
    usr = update.message.from_user

    BUTTON_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="Our Channel 🔈", url = "https://t.me/su_Bots"),
            InlineKeyboardButton(text="Discussion group 👥", url="https://t.me/su_Chats")
        ]
    ]
)

    update.message.reply_text(text=("""

As you would have read in the /start, I can scan members against Telegram's leading Anti-Spam databases.

👥 <b>Group Commands:</b>

1️⃣ /check - Send /check as a reply to a user's message to check the bans of the user.
2️⃣ /checkme - To check the ban info of yourself in a group.

👤 <b>Private Commands:</b>

1️⃣ /start - Sends the introductory start message.
2️⃣ /help - Sends this Help message.
3️⃣ /checkme - Check the ban info of yourself.

🤫 <b>Privacy mode:</b>

To protect your privacy in your groups, <a href='https://core.telegram.org/bots#privacy-mode'>Privacy mode</a> is turned on in this bot. Hence, I will not be able to see the normal messages you send in your group.

But on the downside 👎, I will not be able to see if you send commands like <code>/check</code>. To overcome this, please send the commands like <code>/check@{botusername}</code>.

""").format(id = usr.id, firstname = usr.first_name, botname = context.bot.first_name, botusername = context.bot.username), parse_mode= 'HTML', reply_markup= BUTTON_MARKUP, disable_web_page_preview=True)

__handlers__ = [
    [CommandHandler("help", help_text, filters=Filters.chat_type.private)]
]