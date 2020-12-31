from helpers import sw, sp, cas, nsp

def check_small(userid):
    userid = int(userid)
    results = {}

    #SpamWatch
    SpamWatch = sw.check(userid)

    if SpamWatch.get("is_Banned", False):
        SpamWatchResults = ("🦅 SpamWatch Banned: {banned}\n- 📅 Date of ban (UTC): <code{date}>\n- 💬 Reason: {reason}").format(banned = SpamWatch.get("is_Banned", False), date = SpamWatch['date'], reason = SpamWatch['reason'])
        results.update({'SpamWatch': SpamWatchResults})

    else:
        SpamWatchResults = ("🦅 SpamWatch Banned: {banned}").format(banned = SpamWatch.get("is_Banned", False))
        results.update({'SpamWatch': SpamWatchResults})

    
    #CAS
    CAS = cas.check(userid)

    if CAS.get("is_Banned", False):
        CASResults = ("🤖 CAS Banned: {banned}\n- 📅 Date of ban: {date}\n- 🔢 Number of offences: {offences}").format(banned = CAS.get('is_Banned', False), date = CAS['date'], offences = CAS['offences'])
        results.update({'CAS': CASResults})

    else:
        CASResults = ("🤖 CAS Banned: {banned}").format(banned = CAS.get("is_Banned", False))
        results.update({'CAS': CASResults})


    #SpamProtection
    SpamProtection = sp.check(userid)

    if SpamProtection['success']:
        SpamProtectionResults = ("✉ Spam Protection Banned: {banned}\n⚠ Potential Spammer: {potential}").format(banned = SpamProtection['is_Banned'], potential = SpamProtection['is_Potential'], reason = SpamProtection['reason'])
        
        if SpamProtection['is_Banned']:
            SpamProtectionResults = SpamProtectionResults + ("- 💬 Reason: {reason}").format(reason = SpamProtection['reason'])
            
        results.update({'SpamProtection': SpamProtectionResults})

    else:
        SpamProtectionResults = ("✉ Spam Protection Banned: User not found in Records")
        results.update({'SpamProtection': SpamProtectionResults})


    #NoSpamPlus
    NoSpamPlus = nsp.check(userid)

    if NoSpamPlus.get("is_Banned", False):
        NoSpamPlusResults = ("➕ NoSpam+ Banned: {banned}\n- 💬 Reason: {reason}").format(banned = NoSpamPlus.get("is_Banned", False), reason = NoSpamPlus['reason'])
        results.update({'NoSpamPlus': NoSpamPlusResults})

    else:
        NoSpamPlusResults = ("➕ NoSpam+ Banned: {banned}").format(banned = NoSpamPlus.get("is_Banned", False))
        results.update({'NoSpamPlus': NoSpamPlusResults})

    return results


def check(userid):
    userid = int(userid)
    results = {}

    #SpamWatch
    SpamWatch = sw.check(userid)

    if SpamWatch.get("is_Banned", False):
        SpamWatchResults = ("🦅 SpamWatch Banned: <code>{banned}</code>\n- 📅 Date of ban (UTC): <code{date}></code>\n- 💬 Reason: <code>{reason}</code>\n").format(banned = SpamWatch.get("is_Banned", False), date = SpamWatch['date'], reason = SpamWatch['reason'])
        results.update({'SpamWatch': SpamWatchResults})

    else:
        SpamWatchResults = ("🦅 SpamWatch Banned: <code>{banned}</code>").format(banned = SpamWatch.get("is_Banned", False))
        results.update({'SpamWatch': SpamWatchResults})

    
    #CAS
    CAS = cas.check(userid)

    if CAS.get("is_Banned", False):
        CASResults = ("🤖 CAS Banned: <code>{banned}</code>\n- 📅 Date of ban: <code>{date}</code>\n- 🔢 Number of offences: <code>{offences}</code>\n- 🔗 More Info: {link}\n").format(banned = CAS.get('is_Banned', False), date = CAS['date'], offences = CAS['offences'], link = CAS['link'])
        results.update({'CAS': CASResults})

    else:
        CASResults = ("🤖 CAS Banned: <code>{banned}</code>").format(banned = CAS.get("is_Banned", False))
        results.update({'CAS': CASResults})


    #SpamProtection
    SpamProtection = sp.check(userid)

    if SpamProtection['success']:
        SpamProtectionResults = ("✉ Spam Protection Banned: <code>{banned}</code>\n- ⚠ Potential Spammer: <code>{potential}</code>\n").format(banned = SpamProtection['is_Banned'], potential = SpamProtection['is_Potential'], reason = SpamProtection['reason'], link = SpamProtection['link'])
        
        if SpamProtection['is_Banned']:
            SpamProtectionResults = SpamProtectionResults + ("- 💬 Reason: <code>{reason}</code>\n- 🔗 More Info: <a href='{link}'>Click here 🔘</a>\n").format(reason = SpamProtection['reason'], link = SpamProtection['link'])
        
        else:
            SpamProtectionResults = SpamProtectionResults + ("- 🔗 More Info: <a href='{link}'>Click here 🔘</a>\n").format(link = SpamProtection['link'])
        
        results.update({'SpamProtection': SpamProtectionResults})

    else:
        SpamProtectionResults = ("✉ Spam Protection Banned: <code>User not found in Records</code>")
        results.update({'SpamProtection': SpamProtectionResults})


    #NoSpamPlus
    NoSpamPlus = nsp.check(userid)

    if NoSpamPlus.get("is_Banned", False):
        NoSpamPlusResults = ("➕ NoSpam+ Banned: <code>{banned}</code>\n- 💬 Reason: <code>{reason}</code>\n").format(banned = NoSpamPlus.get("is_Banned", False), reason = NoSpamPlus['reason'])
        results.update({'NoSpamPlus': NoSpamPlusResults})

    else:
        NoSpamPlusResults = ("➕ NoSpam+ Banned: <code>{banned}</code>").format(banned = NoSpamPlus.get("is_Banned", False))
        results.update({'NoSpamPlus': NoSpamPlusResults})
    return results