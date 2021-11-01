class script(object):
    START_TXT = """🔥𝓗𝓲  𝓽𝓱𝓮𝓻𝓮...

♨️𝗔𝗱𝗱 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 𝗔𝗻𝗱 𝗚𝗶𝘃𝗲 𝗔𝗱𝗺𝗶𝗻. 𝗙𝗿𝗼𝗺 𝗧𝗵𝗮𝘁 𝗧𝗶𝗺𝗲 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗪𝗶𝗹𝗹 𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝗠𝗼𝘃𝗶𝗲𝘀 𝗔𝗻𝗱 𝗦𝗲𝗿𝗶𝗲𝘀 𝗙𝗼𝗿 𝗥𝗲𝗾𝘂𝗲𝘀𝘁𝘀. 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗛𝗮𝘃𝗲 𝗧𝗵𝗲 𝗟𝗮𝗿𝗴𝗲𝘀𝘁 𝗠𝗼𝘃𝗶𝗲 & 𝗦𝗲𝗿𝗶𝗲𝘀 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲 𝗜𝗻 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺😜

🤖By Using Our Service You Must Agree To Our Privacy Policy 👀
"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """🔘 Just Send Series Name and Season OR Use Inline Search Button.
    
[Dont Use words Like Season/Episode/Series](https://t.me/MovieHubOfficialSL)

♻️ If any series is Not Available, Then Request it at
@MovieHubOfficialSL

✨ **My Name :**  [🔥𝐌𝐨𝐯𝐢𝐞𝐇𝐮𝐛 𝐅𝐢𝐥𝐭𝐞𝐫𝐬🔥](t.me/MHOFilter_bot)
👨‍💻 **Developer :** [𝚂𝚎𝚗𝚞 𝙶𝚊𝚖𝚎𝚛 𝙱𝚘𝚢](https://github.com/SenuGamerBoy)
🍀 Data Base : Mango DB
📝 **Language :** [Python3](https://python.org)
🧰 **Framework :** [Pyrogram](https://pyrogram.org)
📡 **Server :** [heroku](https://heroku.com)
🌹 **Build Status :** 𝚅2.5
"""
    SOURCE_TXT = """MMa</a>"""
    LOGO_TEXT = """ 🔹 `/hlogo` <text> :  Create your logo with your name
 🔹 `/alogo` <text> :  Create your logo with your name"""
    MANUELFILTER_TXT = """Coming Soon 🚀....."""
    BUTTON_TXT = """Help: <b>Buttons</b>
    
- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>

1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>

<code>[Button Text](buttonurl:https://t.me/MHOFilter_bot)</code>

<b>Alert buttons:</b>

<code>[Button Text](buttonalert:This is an alert message)</code>"""
    
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

Cming Soon features For 🔥𝐌𝐨𝐯𝐢𝐞𝐇𝐮𝐛 𝐅𝐢𝐥𝐭𝐞𝐫𝐬🔥

Movie Player , Movie Uploader"""
    ADMIN_TXT = """
Coming Soon"""
    STATUS_TXT = """📂 Total Movie saved : <code>{}</code>
👤 Total Users : <code>{}</code>
📝 Total Groups : <code>{}</code>
🔰 Used Space : <code>{}</code> MB
🗃️ Free Space : <code>{}</code> MB"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
