import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6038893670:AAEmbVbAFGC3aejZYyA3hXhafOGCHe045Ak")

    API_ID = int(os.environ.get("API_ID", 22524363))

    API_HASH = os.environ.get("API_HASH", "96e150cdf7b9f5c4d960add8be4debb3")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5390385209").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001865577872")

    MAX_FILE_SIZE = 4194304000

    TG_MAX_FILE_SIZE = 4194304000

    FREE_USER_MAX_FILE_SIZE = 4194304000

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://telegra.ph/file/3b7ec1308edb07983efef.png")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 0

    DEF_WATER_MARK_FILE = "Use this bot @real13xx"

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Ibrahim:ibrahim@cluster0.dy9extz.mongodb.net/?retryWrites=true&w=majority")

    SESSION_NAME = os.environ.get("SESSION_NAME", "UploadLinkToFile")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001872431471))

    LOGGER = logging

    OWNER_ID = int(os.environ.get("OWNER_ID", "5390385209"))

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001865577872")
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "urluploaderbabe_bot")
