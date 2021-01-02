import spamwatch
from secrets import SPAMWATCH_TOKEN

client = spamwatch.Client(SPAMWATCH_TOKEN)


def check(userid):
    userid = int(userid)
    results = {}

    userinfo = client.get_ban(userid)

    if userinfo:
        results.update({
            "id": userinfo.id,
            "is_Banned": True,
            "date": userinfo.date,
            "reason": userinfo.reason,
            "admin": userinfo.admin,
            "message": userinfo.message
        })

    else:
        pass

    return results
