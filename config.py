import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
STRING_SESSION = getenv("STRING_SESSION", "session")
BOT_NAME = getenv("BOT_NAME", "bot")
BOT_USERNAME = getenv("BOT_USERNAME", "username")
BOT_TOKEN = getenv("BOT_TOKEN", "token")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1323020756").split()))
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "HeroOfficialBots")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Baddies2Buddies")
OWNER_NAME = getenv("OWNER_NAME", "Shailendra34")

IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/d08d6474628be7571f013.png")
