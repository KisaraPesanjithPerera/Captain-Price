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
        text=f"My Server Status 🍀\n\n"
             f"**📂 Used Space :** {used}({disk_usage}%) \n"
             f"**🌌 Free Space :** {free} \n"
             f"**💻 CPU Usage :** {cpu_usage}% \n"
             f"**☄️ RAM Usage :** {ram_usage}%\n\n"
             f"**My User Status 🤗**\n\n"
             f"**Total Users in DB:** `{total_users}`\n"
             f"**Total Groups in DB:** `{chats}`"
        parse_mode="Markdown",
        quote=True
    )
