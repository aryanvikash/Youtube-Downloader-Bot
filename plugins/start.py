from pyrogram import Client, filters,StopPropagation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup



@Client.on_message(filters.command(["start"])& filters.private)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/aryan_bots")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/aryanvikash")]
    ])
    welcomed = f"Hello <b>{message.from_user.first_name}</b>\nFor more information use /help"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
