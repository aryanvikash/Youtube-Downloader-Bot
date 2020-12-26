from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🙈صفحة الفيسبوك الخاصة بنا", url="https://www.facebook.com/solu404tion/")],
        [InlineKeyboardButton(
            "حساب المطور للابلاغ عن ثغرة او اقتراح 👨🏻‍💻", url="https://www.facebook.com/mohammedsjnoube")]
    ])
    welcomed = f"مرحبااا ابو عنتر 😒 لي اسمك <b>{message.from_user.first_name}</b>\n/help ضغاط هون كرمال تعرف شو بنشغل😌😌 وهي بوتنا التاني @Sy404_bot"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
