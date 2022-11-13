from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "12538418")) 
API_HASH = getenv("API_HASH", "d3ff047ed516f4f1c587f9cbed3fae39")
ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN", "5684425350:AAElOZGbh5de0Eesrfe8ZQHAlR8MvqM86mo")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001538500204"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ilem:ilem@cluster0.uewtgbl.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1962124154").split()))
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/c94a14c0afe7abb639fe7.jpg")
START_IMG = getenv("START_IMG","https://telegra.ph/file/c94a14c0afe7abb639fe7.jpg")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/yahkenatipu")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TodoShotou")
STRING_SESSION = getenv("STRING_SESSION", "BQC8xti1iqScjWd9oBVc23jr3wwMJfwpBjq7ygRK3thuXJYmUtsCAYmO39Y3OXSuPrzyOl2Ddo_loo0Wz8M3ZMDigtZd59vZtEprOHTeE0IZLz3ODQJmZljf7quKS_vry7zOG5Y3Oh9xFVk1hYOliwC5f11u80vVYAweLxSCA1mJJbuuXhwhFmSOM7LTkhM8iEwa-TrKagHr77Bomcbk-XGNR80nI8Wnk0h3kswO0Cm3jPq-pUgh9GWROH0iELxqMKnbHPjrNf2ejzZlJYWDuReyUACnoX9jh9jHTPJjDDE-ODzVhzuEezP2IcCl_dFXfiaD2h1iYCCx-ktgBDAjgQDEAAAAAVjCLAQA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1962124154").split()))
