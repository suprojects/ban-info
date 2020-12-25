from telegram import MessageEntity
from telegram.ext import CallbackQueryHandler
from telegram.utils import helpers

def delete(update, context):
    query, user, chat = update.callback_query, update.effective_user, update.effective_chat

    if user.id == query.message.reply_to_message.from_user.id or chat.get_member(user.id).status in ("creator", "administrator"):
        query.message.delete()
    
    else:
        query.answer("You did not prompt this check ✋!", show_alert = True)


def advinfo(update, context):

    update.callback_query.answer("Coming Soon!", show_alert = True)

__handlers__ = [
    [CallbackQueryHandler(callback = delete, pattern = 'delete', run_async = True)],
    [CallbackQueryHandler(callback = advinfo, pattern = 'advinfo', run_async= True)]
]