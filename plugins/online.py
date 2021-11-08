import re
from typing import Text
from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, InlineQuery, InlineQueryResultArticle, \
InputTextMessageContent



def nospace(s):

    s = re.sub(r"\s+", '%20', s)

    return s

@bot.on_message(filters.command("onlinev"))
async def movie(_, message):
    name = nospace(message.text.strip().split(None, 1)[1].lower())
    m = await message.reply_text("**Searing🍿**")
    await m.edit("👇👇 𝙍𝙚𝙨𝙪𝙡𝙩 𝙁𝙤𝙧 𝙔𝙤𝙪𝙧 𝙌𝙪𝙚𝙧𝙮 👇👇")
    try:
        await message.reply_text(
            text=f"Result for your requested query `{name}` \n\n皿───────────────皿\n\n**🍀 View It Online :** [Link Here](https://www.2embed.ru/embed/imdb/movie?id={name})\n**⭐️ IMDB Link : [View Movie Details On imdb](https://www.imdb.com/title/{name}/) \n\n🌾 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 🌾 : @MaX_Bots \n\n皿───────────────皿\n\n💝Brought to You : {message.chat.title}\n\n`■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■`",
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("View Movie 👻", url=f"https://www.2embed.ru/embed/imdb/movie?id={name}")
                    ]
                ]
            )
        )
    except Exception as e:
        await message.reply_text(str(e))
