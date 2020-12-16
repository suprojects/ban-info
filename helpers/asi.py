from antispaminc import Connect
from secrets import ANTISPAMINC_TOKEN

client = Connect(ANTISPAMINC_TOKEN)


def check(id):
    userinfo = client.is_banned(id)

    results = {}

    if userinfo:

        results.update({'is_Banned': userinfo.banned, 'reason': userinfo.reason})
        return results

    else:
        return results