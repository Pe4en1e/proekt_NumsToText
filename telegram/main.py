from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from rich.progress import track
from rich import print
import time
import inflect
from googletrans import Translator

translator=Translator()
p = inflect.engine()

bot=Bot(token='5661180424:AAEARAsMfPddOCJqFtT4CWXIeewoXLpIzPk')
dp=Dispatcher(bot, storage=MemoryStorage())

async def on_startup(_):
    for i in track(range(3), description="Включение бота..."):
        time.sleep(1)
    print('[bold green]Бот запущен!')


@dp.message_handler(commands=['start'])
async def command_start(message:types.message):
    await bot.send_message(chat_id=message.chat.id, text='Привет! Данный бот предназначен для перевода чисел в текстовую запись')

@dp.message_handler()
async def priem(message:types.message):
    num=message.text
    if num.isdigit():
        def zmn(x): 
            y=(p.number_to_words(x))
            ts=translator.translate(str(y), src='en', dest='ru')
            output=ts.text
            return output.replace(',', '')
        await bot.send_message(chat_id=message.chat.id, text=zmn(num))
    else:
        await bot.send_message(chat_id=message.chat.id, text='Извини, я работаю только с числами!')

@dp.message_handler()
async def priem(message:types.message):
    num=message.text
    if num.isdigit():
        def zmn(x): 
            y=(p.number_to_words(x))
            ts=translator.translate(str(y), src='en', dest='ru')
            output=ts.text
            return output.replace(',', '')
        await bot.send_message(chat_id=message.chat.id, text=zmn(num))
    else:
        await bot.send_message(chat_id=message.chat.id, text='Извини, я работаю только с числами!')
        

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

