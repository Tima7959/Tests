from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from handlers.banwords import banwords

rt = Router()



@rt.message(CommandStart())
async def start(message: Message):
    await message.answer('Hello')


@rt.message(Command('help'))
async def help(message: Message):
    await message.answer('text for help')


@rt.message()
async def echo(message: Message):
    if banwords(message.text):
        await message.answer('Не надо так')
    else:
        await message.answer(f'{message.text}')


