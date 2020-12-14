import spamwatch
from secrets import SPAMWATCH_TOKEN

client = spamwatch.Client(SPAMWATCH_TOKEN)


def check(id):
    banned = client.get_ban(id)

    if banned == False:
        return False
    else:
        return True
