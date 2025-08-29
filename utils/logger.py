import logging
import os
from config.config import Config

def setup_logger():
    """Настройка логирования"""
    
    # Создаем директорию для логов если её нет
    os.makedirs(os.path.dirname(Config.LOG_FILE), exist_ok=True)
    
    # Настраиваем формат логов
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Логгер для файла
    file_handler = logging.FileHandler(Config.LOG_FILE)
    file_handler.setFormatter(formatter)
    
    # Логгер для консоли
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    # Основной логгер
    logger = logging.getLogger('hourly-time-bot')
    logger.setLevel(Config.LOG_LEVEL)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Глобальный экземпляр логгера
logger = setup_logger()