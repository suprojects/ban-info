import requests

def SpamProtectionCheck(id):

    SpamProtectionBanned = requests.get(("https://api.intellivoid.net/spamprotection/v1/lookup?query={userid}").format(userid = id)).json()
    
    if SpamProtectionBanned['success'] == True:
        return(SpamProtectionBanned['results']['attributes']['is_blacklisted'])

    elif SpamProtectionBanned['success'] == False:
        return ("404: User not seen before")