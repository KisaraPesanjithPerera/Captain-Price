import pyrogram
import asyncio
import os
from pyrogram import Client, filters

@bot.on_message(filters.privet & filters.video)
async def tvidei(bot, message):
  await message.reply(message.video.file_id)
