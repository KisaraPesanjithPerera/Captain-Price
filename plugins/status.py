import shutil
import psutil
from pyrogram import filters
from pyrogram.types import (
    Message
)
from utils import humanbytes


@Client.on_message(filters.command("status") & ~filters.edited)
async def status_handler(_, m: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    chats = await db.total_chat_count()
    await m.reply_text(
        text=f"<b>My Server Status 🍀</b>\n\n"
             f"<b>📂 Used Space :</b> {used}({disk_usage}%) \n"
             f"<b>🌌 Free Space :</b> {free} \n"
             f"<b>💻 CPU Usage :</b> {cpu_usage}% \n"
             f"<b>☄️ RAM Usage :</b> {ram_usage}%\n\n"
             f"<b>My User Status 🤗</b>\n\n"
             f"<b>Total Users in DB :</b> `{total_users}`\n"
             f"<b>Total Groups in DB :</b> `{chats}`"
        parse_mode="html",
        quote=True
    )
