from telethon import TelegramClient, events
import os

# ==== CONFIG ====
api_id = int(os.getenv("API_ID"))       # Set in Render env vars
api_hash = os.getenv("API_HASH")        # Set in Render env vars

source_usernames = [
    'Saleghar',
    'LootJunctionn',
    '+SyyT78KRclHKYJeP',
    'Dc_loots_dcloots',
    'gyrodeals',
    '+opX5gBA8ACozMmZl'
]  # without @
earnkaro_bot = 'Affiliaters3Bot'        # without @
# =================

# This will use your pre-saved session file (session_name.session)
client = TelegramClient('session_name', api_id, api_hash)
source_entities = []

async def resolve_entities():
    global source_entities
    source_entities = [await client.get_entity(username) for username in source_usernames]

@client.on(events.NewMessage())
async def handler(event):
    if event.chat_id in [entity.id for entity in source_entities]:
        try:
            await client.forward_messages(earnkaro_bot, event.message)
            print(f"✅ Forwarded from {event.chat.title} to {earnkaro_bot}")
        except Exception as e:
            print(f"❌ Error forwarding: {e}")

async def main():
    print("🔄 Resolving channel usernames...")
    await resolve_entities()
    print("🚀 Bot is running...")

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
