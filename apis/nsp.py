from nospamplus import Connect
from secrets import NOSPAMPLUS_TOKEN

#client = Connect(NOSPAMPLUS_TOKEN)
client = None


def check(userid):

    try:
        results = {}
        userid = int(userid)

        userinfo = client.is_banned(userid)

        if userinfo:

            results.update({
                "success": True,
                "is_Banned": userinfo.banned,
                "reason": userinfo.reason
                })

        else:
            results.update({
                "success": True,
                "is_Banned": False
            })

        return results

    except:
        return {'success': False}
