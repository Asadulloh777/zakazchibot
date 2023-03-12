from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

knopka = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Tasdiqlash  (xato va kamchiliklar yo`qligiga ishonch hosil qiling!)')
        ],
        [
            KeyboardButton(text='Bekor qilish  (Malumotlar o`chirib yuboriladi!)')
        ]
    ],
    resize_keyboard=True
)