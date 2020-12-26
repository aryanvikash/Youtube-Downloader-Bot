from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"حاليااا مندعم تنزيل بس الفيدوهات المفردة بدقااات متنوعة مع دعم تنزيل كموسيقى وبدووون أي حدود للحجم او الاستخدام المتكرر كباقي البوتات الزفت 🐰🐰حاليا مامندعم تنزيل قوائم يوتيوب 😌😌 لاتعذبنا 😒 Programming and development: @Mr00lucifer"
    await message.reply_text(helptxt)
