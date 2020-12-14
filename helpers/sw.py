import spamwatch
#from secrets import SPAMWATCH_TOKEN

SPAMWATCH_TOKEN = '5p3uhBoURYnZVyAa5mzt7EOCRIOhwcTOFeU7NCqfLND8S6N3RCAF~kRJlJ2wVMhR'

client = spamwatch.Client(SPAMWATCH_TOKEN)


def check(id):

    id = int(id)
    baninfo = client.get_ban(id)

    results = {}
    
    if baninfo == False:
        
        results.update({'isBanned': False})
        return results

    elif int(baninfo.id) == id:
        
        results.update({'id': baninfo.id, 'isBanned' : True, 'date' : baninfo.date, 'reason' : baninfo.reason, 'admin' : baninfo.admin, 'message' : baninfo.message})
        return results
        
a = check('1250235607')