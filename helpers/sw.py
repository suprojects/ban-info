import spamwatch
from secrets import SPAMWATCH_TOKEN

client = spamwatch.Client(SPAMWATCH_TOKEN)


def check(id):
    id = int(id)
    results = {}

    try:
        userinfo = client.get_ban(id)

        if userinfo:
            results.update(
                {"id": userinfo.id,
                 "is_Banned": True,
                 "date": userinfo.date,
                 "reason": userinfo.reason,
                 "admin": userinfo.admin,
                 "message": userinfo.message
                 }
            )
            return results

        else:
            return results

    except:
        results.update(
            {"is_Banned": "error"}
        )
        return results
