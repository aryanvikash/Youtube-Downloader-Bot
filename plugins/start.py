from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🌐 WebSite", url="https://ganiyev.uz")],
        [InlineKeyboardButton(
            "Admin 😊", url="https://t.me/jokkerking")]
    ])
    welcomed = f"Salom <b>{message.from_user.first_name}</b>\nTelegramdagi eng zamonaviy YouTube video va audio yuklovchi botga xush kelibsiz!

Iltimos, har qanday YouTube video havolasini yuboring yoki @vid inline rejimidan foydalanib qidiring."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
