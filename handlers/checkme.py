from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, Filters
from helpers import asi, cas, sp, sw

deleteButton = InlineKeyboardButton("OK", callback_data="delete")
checkmeButton = InlineKeyboardButton("Check my ban info", callback_data="checkme")

def checkme(update, context):

    userinfo, msg = update.message.from_user, update.message

    context.bot.send_chat_action(update.message.chat.id, "typing")
    
    SpamWatch = sw.check(userinfo.id)
    CAS = cas.check(userinfo.id)
    SpamProtection = sp.check(userinfo.id)
    AntiSpamInc = asi.check(userinfo.id)

    msg.reply_text(text=("""

👤 Name: {firstname} {lastname}
🆔 ID: <code>{id}</code>
🔗 Permanent Link: <a href="tg://user?id={id}">{firstname}</a>

🦅 SpamWatch Banned: <code>{SW}</code>
🤖 CAS Banned: <code>{CAS}</code>
✉ Spam Protection Blacklisted: <code>{SPB}</code>
⛔ Potential Spammer (By Spam Protection): <code>{SP}</code>
⚡️ AntiSpamInc Banned: <code>{ASI}</code>

""").format(

firstname = "" if userinfo.first_name == None else userinfo.first_name,
lastname = "" if userinfo.last_name == None else userinfo.last_name,
id = userinfo.id,
SW = SpamWatch.get('is_Banned', False),
CAS = CAS.get('is_Banned', False),
SPB = SpamProtection.get('is_Banned', 'Not in records'),
SP = SpamProtection.get('is_Potential', 'Not in records'),
ASI = AntiSpamInc.get('is_Banned', False)

), parse_mode = 'HTML')

def checkme_group(update, context):
    BUTTONS = InlineKeyboardMarkup([
        [checkmeButton],
        [deleteButton]
    ])
    update.message.reply_text(text="Check your ban info by clicking on this button", reply_markup=BUTTONS)

__handlers__ = [

    [CommandHandler("checkme", checkme, filters = Filters.chat_type.private, run_async=True)],
    [CommandHandler("checkme", checkme_group, filters = Filters.chat_type.groups, run_async=True)]
]