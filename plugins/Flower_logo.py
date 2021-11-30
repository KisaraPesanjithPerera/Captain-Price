from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
import json

def nospace(s):

    s = re.sub(r"\s+", '%20', s)

    return s

@Client.on_message(filters.command("flow_logo"))
async def flow_logo(Client, message):
   send = await message.reply_text("🚀 Creating Logo.........")
   name = nospace(message.text.strip().split(None, 1)[1].lower())
    
   server=json.loads(requests.get(f'https://logo-technostoneyt.herokuapp.com/api/textmaker/alam?text={name}&theme=flower&apikey=prem').content)
   st=server['status']
   link=server['url']
   username=name
   api="prem"
   ssh=api+'$'+username
   logo_result=requests.get(f'https://logo-technostoneyt.herokuapp.com/api/textmaker/alam?text={str(ssh)}&theme=flower&apikey=prem').content
   try:
       json_logo=json.loads(logo_result)
       u_name=json_logo['username']
       ap=json_logo['api']
       li=json_logo['link']
       stt=json_ssh['st']
       result = f"""
🌺 Logo Created success 🌺 
"""
       await send.edit(result)
   except:
       await message.reply_text(ssh_result)
