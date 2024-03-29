import requests
from datetime import datetime

def check(userid):

    try:
        userid = int(userid)
        results = {}

        userinfo = requests.get("https://api.cas.chat/check?user_id={}".format(userid)).json()

        if userinfo["ok"]:
            BanDate = userinfo["result"]["time_added"]
            BanDate = datetime.fromisoformat(BanDate.rstrip(BanDate[-1]))

            results.update({
                "success": True,
                "is_Banned": userinfo["ok"],
                "offences": userinfo["result"]["offenses"],
                "date": BanDate,
                "link": f"https://cas.chat/query?u={userid}"
                })

        else:
            results.update({
                "success": True,
                "is_Banned": False,
            })

        return results
    
    except:
        return {'success': False}
