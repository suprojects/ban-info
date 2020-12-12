from telegram.ext import CommandHandler, Filters
from helpers import asi, cas, sp, sw

def start_pvt(update, context):
    usr, msg = update.message.from_user, update.message
#try:
    if msg.reply_to_message:

        fwdusr = msg.reply_to_message.from_user
        context.bot.send_chat_action(update.message.chat.id, "typing")
        msg.reply_text(text=("""

👥 <a href="tg://user?id={id}">{firstname}</a>
🆔 <code>{id}</code>

🦅 SpamWatch Banned: <code>{SW}</code>
🤖 CAS Banned: <code>{CAS}</code>
✉ Spam Protection Banned: <code>{SPB}</code>
⛔️ AntiSpamInc Banned: <code>{ASI}</code>

""").format(

    firstname = str(fwdusr.first_name),
    id=fwdusr.id,
    SW="YES" if sw.check(fwdusr.id) else "NO",
    CAS="YES" if cas.check(fwdusr.id) else "NO",
    SPB="YES" if sp.check(fwdusr.id) else "NO",
    ASI="YES" if asi.check(fwdusr.id) else "NO"

    ), parse_mode = 'HTML'
)

    else:
        msg.reply_text("You need to a message from a user!")
#except:
#    msg.reply_text("An unexpected error occured, try telling us about it in @su_BotsChat.")


__handlers__ = [
    [
        CommandHandler(
            "start",
            start_pvt,
            Filters.chat_type.supergroup
        )
    ]
]
