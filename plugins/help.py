from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"යූටියුබ් ලින්ක් එක එවන්න​"
    await message.reply_text(helptxt)
