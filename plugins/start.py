from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Bizning kanal", url="https://t.me/technoliteuz")],
        [InlineKeyboardButton(
            "Murojaat uchun", url="https://t.me/technoliteuz")]
    ])
    welcomed = f"Salom <b>{message.from_user.first_name}</b>\n/help yordam kerak bo'lsa shu buyruqni bosing"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
