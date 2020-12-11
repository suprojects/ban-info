from antispaminc import Connect
from secrets import ANTISPAMINC_TOKEN

AntispamIncClient = Connect(ANTISPAMINC_TOKEN)

def AntispamIncCheck(id):

    AntispamIncBanned = AntispamIncClient.is_banned(id)

    if AntispamIncBanned == None:
        return False

    elif AntispamIncBanned.banned == True:
        return True