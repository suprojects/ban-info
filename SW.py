import spamwatch
from secrets import SPAMWATCH_TOKEN

SpamWatchClient = spamwatch.Client(SPAMWATCH_TOKEN)

def SpamWatchCheck(id):
    
    SpamWatchBanned = SpamWatchClient.get_ban(id)

    if SpamWatchBanned == False:
        return False

    else:
        return True