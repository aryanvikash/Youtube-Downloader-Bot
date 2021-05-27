from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Our Channel🛰", url="https://t.me/BoburjonVlogs")],
        [InlineKeyboardButton(
            "Owner of the Bot👨‍💻", url="https://t.me/Boburjon_Ravzatov")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n If you want learn /help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
