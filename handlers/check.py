from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, Filters, CallbackQueryHandler
from apis import nsp, cas, sp, sw, sb, owl
from apis import advinfo
from html import escape
from re import search


def check(update, context):
    usr, msg = update.message.from_user, update.message
    userinfo = msg.reply_to_message.from_user

    message = msg.reply_text("🔄")

    SpamWatch = sw.check(userinfo.id)
    CAS = cas.check(userinfo.id)
    SpamProtection = sp.check(userinfo.id)
    NoSpamPlus = nsp.check(userinfo.id)
    SpamBlockers = sb.check(userinfo.id)
    OwlAntiSpam = owl.check(userinfo.id)

    delete_button = InlineKeyboardButton("OK", callback_data=(
        "delete_{userid}").format(userid=update.message.from_user.id))
    more_info = InlineKeyboardButton("Detailed Ban Info", callback_data=(
        f"advcheck_{usr.id}_{userinfo.id}"))

    buttons = InlineKeyboardMarkup(
        [
            [more_info],
            [delete_button],
        ]
    )

    message.edit_text(text=("""

👤 Name: <a href="tg://user?id={id}">{firstname} {lastname}</a>
📛 Username: @{username}
🆔 ID: <code>{id}</code>

🦅 SpamWatch Banned: <code>{SW}</code>
🤖 CAS Banned: <code>{CAS}</code>
✉ Spam Protection Blacklisted: <code>{SPB}</code>
⛔ Potential Spammer (By Spam Protection): <code>{SP}</code>
➕ NoSpamPlus Banned: <code>{NSP}</code>
🐞 SpamBlockers Banned: <code>{SB}</code>
🦉 OwlAntiSpam Banned: <code>{OWL}</code>

✅ Initiated by <a href="tg://user?id={initid}">{initfirstname}</a>
""").format(
        firstname = escape("" if userinfo.first_name == None else userinfo.first_name),
        lastname = escape("" if userinfo.last_name == None else userinfo.last_name),
        username = escape("" if userinfo.username == None else userinfo.username),
        id = userinfo.id,
        initid = usr.id,
        initfirstname = escape(usr.first_name),
        SW = SpamWatch['is_Banned'] if SpamWatch['success'] else "error",
        CAS = CAS['is_Banned'] if CAS['success'] else "error",
        SPB = SpamProtection['is_Banned'] if SpamProtection['success'] else "error",
        SP = SpamProtection['is_Potential'] if SpamProtection['success'] else "error",
        NSP = NoSpamPlus['is_Banned'] if NoSpamPlus['success'] else 'error',
        SB = SpamBlockers['is_Banned'] if NoSpamPlus['success'] else 'error',
        OWL = OwlAntiSpam['is_Banned'] if OwlAntiSpam['success'] else 'error',

    ), parse_mode="HTML", reply_markup=buttons)


def no_reply(update, context):
    delete_button = InlineKeyboardButton("OK", callback_data=(
        "delete_{userid}").format(userid=update.message.from_user.id))
    update.message.reply_text("Reply to a user's message to get the info",
                              reply_markup=InlineKeyboardMarkup([[delete_button]]))


def check_callback(update, context):

    qry = update.callback_query
    attr = qry.data.split('_')
    userid = int(attr[2])

    if int(qry.from_user.id) != int(attr[1]):
        qry.answer('You did not prompt this check ✋', show_alert = True)
        return
    
    qry.edit_message_text('🔄')
    qry.answer()


#Check if the user clicks the button

    text = str()

#Add basic details

    text += f"{qry.message.text.splitlines()[0]}\n{qry.message.text.splitlines()[1]}\n{qry.message.text.splitlines()[2]}\n\n{advinfo.check(userid)}"

    BUTTONS = [[InlineKeyboardButton("OK", callback_data=(f"delete_{attr[1]}"))]]

    qry.edit_message_text(text, parse_mode = 'HTML', reply_markup = InlineKeyboardMarkup(BUTTONS), disable_web_page_preview = True)


def advcheck_error(update, context):
    update.callback_query.answer(text = 'In maintenance ⚠', show_alert = True)

__handlers__ = [
    [CommandHandler("check", check, filters=Filters.chat_type.groups & Filters.reply, run_async=True)],
    [CommandHandler("check", no_reply, filters=Filters.chat_type.groups & ~Filters.reply, run_async=True)],
    [CallbackQueryHandler(pattern="^advcheck_", callback = check_callback, run_async=True)],
]
