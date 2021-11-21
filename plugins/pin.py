#

from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.helper_functions.cust_p_filters import (
    admin_fliter
)

@Client.on_message(filters.command("pin"))
async def pin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.pin()


@Client.on_message(filters.command("unpin"))
async def unpin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.unpin()
