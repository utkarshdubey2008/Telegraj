
import os

# Telegram bot token
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

# Telegraph short name
TELEGRAPH_SHORT_NAME = os.environ.get('TELEGRAPH_SHORT_NAME')

# Set up Telegraph credentials
telegraph_api = telegraph.api.Telegraph()
telegraph_api.create_account(short_name=TELEGRAPH_SHORT_NAME)

