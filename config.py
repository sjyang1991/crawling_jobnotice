import os

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', '')
CHAT_ID = os.environ.get('CHAT_ID', '')
CRAWLING_URL = os.environ.get('CRAWLING_URL', '')

if not TELEGRAM_TOKEN or not CHAT_ID or not CRAWLING_URL:
    raise Exception('TELEGRAM_TOKEN, CAHT_ID, URL 확인 필요')