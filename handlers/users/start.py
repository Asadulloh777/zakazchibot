from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import CommandStart
from states.sorovnoma import sorovnoma
from keyboards.inline.zakaz import tugma, tasdiq, tasdiq1
from loader import dp, baza, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state : FSMContext):
    try:
        ism = message.from_user.first_name
        user = message.from_user.username
        tg_id = message.from_user.id
        await state.update_data({'id' : tg_id})
        baza.user_qoshish(firstname=ism, username=user, tg_id=tg_id)
    except Exception:
        pass
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!", reply_markup=tugma)
@dp.callback_query_handler(text='bot')
async def bot(message : types.CallbackQuery):
    await message.message.answer(text='Ismingizni kiriting:', reply_markup=ReplyKeyboardRemove())
    await sorovnoma.ism.set()
@dp.message_handler(state=sorovnoma.ism)
async def bot1(message : types.Message, state : FSMContext):
    ism = message.text
    await state.update_data({'ism': ism})
    await message.answer(text='Familiyangizni kiriting:')
    await sorovnoma.fam.set()
@dp.message_handler(state=sorovnoma.fam)
async def bot1(message : types.Message, state : FSMContext):
    fam = message.text
    await state.update_data({'fam': fam})
    await message.answer(text='Telefon raqamingizni kiriting:')
    await sorovnoma.telefon.set()
@dp.message_handler(state=sorovnoma.telefon)
async def bot1(message : types.Message, state : FSMContext):
    telefon = message.text
    await state.update_data({'telefon': telefon})
    await message.answer(text='Gmail pochtangizni kiriting:')
    await sorovnoma.mail.set()
@dp.message_handler(state=sorovnoma.mail)
async def bot1(message : types.Message, state : FSMContext):
    mail = message.text
    await state.update_data({'mail': mail})
    await message.answer(text='Hududingizni kiriting:')
    await sorovnoma.hudud.set()
@dp.message_handler(state=sorovnoma.hudud)
async def bot1(message : types.Message, state : FSMContext):
    hudud = message.text
    await state.update_data({'hudud': hudud})
    await message.answer(text='Buyurtmangiz haqida batafsil so`zlab bering:')
    await sorovnoma.buyurtma.set()
@dp.message_handler(state=sorovnoma.buyurtma)
async def bot1(message : types.Message, state : FSMContext):
    buyurtma = message.text
    await state.update_data({'buyurtma': buyurtma})
    await message.answer(text='Muddatni  kiriting:')
    await sorovnoma.muddat.set()
@dp.message_handler(state=sorovnoma.muddat)
async def bot1(message : types.Message, state : FSMContext):
    muddat = message.text
    tg_id = message.from_user.id
    user = message.from_user.username
    await state.update_data({'username': user, 'tg_id': tg_id})
    await state.update_data({'muddat': muddat})
    infos =  await  state.get_data()

    ism1 = infos.get('ism')
    fam = infos.get('fam')
    telefon = infos.get('telefon')
    mail = infos.get('mail')
    hudud = infos.get('hudud')
    buyurtma = infos.get('buyurtma')
    muddat = infos.get('muddat')
    xabar = f"Ism : {ism1} \n" \
            f"Familiya : {fam}\n" \
            f"Username : {user}\n" \
            f"Telefon raqam : {telefon}\n" \
            f"Gmail pochta : {mail}\n" \
            f"Hudud : {hudud}\n" \
            f"Buyurtma : {buyurtma}\n" \
            f"Muddat : {muddat}"
    await message.answer(text=xabar, reply_markup=tasdiq1)
    await sorovnoma.tasdiq.set()

@dp.callback_query_handler(state=sorovnoma.tasdiq, text='tasdiq')
async def bot2(message : types.CallbackQuery, state : FSMContext):
    await message.message.answer(text='Malumotlar dasturchiga yuborildi!', reply_markup=ReplyKeyboardRemove())
    infos = await  state.get_data()

    ism1 = infos.get('ism')
    fam = infos.get('fam')
    a = infos.get('username')
    telefon = infos.get('telefon')
    mail = infos.get('mail')
    hudud = infos.get('hudud')
    buyurtma = infos.get('buyurtma')
    muddat = infos.get('muddat')
    xabar = f"Ism : {ism1} \n" \
            f"Familiya : {fam}\n" \
            f"Username : {a}\n" \
            f"Telefon raqam : {telefon}\n" \
            f"Gmail pochta : {mail}\n" \
            f"Hudud : {hudud}\n" \
            f"Buyurtma : {buyurtma}\n" \
            f"Muddat : {muddat}"

    try:
        baza.add_zakaz(fistname=ism1, lastname=fam,  telefon=telefon, email=mail, hudud=hudud, buyurtma=buyurtma, muddat=muddat)
    except Exception:
        pass
    await bot.send_message(chat_id=1710770340, text=xabar, reply_markup=tasdiq)


@dp.callback_query_handler(state=sorovnoma.tasdiq, text='inkor')
async def bot2(message : types.CallbackQuery, state : FSMContext):
    await message.message.answer(text='Malumotlar o`chirib  yuborildi!', reply_markup=ReplyKeyboardRemove())


@dp.callback_query_handler(chat_id=1710770340, text='qabul')
async def bot3(message: types.CallbackQuery, state : FSMContext):
    info = await state.get_data()
    tg_id = info.get('id')
    await bot.send_message(chat_id=tg_id, text='Buyurtmangiz dasturchi tomonidan qabul qilindi! Qo`shimcha ma`lumotlar bilan shu profilega murojaat qiling👉: @Pythonchi_UZB ')
    await bot.send_message(chat_id=tg_id, text='👍')
    await state.finish()

@dp.callback_query_handler(chat_id=1710770340, text='rad')
async def bot3(message: types.CallbackQuery, state : FSMContext):
    inf = await state.get_data()
    tg_id = inf.get('id')
    await bot.send_message(chat_id=tg_id, text='Buyurtmangiz qabul qilinmadi.Buyurtma juda qiyin yoki noto`g`ri tavsiflangan.  Buyurtmangiz to`g`ri tavsiflanganini tekshiring. ')
    await bot.send_message(chat_id=tg_id, text='☹')
    await state.finish()