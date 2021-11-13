import pyrogram
import asyncio
import os
from pyrogram import Client, filters

@Client.on_message(filters.privet & filters.video)
def tvidei(bot, message):
  await message.reply(message.video.file_id)
