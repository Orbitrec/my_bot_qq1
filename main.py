import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
API_TOKEN = '6121690073:AAF-6Z1mRc8ZJ7lusS_pfgFIkEGWN-CWIS4'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


global step = 0

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Привет, я калькулятор бот.")

@dp.message_handler()
async def echo(message: types.Message):


    await message.answer("Введите первое число")
    global num1;
    num1 = message.text


@dp.message_handler()
async def echo(message: types.Message):

    await message.answer("Введите второе число")
    global num2;
    num2 = message.text

@dp.message_handler()
async def echo(message: types.Message):


    await message.answer("Введите действие")

async def echo(message: types.Message):

    global oper;
    oper = message.text
    if oper == "+":
        result = int(num1) + int(num2)
        await message.answer(message.text, f"{result}")
    elif oper == "-":
        result = int(num1) - int(num2)
        await message.answer(message.text, f"{result}")
    elif oper == "*":
        result = int(num1) * int(num2)
        await message.answer(message.text, f"{result}")
    elif oper == "/":
        result = int(num1) / int(num2)
        await message.answer(message.text, f"{result}")
    else:
        await message.answer("Ошибка. Введите /start")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)