import io
from re import template
from typing import Text

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import input_file
from aiohttp.helpers import IS_MACOS

from filters import IsGroup
from filters.admins import AdminFilter
from loader import dp, bot


@dp.message_handler(IsGroup(), Command("set_photo", prefixes="!/"), AdminFilter())
async def set_new_photo(message: types.Message):
    source_message = message.reply_to_message
    photo = source_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(photo)
    await message.chat.set_photo(photo=input_file)


@dp.message_handler(IsGroup(), Command("set_title", prefixes="!/"), AdminFilter())
async def set_new_title(message: types.Message):
    source_message = message.reply_to_message
    title = source_message.text
    await bot.set_chat_title(message.chat.id, title=title)


@dp.message_handler(IsGroup(), Command("set_description", prefixes="!/"), AdminFilter())
async def set_new_description(message: types.Message):
    source_message = message.reply_to_message
    description = source_message.text

    await bot.set_chat_description(message.chat.id, description=description)