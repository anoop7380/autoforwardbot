from telethon import TelegramClient

api_id = 11312838   # your API ID from my.telegram.org
api_hash = 'dd5bfbf1d085b08e8156f9a1a07dff16'   # your API hash
phone = '+919997477794'  # your Telegram phone number with country code

client = TelegramClient('session_name', api_id, api_hash)
client.start(phone=phone)
print("✅ Session saved as session_name.session")
