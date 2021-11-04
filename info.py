import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]
TUTORIAL = "t.me/MainlandGroup_CC"
# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm Jely Been Clone Bot you can call me as Jely Been **
Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)

# caption
default_start_cap = """
📝 File Name : <code>{file_name}</code>

🧲 File Size : {file_size}
<b>
 ┏━━━━•❅•°•❈•°•❅•━━━━┓
✰👑ɱσѵเε ɦµɓ σƒƒเ૮เαℓ👑✰
 ┗━━━━•❅•°•❈•°•❅•━━━━┛
🎭Proudly Presented By🎭 </b>
 @MovieHubOfficialSL
"""

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
PICS = (environ.get('PICS', 'https://telegra.ph/file/3553edf2ec4f52e8a5cf9.jpg')).split()
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'MaX_Bots_Support')
IMDB = eval((environ.get('IMDB', "True")))
P_TTTI_SHOW_OFF = eval((environ.get('P_TTTI_SHOW_OFF', "False")))
BUTTON = environ.get("BUTTON",False)
FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", default_start_cap)
SINGLE_BUTTON = eval((environ.get('SINGLE_BUTTON', "True")))
OMDB_API_KEY = environ.get("OMDB_API_KEY", "http://www.omdbapi.com/?i=tt3896198&apikey=4f08a979")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY

LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "True"), True)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
