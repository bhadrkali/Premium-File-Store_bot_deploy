from operator import add
import os
import logging

from logging.handlers import RotatingFileHandler

#your bot token here from https://telegram.me/BotFather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7278104225:AAELo0AtOQ_jbGYJPgWDcM-6olmoLJ3tkp8") 
#your api id from https://my.telegram.org/apps
APP_ID = int(os.environ.get("APP_ID", "25517360"))
#your api hash from https://my.telegram.org/apps
API_HASH = os.environ.get("API_HASH", "011e52db3b8390422cb2510d04d74fc9")
#your channel_id from https://t.me/MissRose_bot by forwarding dummy message to rose and applying command `/id` in reply to that message
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002196480720"))
#your channel link
CHANNEL_LINK = os.environ.get("CHANNEL_LINK", "-1002196480720")
#your id of telegram can be found by https://t.me/MissRose_bot with '/id' command
OWNER_ID = int(os.environ.get("OWNER_ID", "6524542196"))
#port set to default 8080
PORT = os.environ.get("PORT", "8080")
#your database url
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://JobTask:JobTask@cluster0.sivitpp.mongodb.net/") 
#your database name
DB_NAME = os.environ.get("DATABASE_NAME", "Premium-Store-bot")
#force user to join your backup channel
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002243479079"))
#for creating telegram thread for bot to improve performance of the bot
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
#your start default command message.
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
#your telegram tag
OWNER_TAG = ""
#add admins in the list without "" or ''
ADMINS=[34768, 343487]#remove predefined numbers <<just for demonstration purpose
try:
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
#force message for joining the channel
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"
ADMINS.append(OWNER_ID)

LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
