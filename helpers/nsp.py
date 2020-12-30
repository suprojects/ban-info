from nospamplus import Connect
from secrets import NOSPAMPLUS_TOKEN

client = Connect(NOSPAMPLUS_TOKEN)


def check(userid):
    results = {}
    userid = int(userid)

    userinfo = client.is_banned(userid)

    if userinfo:

        results.update(
            {
                "is_Banned": userinfo.banned,
                "reason": userinfo.reason
            }
        )
        return results

    else:
        return results
