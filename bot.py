import os
import asyncio
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.filters.text import Text
from aiogram.types import ChatPermissions

bot = Bot(token=os.getenv("TOKEN"))

dp = Dispatcher()

WEBHOOK_HOST = 'https://tcontact.ru'
WEBHOOK_PATH = '/api/telegram'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

@dp.message(Command("start"))
async def start(mess: types.Message):
    await mess.answer("Добро пожаловать в Бот, который будет уведомлять вас о запланированных встречах и мероприятиях!\n\nДля начала работы необходимо авторизоваться\n\nВведите ваш ноиер телефона в формате +7ХХХХХХХХХХ, тот же, что указывали при регистрации на платформе\nПример: +79991113355")

@dp.message(Text(startswith='+'))
async def phone(mess: types.Message):
    # await bot.restrict_chat_member(mess.chat.id, mess.from_user.id, permissions=ChatPermissions(can_send_messages=False))
    await mess.answer("Проверяем...")
    requests.post("https://tcontact.ru/api/add_telegram_bot_sv", data={
        "chat_id": mess.chat.id,
        "phone": mess.text
    })

@dp.message()
async def not_found(mess: types.Message):
    await mess.answer("Неверный формат. Убедитесь что ввели '+' перед номером.\n\nПример ввода: +79991112244")

# async def main():
#     await dp.start_polling(bot)

if __name__ == "__main__":
    dp.run_polling(bot)
