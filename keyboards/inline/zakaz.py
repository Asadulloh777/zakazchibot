from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

tugma = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Buyurtma berish➕', callback_data='bot')
        ]
    ]
)

tasdiq = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Qabul qilish✅', callback_data='qabul'),
            InlineKeyboardButton(text='Rad etish❌', callback_data='rad')
        ]
    ]
)

tasdiq1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Tasdiqlash✅ ', callback_data='tasdiq')
        ],
        [
            InlineKeyboardButton(text='Bekor qilish❌ ', callback_data='inkor')
        ]
    ]
)