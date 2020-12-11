import requests


def check(id):
    CASBanned = requests.get(
        (
            "https://api.cas.chat/check?user_id={userid}"
        ).format(
            userid=id
        )
    ).json()
    return CASBanned.get('ok')
