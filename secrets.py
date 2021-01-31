
from telegram.ext import Filters

try:
    from config import *
except ImportError:
    from os import environ
    SPAMWATCH_TOKEN = environ.get("SPAMWATCH")
    NOSPAMPLUS_TOKEN = environ.get("NOSPAMPLUS")
    BOT_TOKEN = environ.get("BOT_TOKEN")
    SUDO_USERS = list(map(int, environ.get("SUDO_USERS").split()))
    LOG_CHAT = environ.get("LOG_ID")
    OWLANTISPAM_TOKEN = environ.get("OWLANTISPAM")
    URI = environ.get("URI")

SUDO_ONLY = Filters.user(SUDO_USERS)
