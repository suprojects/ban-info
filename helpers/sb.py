import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def check(userid):
    userid = int(userid)
    results = {}

    userinfo = requests.get(
        "https://sb.lungers.com:9613/user/{}".format(userid), verify=False).json()

    if userinfo["user"]:
        info = userinfo["user"]
        results.update(
            {"is_Banned": True, "admin_id": info["admin_id"], "reason": info["reason"]})

    else:
        pass

    return results
