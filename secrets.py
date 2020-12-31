import os

os.environ['SPAMWATCH'] = 'fUG438ge8iVPrf7SfwFxCPNnY2Q0P2IiaVOhviePNsIo31m8nQwr~gzku5x_7gV0'
os.environ['NOSPAMPLUS'] = 'UQxkLhHV_GEH7JR23SwOhA'
os.environ['BOT_TOKEN'] = '1459172207:AAExAyKQXHBWmFa4Zt9RYlLHwhpSygF9ZYM'
os.environ['SUDO_USERS'] = '1178472788'
os.environ['LOG_ID'] = '-1001146754909'

SPAMWATCH_TOKEN = os.environ.get("SPAMWATCH")
NOSPAMPLUS_TOKEN = os.environ.get("NOSPAMPLUS")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
SUDO_USERS = int(os.environ.get("SUDO_USERS"))
LOG_CHAT = os.environ.get("LOG_ID")