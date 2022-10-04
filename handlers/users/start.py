from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"<b><i>Salom, <code>{message.from_user.full_name}</code>!\n\n🤖Krill-Lotin, Lotin-Krill botimizga xush kelibsiz!\n\n🔍Botdga istalgan so'zni yuboring, bot sizga o'girib beradi!</i></b>")
