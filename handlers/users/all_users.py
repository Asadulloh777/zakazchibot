from aiogram import types

from loader import dp, baza


# Echo bot
@dp.message_handler(commands='foydalanuvchilar')
async def bot_echo(message: types.Message):
    userlar =  baza.userlar_soni()
    await message.answer(text=f"Hozirda {userlar[0]}, ta foydalanuvchi mavjud")
