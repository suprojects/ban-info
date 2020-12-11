#######################################################################################
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
#######################################################################################

from telegram import Update
from telegram.ext import Updater, CommandHandler, Filters
from secrets import BOT_TOKEN, ANTISPAMINC_TOKEN, SPAMWATCH_TOKEN




'''{'update_id': 87119953, 
'message': {'message_id': 1236, 'date': 1607665124,  
'reply_to_message': {'message_id': 1218, 'date': 1607664968, 'text': 'Going to introduce a new bot?', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 
'from': {'id': 1462830154, 'first_name': 'A.B.Ashwanth', 'is_bot': False, 'last_name': 'Morris', 'username': 'Ashwanth123'}}, 'text': '/start@sudoalphaxbot', 'entities': [{'type': 'bot_command', 'offset': 0, 'length': 20}], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 'from': {'id': 1093541050, 'first_name': '𝙿𝚕𝚞𝚝𝚘𝚗𝚒𝚞𝚖 𝚇²', 'is_bot': False, 'username': 'plutoniumx'}}}
'''
def main():

    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler()

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()