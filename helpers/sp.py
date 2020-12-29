import requests


def check(userid):
    userid = int(userid)
    results = {}

    userinfo = requests.get("https://api.intellivoid.net/spamprotection/v1/lookup?query={}".format(userid)).json()

    if userinfo["success"]:

        attributes = userinfo["results"]["attributes"]
        results.update(
            {
                "success": userinfo["success"],
                "is_Banned": attributes["is_blacklisted"],
                "reason": attributes["blacklist_reason"],
                "is_Potential": attributes["userid"],
                "link": ("https://t.me/SpamProtectionBot?start=00_{userid}").format(userid = userid)
            }
        )

        return results

    else:
        return results
