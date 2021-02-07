from apis import sw, sp, cas, nsp, sb, owl


def check(userid):
    userid = int(userid)
    text = str()

#SpamWatch

    SpamWatch = sw.check(userid)

    if SpamWatch['success']:
        text += f"🦅 SpamWatch Banned: <code>{SpamWatch['is_Banned']}</code>"

        if SpamWatch['is_Banned']:
            text += f"""

- 📅 Date: {SpamWatch['date']}</code>
- 💬 Reason: <code>{SpamWatch['reason']}</code>
"""
        text += "\n"

    else: text += "🦅 SpamWatch Banned: <code>error</code>\n"


#CAS
    CAS = cas.check(userid)

    if CAS['success']:
        text += f"🤖 CAS Banned: <code>{CAS['is_Banned']}</code>"

        if CAS['is_Banned']:
            text += f"""

- 📅 Date: {CAS['date']}</code>
- 🔢 Number of Offences: <code>{CAS['offences']}</code>
- 🔗 More info: <a href="{CAS['link']}">link</a>
"""

        text += "\n"
    else: text += "🤖 CAS Banned: <code>error</code>\n"


#SpamProtection
    SpamProtection = sp.check(userid)

    if SpamProtection['success']:
        text += f"✉ SpamProtection Banned: <code>{SpamProtection['is_Banned']}</code>"

        if SpamProtection['is_Banned']:
            text += f"""
- 💬 Reason: <code>{SpamProtection['reason']}</code>
- 🔗 More info: <a href="{SpamProtection['link']}">link</a>
"""
        text += "\n"
        text += f"⚠ Potential Spammer: <code>{SpamProtection['is_Potential']}</code>\n"

    else: text += "✉ SpamProtection Banned: <code>error</code>\n"


#NoSpamPlus
    NoSpamPlus = nsp.check(userid)

    if NoSpamPlus['success']:
        text += f"➕ NoSpamPlus Banned: <code>{NoSpamPlus['is_Banned']}</code>"

        if NoSpamPlus['is_Banned']:
            text += f"""
- 💬 Reason: {NoSpamPlus['date']}</code>
"""
        text += "\n"

    else: text += "➕ NoSpamPlus Banned: <code>error</code>\n"


#SpamBlockers
    SpamBlockers = sb.check(userid)
    
    if SpamBlockers['success']:
        text += f"🐞 SpamBlockers Banned: <code>{SpamBlockers['is_Banned']}</code>"

        if SpamBlockers['is_Banned']:
            text += f"""
- 💬 Reason: <code>{SpamBlockers['reason']}</code>
"""
        text += "\n"

    else: text += "🐞 SpamBlockers Banned: <code>error</code>\n"


#OwlAntiSpam
    OwlAntiSpam = owl.check(userid)

    if OwlAntiSpam['success']:
        text += f"🦉 OwlAntiSpam Banned: <code>{OwlAntiSpam['is_Banned']}</code>"

        if OwlAntiSpam['is_Banned']:
            text += f"""
- 📅 Date: {OwlAntiSpam['date']}</code>
- 💬 Reason: <code>{OwlAntiSpam['reason']}</code>
"""
        text += "\n"

    else: text += "🦉 OwlAntiSpam Banned: <code>error</code>\n"

    return text
