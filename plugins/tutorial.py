from pyrogram import Client, filters

@Client.on_message(filters.command("How"))
async def howto(client, message):
      client.send_photo(massage.chat.id, "https://www.creative-tim.com/blog/content/images/2021/07/coming-soon.jpg" caption="Coming Soon 👏👏👏")
