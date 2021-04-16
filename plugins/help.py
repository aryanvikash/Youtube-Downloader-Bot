from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"cukup kirimkan saja link video youtube yang ingin di download"
    await message.reply_text(helptxt)
