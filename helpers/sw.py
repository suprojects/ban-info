import spamwatch
#from secrets import SPAMWATCH_TOKEN

SPAMWATCH_TOKEN = '5p3uhBoURYnZVyAa5mzt7EOCRIOhwcTOFeU7NCqfLND8S6N3RCAF~kRJlJ2wVMhR'

client = spamwatch.Client(SPAMWATCH_TOKEN)


def check(id):

    id = int(id)
    userinfo = client.get_ban(id)

    results = {}

    if userinfo:

        results.update({'id' : userinfo.id, 'is_Banned' : True, 'date' : userinfo.date, 'reason' : userinfo.reason, 'admin' : userinfo.admin, 'message' : userinfo.message})
        return results

    else:
        return results