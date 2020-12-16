import requests

def check(id):

    userinfo = requests.get(("https://api.intellivoid.net/spamprotection/v1/lookup?query={userid}").format(userid=id)).json()

    results = {}

    if userinfo['success']:

        attributes = userinfo['results']['attributes']

        results.update({'success': userinfo['success'], 'is_Banned': attributes['is_blacklisted'], 'reason': attributes['blacklist_reason'], 'is_Potential': attributes['is_potential_spammer']})

        return results

    else:
        return results