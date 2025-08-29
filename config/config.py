import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

class Config:
    """Конфигурация бота"""
    
    # Токен бота из @MasterBot (обязательно!)
    BOT_TOKEN = os.getenv('BOT_TOKEN', '')
    
    # ID чата для отправки сообщений (можно получить эмпирически)
    TARGET_CHAT_ID = os.getenv('TARGET_CHAT_ID', '')
    
    # Настройки времени
    TIMEZONE = os.getenv('TIMEZONE', 'Europe/Moscow')
    
    # Настройки логирования
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', '/opt/hourly-time-bot/logs/bot.log')
    
    # Настройки API
    API_BASE_URL = 'https://botapi.max.ru'
    
    # Интервал проверки обновлений (в секундах)
    POLLING_INTERVAL = int(os.getenv('POLLING_INTERVAL', '30'))

# Проверяем обязательные параметры
if not Config.BOT_TOKEN:
    raise ValueError("BOT_TOKEN не установлен. Добавьте его в .env файл")