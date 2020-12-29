from antispaminc import Connect
from secrets import ANTISPAMINC_TOKEN

client = Connect(ANTISPAMINC_TOKEN)


def check(id):
    results = {}

    try:
        userinfo = client.is_banned(id)

        if userinfo:

            results.update(
                {
                    "is_Banned": userinfo.banned,
                    "reason": userinfo.reason
                }
            )
            return results

        else:
            return results
    except:
        results.update(
            {
                "is_Banned": "error"
            }
        )
        return results
