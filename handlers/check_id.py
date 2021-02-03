import html
import re

from apis import cas, nsp, owl, sb, sp, sw
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, Filters
from utils import get_user


def check_id(update, context):
    usr, msg = update.message.from_user, update.message

    message = msg.reply_text("🔄")

    attr = context.args

    deleteButton = InlineKeyboardButton("OK", callback_data=(f"delete_{usr.id}"))

    if int(len(attr)) == 0:
        message.edit_text(
            text = "Reply to a user's message to get the info or pass a Telegram Username/id" if msg.chat.type != 'private' else "Forward a message, or pass a Telegram Username/id",
            reply_markup=InlineKeyboardMarkup([[deleteButton]]) if msg.chat.type != 'private' else None
        )
        return

    userInfo = get_user.find(attr[0])

    if not userInfo:
        message.edit_text(
            text = f'I am not sure I have seen that user <code>{html.escape(attr[0])}</code> anywhere 👀. Maybe just forward one of the messages to me in private and I will remember it, forever ♾.',
            parse_mode = 'HTML',
            reply_markup = InlineKeyboardMarkup([[deleteButton]]) if msg.chat.type != 'private' else None
        )
        return


    SpamWatch = sw.check(userInfo['id'])
    CAS = cas.check(userInfo['id'])
    SpamProtection = sp.check(userInfo['id'])
    NoSpamPlus = nsp.check(userInfo['id'])
    SpamBlockers = sb.check(userInfo['id'])
    OwlAntiSpam = owl.check(userInfo['id'])


    BUTTONS = []

    banList = [
        SpamWatch['is_Banned'] if SpamWatch['success'] else None,
        CAS['is_Banned'] if CAS['success'] else None,
        SpamProtection['is_Banned'] if SpamProtection['success'] else None,
        NoSpamPlus['is_Banned'] if NoSpamPlus['success'] else None,
        SpamBlockers['is_Banned'] if NoSpamPlus['success'] else None,
        OwlAntiSpam['is_Banned'] if OwlAntiSpam['success'] else None,
    ]

    #moreinfo button
    if any(banList): BUTTONS.append([InlineKeyboardButton("Detailed Ban Info", callback_data=(f"advcheck_{usr.id}_{userInfo['id']}"))])
    
    #delete button
    BUTTONS.append([deleteButton]) if msg.chat.type != 'private' else None

    message.edit_text(text=("""

👤 Name: <a href="tg://user?id={userid}">{firstname} {lastname}</a>
📛 Username: @{username}
🆔 ID: <code>{userid}</code>

🦅 SpamWatch Banned: <code>{SW}</code>
🤖 CAS Banned: <code>{CAS}</code>
✉ Spam Protection Blacklisted: <code>{SPB}</code>
⛔ Potential Spammer (By Spam Protection): <code>{SP}</code>
➕ NoSpamPlus Banned: <code>{NSP}</code>
🐞 SpamBlockers Banned: <code>{SB}</code>
🦉 OwlAntiSpam Banned: <code>{OWL}</code>

✅ Username/id check initiated by <a href="tg://user?id={initid}">{initfirstname}</a>
""").format(
        firstname = html.escape("" if userInfo['firstname'] == None else userInfo['firstname']),
        lastname = html.escape("" if userInfo['lastname'] == None else userInfo['lastname']),
        username = html.escape("" if userInfo['username'] == None else userInfo['username']),
        userid = userInfo['id'],
        initid = usr.id,
        initfirstname = html.escape(usr.first_name),
        SW = SpamWatch['is_Banned'] if SpamWatch['success'] else "error",
        CAS = CAS['is_Banned'] if CAS['success'] else "error",
        SPB = SpamProtection['is_Banned'] if SpamProtection['success'] else "error",
        SP = SpamProtection['is_Potential'] if SpamProtection['success'] else "error",
        NSP = NoSpamPlus['is_Banned'] if NoSpamPlus['success'] else 'error',
        SB = SpamBlockers['is_Banned'] if NoSpamPlus['success'] else 'error',
        OWL = OwlAntiSpam['is_Banned'] if OwlAntiSpam['success'] else 'error',

    ), parse_mode="HTML", reply_markup=InlineKeyboardMarkup(BUTTONS))


__handlers__ = [
    [CommandHandler("check", check_id, filters= ~Filters.reply, pass_args=True, run_async=True)],
]
