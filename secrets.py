import os

SPAMWATCH_TOKEN = "wedfrtgyh"
ANTISPAMINC_TOKEN = "edrftgyh"
BOT_TOKEN = "edfrgbh"
SUDO_USERS = []
LOG_ID = 123456

if os.environ.get("ENV"):
  SPAMWATCH_TOKEN = os.environ.get('SPAMWATCH')
  ANTISPAMINC_TOKEN = os.environ.get('ANTISPAMINC')
  BOT_TOKEN = os.environ.get('BOT_TOKEN')
  SUDO_USERS = os.environ.get('SUDO_USERS').split()
  LOG_ID = os.environ.get('LOG_ID')
