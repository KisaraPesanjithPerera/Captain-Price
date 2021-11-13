class script(object):
    START_TXT = """<b>🔥𝓗𝓲  𝓽𝓱𝓮𝓻𝓮 </b> {}

♨️𝗔𝗱𝗱 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 𝗔𝗻𝗱 𝗚𝗶𝘃𝗲 𝗔𝗱𝗺𝗶𝗻. 𝗙𝗿𝗼𝗺 𝗧𝗵𝗮𝘁 𝗧𝗶𝗺𝗲 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗪𝗶𝗹𝗹 𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝗠𝗼𝘃𝗶𝗲𝘀 𝗔𝗻𝗱 𝗦𝗲𝗿𝗶𝗲𝘀 𝗙𝗼𝗿 𝗥𝗲𝗾𝘂𝗲𝘀𝘁𝘀. 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗛𝗮𝘃𝗲 𝗧𝗵𝗲 𝗟𝗮𝗿𝗴𝗲𝘀𝘁 𝗠𝗼𝘃𝗶𝗲 & 𝗦𝗲𝗿𝗶𝗲𝘀 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲 𝗜𝗻 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺😜

🤖By Using Our Service You Must Agree To Our Privacy Policy 👀
"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """🔘 Just Send Series Name and Season OR Use Inline Search Button.
    
[Dont Use words Like Season/Episode/Series](https://t.me/MovieHubOfficialSL)

♻️ If any series is Not Available, Then Request it at
@MovieHubOfficialSL

✨ <b>My Name :</b>  [🔥𝐌𝐨𝐯𝐢𝐞𝐇𝐮𝐛 𝐅𝐢𝐥𝐭𝐞𝐫𝐬🔥](t.me/MHOFilter_bot)
👨‍💻 <b>Developer :</b> [𝚂𝚎𝚗𝚞 𝙶𝚊𝚖𝚎𝚛 𝙱𝚘𝚢](https://github.com/SenuGamerBoy)
🍀 <b>Data Base :</b> Mango DB
📝 <b>Language :</b> [Python3](https://python.org)
🧰 <b>Framework :</b> [Pyrogram](https://pyrogram.org)
📡 <b>Server :</b> [heroku](https://heroku.com)
🌹 <b>Build Status :</b> 𝚅2.5
"""
    CREDITS = """<b>Credit 🌟</b>
    
Jelly Bean is a movie auto filter bot as well as one bot in Telegram that can download movies inline. jelly is an open scoure closed project 🥲.

- <b>Dev 👨‍💻</b>

<b>[Senu Gamer Boy](https://github.com/SenuGamerBoy)</b>

- <b>Thanks to 👑</b>

<b>Dan</b> For His Awsome Libary
<b>Mahesh</b> For His Awesome Media-Search-bot
<b>Trojanz</b> for Their Awesome Unlimited Filter Bot And AutoFilterBoT
<b>Senu Gamer Boy</b> And His friend <b>SUBIN</b> """
    
    
"""
# MANUELFILTER_TXT = """."""
AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
    
<b>NOTE:</b>

1. Add me to your group
2. Then give me admin
3. Just send the name of the movie/TV series.🎥 Result will come to you.😍"""
CONNECTION_TXT = """Help: <b>Connections</b>
    
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>

1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
 EXTRAMOD_TXT = """
Help: <b>Extra Modules 🍀</b>
    
<b>NOTE:</b>
these are the extra features of 🔥𝐌𝐨𝐯𝐢𝐞𝐇𝐮𝐛 𝐅𝐢𝐥𝐭𝐞𝐫𝐬🔥

<b>Commands and Usage:</b>

• /id - <code>get id of a specifed user.</code>

• /info  - <code>get information about a user.</code>

• /imdb  - <code>get the film information from IMDb source.</code>

Coming Soon features For 🔥𝐌𝐨𝐯𝐢𝐞𝐇𝐮𝐛 𝐅𝐢𝐥𝐭𝐞𝐫𝐬🔥

Movie Player , Movie Uploader"""
ADMIN_TXT = """
Coming Soon"""
STATUS_TXT = """My Status 🤗
    
📂 Total Movie saved : <code>{}</code>
👤 Total Users : <code>{}</code>
📝 Total Groups : <code>{}</code>
🔰 Used Space : <code>{}</code> MB
🗃️ Free Space : <code>{}</code> MB

My Server Status 🍀

💻 CPU Usage :</b> {}%
☄️ RAM Usage :</b> {}%"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
