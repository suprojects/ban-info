from nospamplus import Connect
from secrets import NOSPAMPLUS_TOKEN

client = Connect(NOSPAMPLUS_TOKEN)


def check(userid):

    try:
        results = {}
        userid = int(userid)

        userinfo = client.is_banned(userid)

        if userinfo:

            results.update({
                    "is_Banned": userinfo.banned,
                    "reason": userinfo.reason
                })

        else:
            pass

        return results

    except:
        return {'is_Banned': 'Error'}