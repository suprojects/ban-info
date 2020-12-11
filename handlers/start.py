from telegram.ext import CommandHandler, Filters

from SW import SpamWatchCheck
from CAS import CASCheck
from SpamProtection import SpamProtectionCheck
from AntispamInc import AntispamIncCheck
def start_pvt(update, context):

    try:
        userid = update.message.reply_to_message.from_user.id
        
        update.message.reply_text(text=("""
User's name: {name}
User's id: {id}

Ban info:
SpamWatch Banned: {SW}
CAS Banned: {CAS}
Spam Protection Banned: {SPB}
AntiSpamInc Banned: {ASI}
""").format(name = update.message.reply_to_message.from_user.first_name, id = userid, SW = str(SpamWatchCheck(userid)), CAS = str(CASCheck(userid)), SPB = str(SpamProtectionCheck(userid)), ASI = str(AntispamIncCheck(userid)))

        )

    except:
        update.message.reply_text("You need to reply to a user's message!")

__handlers__ = [[CommandHandler("start", start_pvt, Filters.chat_type.supergroup)]]