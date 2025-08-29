import requests
import schedule
import time
import pytz
from datetime import datetime
from typing import Optional, Dict, Any

from config.config import Config
from utils.logger import logger

class MaxBot:
    """Класс для работы с MAX Bot API"""
    
    def __init__(self, token: str):
        self.token = token
        self.base_url = Config.API_BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {token}'
        })
    
    def _make_request(self, method: str, endpoint: str, **kwargs) -> Optional[Dict[str, Any]]:
        """Базовый метод для выполнения HTTP запросов"""
        url = f"{self.base_url}{endpoint}"
        
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка запроса к {url}: {e}")
            return None
    
    def send_message(self, chat_id: str, text: str) -> bool:
        """Отправка сообщения в чат"""
        endpoint = f"/messages?chat_id={chat_id}"
        data = {
            "text": text,
            "format": "markdown"
        }
        
        result = self._make_request("POST", endpoint, json=data)
        if result:
            logger.info(f"Сообщение отправлено в чат {chat_id}")
            return True
        return False
    
    def get_updates(self, timeout: int = 30) -> Optional[Dict[str, Any]]:
        """Получение обновлений через Long Polling"""
        endpoint = f"/updates?timeout={timeout}&access_token={self.token}"
        return self._make_request("GET", endpoint)

class TimeBot:
    """Основной класс бота"""
    
    def __init__(self):
        self.max_bot = MaxBot(Config.BOT_TOKEN)
        self.target_chat_id = Config.TARGET_CHAT_ID
        self.timezone = pytz.timezone(Config.TIMEZONE)
    
    def get_current_time(self) -> str:
        """Получение текущего времени в формате строки"""
        now = datetime.now(self.timezone)
        return now.strftime("🕐 **Текущее время:** %H:%M (%Z)")
    
    def send_hourly_message(self):
        """Отправка сообщения с текущим временем"""
        if not self.target_chat_id:
            logger.warning("TARGET_CHAT_ID не установлен. Сообщение не отправлено.")
            return
        
        time_message = self.get_current_time()
        success = self.max_bot.send_message(self.target_chat_id, time_message)
        
        if success:
            logger.info(f"Успешно отправлено часовое сообщение: {time_message}")
        else:
            logger.error("Не удалось отправить часовое сообщение")
    
    def setup_scheduler(self):
        """Настройка планировщика задач"""
        # Отправка каждый час в 0 минут
        schedule.every().hour.at(":00").do(self.send_hourly_message)
        
        logger.info("Планировщик задач настроен")
    
    def run(self):
        """Запуск бота"""
        logger.info("Запуск Hourly Time Bot...")
        
        # Проверяем доступность токена
        if not Config.BOT_TOKEN:
            logger.error("BOT_TOKEN не установлен. Завершение работы.")
            return
        
        # Настраиваем планировщик
        self.setup_scheduler()
        
        logger.info("Бот запущен. Ожидание расписания...")
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Бот остановлен пользователем")
        except Exception as e:
            logger.error(f"Ошибка в основном цикле: {e}")

def main():
    """Точка входа в приложение"""
    bot = TimeBot()
    bot.run()

if __name__ == "__main__":
    main()