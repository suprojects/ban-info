import sw, sp, cas, asi

def advcheck(userid):
    userid = int(userid)
    results = {}

    #SpamWatch
    SpamWatch = sw.check(userid)

    if SpamWatch.get("is_Banned", False):
        SpamWatchResults = ("🦅 SpamWatch Banned: <code>{banned}</code>\n- 📅 Date of ban (UTC): <code{date}></code>\n- 💬 Reason: <code>{reason}</code>\n\n").format(banned = SpamWatch.get("is_Banned", False), date = SpamWatch['date'], reason = SpamWatch['reason'])
        results.update({'SpamWatch': SpamWatchResults})

    else:
        SpamWatchResults = ("🦅 SpamWatch Banned: <code>{banned}</code>\n\n").format(banned = SpamWatch.get("is_Banned", False))
        results.update({'SpamWatch': SpamWatchResults})

    
    #CAS
    CAS = cas.check(userid)

    if CAS.get("is_Banned", False):
        CASResults = ("🤖 CAS Banned: <code>{banned}</code>\n- 📅 Date of ban: <code>{date}</code>\n- 🔢 Number of offences: <code>{offences}</code>\n- 🔗 More Info: {link}\n\n").format(banned = CAS.get('is_Banned', False), date = CAS['date'], offences = CAS['offences'], link = CAS['link'])
        results.update({'CAS': CASResults})

    else:
        CASResults = ("🤖 CAS Banned: <code>{banned}</code>\n\n").format(banned = CAS.get("is_Banned", False))
        results.update({'CAS': CASResults})


    #SpamProtection
    SpamProtection = sp.check(userid)

    if SpamProtection['success']:
        SpamProtectionResults = ("✉ Spam Protection Banned: <code>{banned}</code>\n- ⚠ Potential Spammer: <code>{potential}</code>\n").format(banned = SpamProtection['is_Banned'], potential = SpamProtection['is_potential'], reason = SpamProtection['reason'], link = SpamProtection['link'])
        
        if SpamProtection['is_Banned']:
            SpamProtectionResults = SpamProtectionResults + ("- 💬 Reason: <code>{reason}</code>\n- 🔗 More Info: <a href='{link}'>Click here 🔘</a>\n\n").format(reason = SpamProtection['reason'], link = SpamProtection['link'])
        
        else:
            SpamProtectionResults = SpamProtectionResults + ("- 🔗 More Info: <a href='{link}'>Click here 🔘</a>\n\n").format(link = SpamProtection['link'])
        
        results.update({'SpamProtection': SpamProtectionResults})

    else:
        SpamProtectionResults = ("✉ Spam Protection Banned: <code>User not found in Records</code>\n\n")
        results.update({'SpamProtection': SpamProtectionResults})


    #AntiSpamInc
    AntiSpamInc = asi.check(userid)

    if AntiSpamInc.get("is_Banned", False):
        AntiSpamIncResults = ("⚡ AntiSpamInc Banned: <code>{banned}</code>\n- 💬 Reason: <code>{reason}</code>\n\n").format(banned = AntiSpamInc.get("is_Banned", False), reason = AntiSpamInc['reason'])
        results.update({'AntiSpamInc': AntiSpamIncResults})

    else:
        AntiSpamIncResults = ("⚡ AntiSpamInc Banned: <code>{banned}</code>\n\n").format(banned = AntiSpamInc.get("is_Banned", False))

    return results