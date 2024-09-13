from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram import F
import asyncio
import logging

API_TOKEN = '7246937741:AAGkH94PAE24bFBoQVADS2mIlLNpHtSCdj8'
CHANNEL_ID = '-1002181122538'  # Замените на ID вашего канала
WEB_APP_URL = 'https://your-web-app-url.com'  # Ссылка на ваш Telegram Web App

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Проверка подписки на канал
async def check_subscription(user_id: int):
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        if member.status != 'left':
            return True
        return False
    except Exception as e:
        return False

@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username

    # Проверка подписки
    if await check_subscription(user_id):
        # Если подписан, даем ссылку на Telegram Web App
        keyboard = InlineKeyboardMarkup()
        button = InlineKeyboardButton('Перейти в Web App', url=WEB_APP_URL)
        keyboard.add(button)

        await message.answer(f"Привет, {username}! Вы успешно подписаны на канал. Нажмите на кнопку ниже для входа в Web App.", reply_markup=keyboard)
    else:
        # Если не подписан, отправляем просьбу подписаться
        keyboard = InlineKeyboardMarkup()
        subscribe_button = InlineKeyboardButton('Подписаться на канал', url=f"https://t.me/{CHANNEL_ID}")
        keyboard.add(subscribe_button)

        await message.answer(f"Привет, {username}! Пожалуйста, подпишитесь на наш канал, чтобы продолжить.", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
