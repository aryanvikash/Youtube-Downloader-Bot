from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"حاليااا مندعم بس الفيدوهات المفردة بدون تنزيل قوائم يوتيوب 😌😌 لاتعذبنا 😒 Programming and development: @Mr00lucifer"
    await message.reply_text(helptxt)
