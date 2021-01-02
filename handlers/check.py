from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, Filters, CallbackQueryHandler
from helpers import nsp, cas, sp, sw, sb, advinfo
from html import escape
from re import search


def check(update, context):
    usr, msg = update.message.from_user, update.message
    userinfo = msg.reply_to_message.from_user

    message = msg.reply_text("🔄 Processing...")

    context.bot.send_chat_action(update.message.chat.id, "typing")

    SpamWatch = sw.check(userinfo.id)
    CAS = cas.check(userinfo.id)
    SpamProtection = sp.check(userinfo.id)
    NoSpamPlus = nsp.check(userinfo.id)
    SpamBlockers = sb.check(userinfo.id)

    delete_button = InlineKeyboardButton("OK", callback_data=("delete_{userid}").format(userid = update.message.from_user.id))
    more_info = InlineKeyboardButton("Detailed Ban Info", callback_data = ("check_{userid}").format(userid = userinfo.id))

    buttons = InlineKeyboardMarkup(
        [
            [more_info],
            [delete_button],
        ]
    )

    message.edit_text(text = ("""

👤 Name: <a href="tg://user?id={id}">{firstname} {lastname}</a>
🆔 ID: <code>{id}</code>

🦅 SpamWatch Banned: <code>{SW}</code>
🤖 CAS Banned: <code>{CAS}</code>
✉ Spam Protection Blacklisted: <code>{SPB}</code>
⛔ Potential Spammer (By Spam Protection): <code>{SP}</code>
➕ NoSpamPlus Banned: <code>{NSP}</code>
🐞 SpamBlockers Banned: <code>{SB}</code>

✅ Initiated by <a href="tg://user?id={initid}">{initfirstname}</a>
""").format(
        firstname=escape("" if userinfo.first_name == None else userinfo.first_name),
        lastname=escape("" if userinfo.last_name == None else userinfo.last_name),
        id=userinfo.id,
        initid=usr.id,
        initfirstname=escape(usr.first_name),
        SW=SpamWatch.get("is_Banned", False),
        CAS=CAS.get("is_Banned", False),
        SPB=SpamProtection.get("is_Banned", "Not in records"),
        SP=SpamProtection.get("is_Potential", "Not in records"),
        NSP=NoSpamPlus.get("is_Banned", False),
        SB=SpamBlockers.get('is_Banned', False),

    ), parse_mode = 'HTML', reply_markup=buttons)


def no_reply(update, context):
    delete_button = InlineKeyboardButton("OK", callback_data=("delete_{userid}").format(userid = update.message.from_user.id))
    update.message.reply_text("Reply to a user's message to get the info", reply_markup = InlineKeyboardMarkup([[delete_button]]))


def check_callback(update, context):
    
    userid = int(update.callback_query.data.replace('check_', ''))

    BanInfo = advinfo.check_small(userid)
    BanText = ("{SpamWatch}\n{CAS}\n{SpamProtection}\n{NoSpamPlus}\n{SpamBlockers}").format(SpamWatch = BanInfo['SpamWatch'], CAS = BanInfo['CAS'], SpamProtection = BanInfo['SpamProtection'], NoSpamPlus = BanInfo['NoSpamPlus'], SpamBlockers = BanInfo['SpamBlockers'])

    update.callback_query.answer(text = BanText, show_alert = True)


__handlers__ = [
    [CommandHandler("check", check, filters=Filters.chat_type.groups & Filters.reply, run_async=True)],
    [CommandHandler("check", no_reply, filters=Filters.chat_type.groups & ~ Filters.reply, run_async=True)],
    [CallbackQueryHandler(pattern = "^check_", callback = check_callback, run_async=True)],
]