import requests


def check(id):

    banned = requests.get(
        (
            "https://api.intellivoid.net/spamprotection/v1/lookup?query={userid}"
        ).format(
            userid=id
        )
    ).json()

    if banned["success"] == True:
        return(banned["results"]["attributes"]["is_blacklisted"])

    elif banned["success"] == False:
        return ("404: User not seen before")
