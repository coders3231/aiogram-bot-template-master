from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("<b><i>❗️Botdan foydalanish uchun istalgan so'zni yuboring!\n",
            "🔍Bot bu so'zni avtomatik tarzda agar lotin bo'lsa krill aksincha krill bo'lsa lotin alifbosida qaytaradi.\n",

            "🧑‍💻Bot buyicha savol va takliflar: @coder3231</i></b>")
    
    await message.answer("\n".join(text))
