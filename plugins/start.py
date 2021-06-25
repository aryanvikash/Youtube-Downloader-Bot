from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/joinchat/4WcL94IzXzswZGNl")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/joinchat/4WcL94IzXzswZGNl")]
    ])
    welcomed = f"WELCOME <b>{message.from_user.first_name}</b>\nWELCOME 🙏 TO OUR PEARL YT DOWNLOADER BOT SERVICE 🤍🤍

ඔබට අවශ්‍ය ඕනෑම යූටියුබ් වීඩියෝවක් මෙම බොට් සේවාව මගින් ලබා ගත හැක.

ඔබ කල යුත්තේ ඔබට අවශ්‍ය යූටියුබ් වීඩියෝවේ ලින්කුව අප බොට් සේවාවට සෙන්ඩ් කිරීම පමනයි.

එවිත් ඔබට එහි QUALITY එක තෝරා ඩව්න්ලෝඩ් කර ගත හැක. 🙏🤍

ස්තූතී.🤍🙏

/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
