import os


SPAMWATCH_TOKEN = os.environ.get("SPAMWATCH")
NOSPAMPLUS_TOKEN = os.environ.get("NOSPAMPLUS")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
SUDO_USERS = int(os.environ.get("SUDO_USERS"))
LOG_CHAT = os.environ.get("LOG_ID")