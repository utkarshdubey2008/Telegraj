import telegraph
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up Telegraph credentials
telegraph_api = telegraph.Telegraph()
telegraph_api.create_account(short_name='your_short_name')

# Define the function to handle the /start command
def start(update, context):
    update.message.reply_text('Hi there! Send me a file and I will upload it to Telegraph for you.')

# Define the function to handle file uploads
def upload_file(update, context):
    file = context.bot.get_file(update.message.document.file_id)
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
```

Please make sure to replace `'your_short_name'` with your desired short name for Telegraph and `'your_bot_token'` with your actual Telegram bot token.