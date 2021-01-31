import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def check(userid):
    try:
        userid = int(userid)
        results = {}

        userinfo = requests.get(
            "https://sb.lungers.com:9613/user/{}".format(userid), verify=False).json()

        if userinfo["user"]:
            info = userinfo["user"]
            results.update({
                "success": True,
                "is_Banned": True,
                "admin_id": info["admin_id"],
                "reason": info["reason"]})

        else:
            results.update({
                'success': True,
                "is_Banned": False
                })

        return results
    
    except:
        return {'success': False}
