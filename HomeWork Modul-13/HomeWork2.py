# Импорт библиотек
from aiogram import Bot, Dispatcher, executor, types  # Основные модули для работы с Telegram Bot API
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


# Создание объектов бота и диспетчера
api = 'Token'  # Токен Telegram-бота
bot = Bot(token=api)  # Инициализация бота
dp = Dispatcher(bot, storage=MemoryStorage())  # Инициализация диспетчера с хранением состояний
# =====================================================================================================
# Обработка сообщений
@dp.message_handler(commands=['start'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')


# =====================================================================================================
# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)  # Запуск long-polling для обработки сообщений
