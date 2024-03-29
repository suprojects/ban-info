import owlantispam
from secrets import OWLANTISPAM_TOKEN

try: client = owlantispam.Client(OWLANTISPAM_TOKEN)
except: pass

def check(userid):

    try:
        userid = int(userid)
        results = {}

        userinfo = client.get_ban(userid)

        if userinfo:
            results.update({
                "success": True,
                "id": userinfo.id,
                "is_Banned": True,
                "date": userinfo.date,
                "reason": userinfo.reason,
                "admin": userinfo.admin,
                "message": userinfo.message
            })

        else:
            results.update({
                "success": True,
                "is_Banned": False
            })

        return results

    except:
        return {'success': False}
