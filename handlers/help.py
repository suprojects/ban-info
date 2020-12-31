from telegram.ext import CommandHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def help_text(update, context):

    BUTTON_MARKUP = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(text="Our Channel 🔈", url="https://t.me/su_Bots"),
                InlineKeyboardButton(text="Discussion group 👥",url="https://t.me/su_Chats")
            ]
        ])

    update.message.reply_text("""
As you would have read in the /start, I can scan members against Telegram"s leading Anti-Spam databases.

👥 <b>Group Commands:</b>

1️⃣ /check - Send /check as a reply to a user"s message to check the ban info of the user.

👤 <b>Private Commands:</b>

1️⃣ /start - Sends the introductory start message.
2️⃣ /help - Sends this Help message.
3️⃣ /checkme - Check the ban info of yourself.

🤫 <b>Privacy mode:</b>

To protect your privacy in your groups, <a href="https://core.telegram.org/bots#privacy-mode">Privacy mode</a> is turned on in this bot. Hence, I will not be able to see the normal messages you send in your group.

But on the downside 👎, I will not be able to see if you send commands like <code>/check</code>. To overcome this, please send the commands like <code>/check@{botusername}</code>.

""".format(botusername=context.bot.username), parse_mode = "HTML", disable_web_page_preview = True, reply_markup = BUTTON_MARKUP)


__handlers__ = [
    [CommandHandler("help", help_text, filters=Filters.chat_type.private, run_async=True)]
]
