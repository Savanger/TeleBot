# Ported from other Telegram UserBots for TeleBot
# Kangers, don't remove this line 
# @its_xditya

from userbot import CMD_LIST
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "TeleBot User"
      
@borg.on(admin_cmd(pattern="help ?(.*)", allow_sudo=True))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    splugin_name = event.pattern_match.group(1)
    if splugin_name in borg._plugins:
        s_help_string = borg._plugins[splugin_name].__doc__
    else:
        s_help_string = ""
    _, check_sgnirts = check_data_base_heal_th()

  help_string = f"""`Userbot Helper for {DEFAULTUSER} to reveal all the commands of `**[TeleBot](https://xditya.gitbook.io/telebot/)**\n\n"""
    borg._iiqsixfourstore[str(event.chat_id)] = {}
    borg._iiqsixfourstore[
        str(event.chat_id)
    ][
        str(event.id)
    ] = help_string + "\n\n" + s_help_string
    tgbotusername = Config.TG_BOT_USER_NAME_BF_HER  # pylint:disable=E0602
    if tgbotusername is not None:
        results = await borg.inline_query(  # pylint:disable=E0602
            tgbotusername,
            f"TeleBot {event.chat_id} {event.id}"
        )
        await results[0].click(
            event.chat_id,
            reply_to=event.reply_to_msg_id,
            hide_via=True
        )
    else:
        await event.reply(
            help_string + "\n\n" + s_help_string,
            parse_mode="html"
        )

    await event.delete()

        
