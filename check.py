from SW import SpamWatchCheck
from CAS import CASCheck
from AntispamInc import AntispamIncCheck
from SpamProtection import SpamProtectionCheck


while True:

    userid = input("Please enter the User ID: ")

    print("SpamWatch Banned: " + str(SpamWatchCheck(userid)))
    print("CAS Banned: " + str(CASCheck(userid)))
    print("AntiSpamInc Banned: " + str(AntispamIncCheck(userid)))
    print("Spam Protection Banned: " + str(SpamProtectionCheck(userid)))