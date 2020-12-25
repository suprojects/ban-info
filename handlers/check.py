from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, Filters
from helpers import asi, cas, sp, sw

deleteButton = InlineKeyboardButton("OK", callback_data="delete")
moreinfo = InlineKeyboardButton("Detailed Ban Info", callback_data="advinfo")


def check(update, context):

    usr, msg = update.message.from_user, update.message
    userinfo = msg.reply_to_message.from_user

    context.bot.send_chat_action(update.message.chat.id, "typing")

    SpamWatch = sw.check(userinfo.id)
    CAS = cas.check(userinfo.id)
    SpamProtection = sp.check(userinfo.id)
    AntiSpamInc = asi.check(userinfo.id)

    BUTTONS = InlineKeyboardMarkup([
        [moreinfo],
        [deleteButton],
    ])

    s = msg.reply_text(text=("""

👤 Name: {firstname} {lastname}
🆔 ID: <code>{id}</code>
🔗 Permanent Link: <a href="tg://user?id={id}">{firstname}</a>

🦅 SpamWatch Banned: <code>{SW}</code>
🤖 CAS Banned: <code>{CAS}</code>
✉ Spam Protection Blacklisted: <code>{SPB}</code>
⛔ Potential Spammer (By Spam Protection): <code>{SP}</code>
🛡 AntiSpamInc Banned: <code>{ASI}</code>

✅ Initiated by <a href="tg://user?id={initid}">{initfirstname}</a>
""").format(

        firstname="" if userinfo.first_name == None else userinfo.first_name,
        lastname="" if userinfo.last_name == None else userinfo.last_name,
        id=userinfo.id,
        initid=usr.id,
        initfirstname=usr.first_name,
        SW=SpamWatch.get('is_Banned', False),
        CAS=CAS.get('is_Banned', False),
        SPB=SpamProtection.get('is_Banned', 'Not in records'),
        SP=SpamProtection.get('is_Potential', 'Not in records'),
        ASI=AntiSpamInc.get('is_Banned', False)

    ), parse_mode='HTML', reply_markup=BUTTONS)
    

def no_reply(update, context):
    BUTTONS = InlineKeyboardMarkup([[deleteButton]])
    
    update.message.reply_text(text=("You will need to reply to a user's message to get the info 🔗"), reply_markup=BUTTONS)


__handlers__ = [

    [CommandHandler('check', check, filters=Filters.chat_type.groups & Filters.reply, run_async=True)],
    [CommandHandler('check', no_reply, filters=Filters.chat_type.groups & ~ Filters.reply, run_async=True)]
]
