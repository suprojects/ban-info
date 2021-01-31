import requests

def check(userid):

    try: 
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
                    "is_Potential": attributes["is_potential_spammer"],
                    "link": ("https://t.me/SpamProtectionBot?start=00_{userid}").format(userid = userid)
                }
            )

        else:
            results.update({
                'success': True,
                "is_Banned": False,
                "is_Potential": False,
                })

        return results

    except:
        return {'success': False}