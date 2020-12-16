import requests
from datetime import datetime

def check(id):

    id = int(id)
    userinfo = requests.get(("https://api.cas.chat/check?user_id={userid}").format(userid=id)).json()

    results = {}

    if userinfo['ok']:
        
        BanDate = userinfo['result']['time_added']
        BanDate = datetime.fromisoformat(BanDate.rstrip(BanDate[-1]))

        results.update({'is_Banned': userinfo['ok'], 'offences': userinfo['result']['offenses'], 'date': BanDate, 'link': ('https://cas.chat/query?u={id}').format(id = id)})   
        
        return results

    else:
        return results