from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("කණ්ඩායම් සම්බන්ධකය ❤️❤️", url="https://t.me/joinchat/BI1Arw6rgAQ2NGZl")],
        [InlineKeyboardButton(
            "දෝෂයක් නම් කියන්න 😁", url="https://t.me/Ishanstudio")]
    ])
    welcomed = f"අඩෝ <b>{message.from_user.first_name}</b>\n/ඔබට උදව්වක් අවශ්‍ය නම්"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
