from telegram.ext import CommandHandler, Filters

import helpers.asi
import helpers.cas
import helpers.sp
import helpers.sw


def start_pvt(update, context):
    usr, msg = update.effective_user, update.effective_message

    try:
        if msg.reply_to_message:
            msg.reply_text(
                "User ID: {id}\n\n\nBan info:\nSpamWatch Banned: {SW}\nCAS Banned: {CAS}\nSpam Protection Banned: {SPB}\nAntiSpamInc Banned: {ASI}"
                .format(
                    id=usr.id,
                    SW=sw.check(
                        usr.id
                    ),
                    CAS=cas.check(
                        usr.id
                    ),
                    SPB=sp.check(
                        usr.id
                    ),
                    ASI=asi.check(
                        usr.id
                    )
                )
            )
        else:
            msg.reply_text("You need to a message from a user!")
    except:
        msg.reply_text(
            "An unexpected error occured, try telling us about it in @su_BotsChat."
        )


__handlers__ = [
    [
        CommandHandler(
            "start",
            start_pvt,
            Filters.chat_type.supergroup
        )
    ]
]
