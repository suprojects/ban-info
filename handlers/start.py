from telegram.ext import CommandHandler, Filters
from helpers import asi, cas, sp, sw

def start_pvt(update, context):
    usr, msg = update.message.from_user, update.message
#try:
    if msg.reply_to_message:

        fwdusr = msg.reply_to_message.from_user
        context.bot.send_chat_action(update.message.chat.id, "typing")
        msg.reply_text(text=("""

👥 Info of <a href="tg://user?id={id}">{firstname}</a>:
🔖 User ID: <code>{id}</code>
🦅 SpamWatch Banned: <code>{SW}</code>
🤖 CAS Banned: <code>{CAS}</code>
✉ Spam Protection Banned: <code>{SPB}</code>
⛔️AntiSpamInc Banned: <code>{ASI}</code>

""").format(

    firstname = str(fwdusr.first_name),
    id=fwdusr.id,
    SW=sw.check(fwdusr.id),
    CAS=cas.check(fwdusr.id),
    SPB=sp.check(fwdusr.id),
    ASI=asi.check(fwdusr.id)

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
