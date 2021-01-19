import os

if os.path.exists('tokens.py'):

    from tokens import *

    os.environ['SPAMWATCH'] = SPAMWATCH
    os.environ['NOSPAMPLUS'] = NOSPAMPLUS
    os.environ['BOT_TOKEN'] = BOT_TOKEN
    os.environ['SUDO_USERS'] = SUDO_USERS
    os.environ['LOG_ID'] = LOG_ID
    os.environ['OWLANTISPAM'] = OWLANTISPAM


SPAMWATCH_TOKEN = os.environ.get("SPAMWATCH")
NOSPAMPLUS_TOKEN = os.environ.get("NOSPAMPLUS")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
SUDO_USERS = list(os.environ.get("SUDO_USERS"))
LOG_CHAT = os.environ.get("LOG_ID")
OWLANTISPAM_TOKEN = os.environ.get("OWLANTISPAM")
