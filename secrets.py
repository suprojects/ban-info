from telegram.ext import Filters

try:
    from config import *

except ImportError:
    pass

from os import environ
SPAMWATCH_TOKEN = environ.get("SPAMWATCH_TOKEN")
NOSPAMPLUS_TOKEN = environ.get("NOSPAMPLUS_TOKEN")
BOT_TOKEN = environ.get("BOT_TOKEN")
SUDO_USERS = list(map(int, environ.get("SUDO_USERS").split()))
LOG_CHAT = environ.get("LOG_CHAT")
OWLANTISPAM_TOKEN = environ.get("OWLANTISPAM_TOKEN")
URI = environ.get("URI")

SUDO_ONLY = Filters.user(SUDO_USERS)
