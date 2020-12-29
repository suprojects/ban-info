from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, Filters
from telegram.utils import helpers
from helpers import asi, cas, sp, sw

delete_button = InlineKeyboardButton("OK", callback_data="delete")

def check(update, context):
    usr, msg = update.message.from_user, update.message
    userinfo = msg.reply_to_message.from_user

    context.bot.send_chat_action(update.message.chat.id, "typing")

    SpamWatch = sw.check(userinfo.id)
    CAS = cas.check(userinfo.id)
    SpamProtection = sp.check(userinfo.id)
    AntiSpamInc = asi.check(userinfo.id)

    more_info = InlineKeyboardButton("Detailed Ban Info", helpers.create_deep_linked_url(context.bot.username, "check_{id}".format(id=userinfo.id)))

    keyboard = InlineKeyboardMarkup(
        [
            [more_info],
            [delete_button],
        ]
    )

    msg.reply_text(text = ("""

👤 Name: {firstname} {lastname}
🆔 ID: <code>{id}</code>
🔗 Permanent Link: <a href="tg://user?id={id}">{firstname}</a>

🦅 SpamWatch Banned: <code>{SW}</code>
🤖 CAS Banned: <code>{CAS}</code>
✉ Spam Protection Blacklisted: <code>{SPB}</code>
⛔ Potential Spammer (By Spam Protection): <code>{SP}</code>
⚡️ AntiSpamInc Banned: <code>{ASI}</code>

✅ Initiated by <a href="tg://user?id={initid}">{initfirstname}</a>
""").format(
        firstname="" if userinfo.first_name == None else userinfo.first_name,
        lastname="" if userinfo.last_name == None else userinfo.last_name,
        id=userinfo.id,
        initid=usr.id,
        initfirstname=usr.first_name,
        SW=SpamWatch.get("is_Banned", False),
        CAS=CAS.get("is_Banned", False),
        SPB=SpamProtection.get("is_Banned", "Not in records"),
        SP=SpamProtection.get("is_Potential", "Not in records"),
        ASI=AntiSpamInc.get("is_Banned", False)

    ), parse_mode = 'HTML', reply_markup=keyboard)


def no_reply(update, context):

    update.message.reply_text("Reply to a user's message to get the info", reply_markup = InlineKeyboardMarkup([[delete_button]]))


__handlers__ = [
    [CommandHandler("check", check, filters=Filters.chat_type.groups & Filters.reply, run_async=True)],
    [CommandHandler("check", no_reply, filters=Filters.chat_type.groups & ~ Filters.reply, run_async=True)]
]
