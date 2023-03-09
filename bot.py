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



import telegraph
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up Telegraph credentials
telegraph_api = telegraph.api.Telegraph()
telegraph_api.create_account(short_name='your_short_name')

# Define the function to handle the /start command
def start(update, context):
    update.message.reply_text('Hi there! Send me a file and I will upload it to Telegraph for you.')

# Define the function to handle file uploads
def upload_file(update, context):
    file = context.bot.getFile(update.message.document.file_id)
    file_url = telegraph_api.upload(file=file.file_path)[0]['url']
    update.message.reply_text(f'Your file has been uploaded to Telegraph: {file_url}')

# Set up the Telegram bot
updater = Updater(token='your_bot_token', use_context=True)
dispatcher = updater.dispatcher

# Add the command and message handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.document, upload_file))

# Start the bot
updater.start_polling()
