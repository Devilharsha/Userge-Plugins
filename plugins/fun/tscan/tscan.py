from . import *

@ultroid_cmd(pattern="tscan ?(.*)")
async def tscan(e):
    mat = e.pattern_match.group(1)
    if e.is_reply and not mat:
        re = await e.get_reply_message()
        mat = re.sender_id
    if not mat:
        return await eor(e, "Give me Something to look for.")
    chat = "@tgscanrobot"
    async with e.client.conversation(chat) as bot:
        await bot.send_message(str(mat))
        a = await bot.get_response()
    await eor(e, a.message)
    await ultroid_bot.send_read_acknowledge(chat)

HELP.update({"tscan":"tscan - Get The channel/groups user in."})