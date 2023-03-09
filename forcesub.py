
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import UserNotParticipant

# Replace with your channel username or ID
UPDATES_CHANNEL = "@my_channel_username"

app = Client("my_bot")

@app.on_message(filters.private & ~filters.command("start"))
async def force_sub(bot: Client, message: Message):
    try:
        user = await bot.get_chat_member(chat_id=UPDATES_CHANNEL, user_id=message.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=message.from_user.id,
                text="Sorry, you are banned from using this bot. Contact the bot admin for more info."
            )
            return
        await message.forward(chat_id=UPDATES_CHANNEL)
    except UserNotParticipant:
        invite_link = f"https://t.me/{UPDATES_CHANNEL}"
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f"You must join [this channel]({invite_link}) to use this bot.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Join Channel", url=invite_link)]
            ]),
            disable_web_page_preview=True
        )

@app.on_message(filters.channel & ~filters.forwarded)
async def forward_message(bot: Client, message: Message):
    if message.chat.id == UPDATES_CHANNEL:
        await bot.forward_messages(chat_id=message.forward_from_chat.id, from_chat_id=message.chat.id, message_ids=message.message_id)

app.run()
