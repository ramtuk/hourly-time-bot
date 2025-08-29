# 🤖 Hourly Time Bot for MAX Platform

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Бот для платформы MAX, который отправляет уведомления с текущим временем каждый час в указанный чат.

## ✨ Возможности

- ⏰ Автоматическая отправка времени каждый час
- 🌍 Поддержка различных временных зон
- 📊 Логирование всех операций
- 🔧 Простая конфигурация через environment variables
- 🐳 Готовность к деплою как systemd service

## 🚀 Быстрый старт

### Предварительные требования

- Python 3.8+
- Аккаунт в MAX платформе
- Зарегистрированный бот через @MasterBot

### Установка

1. **Клонирование репозитория:**
```bash
git clone https://github.com/ramtuk/hourly-time-bot.git
cd hourly-time-bot
Настройка виртуального окружения:

bash
python -m venv venv
source venv/bin/activate
Установка зависимостей:

bash
pip install -r requirements.txt
Настройка конфигурации:

bash
cp .env.example .env
# Отредактируйте .env файл с вашими настройками
Конфигурация
Создайте файл .env со следующими параметрами:

env
# Обязательные параметры
BOT_TOKEN=your_bot_token_from_masterbot
TARGET_CHAT_ID=your_target_chat_id

# Опциональные параметры
TIMEZONE=Europe/Moscow
LOG_LEVEL=INFO
LOG_FILE=/path/to/logs/bot.log
POLLING_INTERVAL=30
Как получить BOT_TOKEN
Найдите в MAX бота @MasterBot

Отправьте команду /create

Следуйте инструкциям для создания бота

Сохраните полученный токен

Как получить CHAT_ID
Добавьте бота в нужный чат

Напишите любое сообщение в чате

Бот автоматически определит chat_id и запишет его в логи

Запуск
Ручной запуск:

bash
python run.py
Запуск как systemd service:

bash
# Копируем конфигурационный файл
sudo cp systemd/hourly-time-bot.service /etc/systemd/system/

# Перезагружаем systemd
sudo systemctl daemon-reload

# Включаем автозагрузку
sudo systemctl enable hourly-time-bot.service

# Запускаем сервис
sudo systemctl start hourly-time-bot.service

# Проверяем статус
sudo systemctl status hourly-time-bot.service
📁 Структура проекта
text
hourly-time-bot/
├── src/                    # Исходный код
│   ├── bot.py             # Основной модуль бота
│   └── __init__.py
├── config/                # Конфигурация
│   └── config.py         # Настройки приложения
├── utils/                # Вспомогательные утилиты
│   └── logger.py        # Логирование
├── logs/                # Директория логов
├── tests/              # Тесты (будущее)
├── requirements.txt    # Зависимости Python
├── .env.example       # Пример environment variables
├── run.py            # Точка входа
└── README.md        # Документация
🛠️ Разработка
Установка для разработки
bash
git clone https://github.com/ramtuk/hourly-time-bot.git
cd hourly-time-bot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
Логирование
Логи сохраняются в файл и выводятся в консоль. Уровень логирования настраивается через LOG_LEVEL.

Тестирование
bash
# Запуск тестов (будущее)
python -m pytest tests/
📝 License
Этот проект лицензирован под MIT License - смотрите файл LICENSE для деталей.

🤝 Contributing
Форкните репозиторий

Создайте feature branch (git checkout -b feature/amazing-feature)

Закоммитьте изменения (git commit -m 'Add amazing feature')

Запушьте branch (git push origin feature/amazing-feature)

Откройте Pull Request

📞 Поддержка
Если у вас есть вопросы или предложения, создавайте issue в репозитории.

⭐ Не забудьте поставить звезду репозиторию, если проект вам помог!