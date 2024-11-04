from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


BOT_TOKEN = '---какой-то-BOT-TOKEN---'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=['start']))
async def start_message(message: Message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message()
async def all_massages(message: Message):
    print('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    dp.run_polling(bot)

