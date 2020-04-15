import telegram
from config import TELEGRAM_TOKEN, CHAT_ID, CRAWLING_URL

bot = telegram.Bot(token=TELEGRAM_TOKEN)

def send(results):
    bot.sendMessage(chat_id = CHAT_ID, text = results)