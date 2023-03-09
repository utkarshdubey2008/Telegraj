#    This file is part of the ChannelAutoForwarder distribution (https://github.com/utkarsh212646/Telegraph_uploader).
#    Copyright (c) 2021 Rithunand
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/utkarsh212646/Telegraph_Uploader/blob/main/License> 


import os
import requests
from telegraph import Telegraph

from pyrogram import Client, filters
from pyrogram.types import Message

# Replace with your bot token
BOT_TOKEN = "6218979167:AAFwntHGW5irHRgv-_sKn1KiWK3FuLxeYkM"

app = Client("my_bot", bot_token=BOT_TOKEN)
telegraph = Telegraph()

@app.on_message(filters.photo)
async def upload_image(bot: Client, message: Message):
    # Download the photo to a temporary file
    photo = message.photo[-1]
    file_path = await bot.download_media(photo.file_id)
    
    # Upload the photo to Telegraph
    with open(file_path, "rb") as f:
        img_url = telegraph.upload(f)["src"]
    
    # Send the Telegraph URL to the user
    await bot.send_message(
        chat_id=message.chat.id,
        text=img_url,
        disable_web_page_preview=True
    )

app.run()

