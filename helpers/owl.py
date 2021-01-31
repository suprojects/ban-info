import owlantispam
from secrets import OWLANTISPAM_TOKEN

client = owlantispam.Client(OWLANTISPAM_TOKEN)


def check(userid):

    try:
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

    except:
        return {'is_Banned': 'Error'}
