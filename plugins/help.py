from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"just send me the YouTube video link🔗"
    await message.reply_text(helptxt)
