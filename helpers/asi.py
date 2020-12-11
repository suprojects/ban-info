from antispaminc import Connect
from secrets import ANTISPAMINC_TOKEN

client = Connect(ANTISPAMINC_TOKEN)


def check(id):
    banned = client.is_banned(id)

    if banned == None:
        return False

    elif AntispamIncBanned.banned == True:
        return True
