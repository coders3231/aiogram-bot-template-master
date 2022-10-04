from aiogram import types
from transliterate import to_latin, to_cyrillic
from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    b=message.text
    if b.isascii():
        await message.answer(f"<b><i> 👉  <code>{to_cyrillic(message.text)}</code>\n\nTepadagi matnni ustiga bosing avtomatik nusxalanadi.\n👉@LOTIN_KRILL_TRANSLATE_BOT</i></b>")
    else:
        await message.answer(f"<b><i> 👉  <code>{to_latin(message.text)}</code>\n\nТепадаги матнни устига босинг автоматик нусхаланади.\n👉@LOTIN_KRILL_TRANSLATE_BOT</i></b>")
