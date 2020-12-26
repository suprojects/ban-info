import requests

def check(id):

    results = {}

    try:

        userinfo = requests.get(("https://api.intellivoid.net/spamprotection/v1/lookup?query={userid}").format(userid=id)).json()

        if userinfo['success']:

            attributes = userinfo['results']['attributes']
            results.update({'success': userinfo['success'], 'is_Banned': attributes['is_blacklisted'], 'reason': attributes['blacklist_reason'], 'is_Potential': attributes['is_potential_spammer']})

            return results

        else:
            return results
        
    except:
        results.update({'is_Banned': 'error'})
        return results