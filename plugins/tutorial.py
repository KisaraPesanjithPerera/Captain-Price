from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message

@Client.on_message(filters.command("How"))
async def howto(client, message):
      client.send_photo(massage.chat.id, "https://www.creative-tim.com/blog/content/images/2021/07/coming-soon.jpg" caption="Coming Soon 👏👏👏")
