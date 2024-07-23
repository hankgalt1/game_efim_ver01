import asyncio
from datetime import time

from pytonconnect import TonConnect
import pytonconnect
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.keyboard import InlineKeyboardBuilder
from pytoniq_core import Address

##########################################################
from Connect_BD import Database,Database_boost
from aiogram import Dispatcher, Bot, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery, InputMediaPhoto
from aiogram import types
from aiogram.types.web_app_info import WebAppInfo
from PIL import Image, ImageDraw, ImageFont
####################################################################
TOKEN = "6493506230:AAFA-66RvNZoeOmz9n0cN7y_RrJW8MuPM90"
BOT_NICKNAME = "Hoary_Efim_bot"
dp = Dispatcher()
bot = Bot(token=TOKEN)
###########################################################################
def connect_DB():
    db = Database()
    return db
def connect_DB_boost():
    dbb = Database_boost()
    return dbb
###########################################################################
class klen(StatesGroup):
    username = State()
    count = State()
class ecoin(StatesGroup):
    username = State()
    count = State()
class profil(StatesGroup):
    username = State()

###########################################################################
def extract_unique_code(text):
    return text.split()[1] if len(text.split()) > 1 else None
############################################################################
@dp.message(CommandStart())
async def handle_start(message: types.Message):
    unique_code = extract_unique_code(message.text)

    User_status = connect_DB().users_id(message.from_user.id)
    if User_status == False:
        if unique_code != None:
            connect_DB().add_user_s_referal(message.from_user.id, message.from_user.username, None, None, unique_code,0,0,0,0,0,0,0,0,0,0,0,False,False,False)
            kl = connect_DB().get_count_klen_by_user_id(unique_code)
            connect_DB().add_klen_by_id(kl+25,unique_code)
            ref_refa = connect_DB().get_ref_by_user_id(unique_code)
            print(f"Реферал,реферала = {ref_refa}")
            if ref_refa != 0:
                kln = connect_DB().get_count_klen_by_user_id(ref_refa)
                connect_DB().add_klen_by_id(kln+7,ref_refa)

        else:
            connect_DB().add_user_no_referal(message.from_user.id, message.from_user.username, None, None, None ,0,0,0,0,0,0,0,0,0,0,0,False,False,False)
    else:
        pass
##############################################################################################
    await message.delete()
    await message.answer("Select a language.\n"
                         "Выберите язык.", reply_markup=select_language())
@dp.callback_query()
async def callbacks_num(callback: types.CallbackQuery):
    print(callback.data)

    #########################################################################################
    if callback.data == "en_buttom":
        connect_DB().add_lang_by_id("EN", callback.from_user.id)
        await callback.answer("English is selected")
        await callback.message.edit_text(
                f"I'm glad to see you {callback.from_user.full_name}.\n"
                f" \n This is the official bot of the Hoary Efim project\n",reply_markup=okey_en())

    if callback.data == "ru_buttom":
        connect_DB().add_lang_by_id("RU", callback.from_user.id)
        await callback.answer("Выбран язык Русский")
        await callback.message.edit_text(
                f"Рад видеть тебя {callback.from_user.full_name}.\n"
                f" \n Это официальный бот проекта Седой Ефим | Hoary Efim🫡\n",reply_markup=okey())

    if callback.data == "okey":
        profile_image(callback.from_user.id,
                      connect_DB().get_data_reg_by_user_id(callback.from_user.id),
                      connect_DB().count_referal(callback.from_user.id),
                      connect_DB().get_count_klen_by_user_id(callback.from_user.id),
                      connect_DB().get_count_ecoin_by_user_id(callback.from_user.id),
                      connect_DB().get_count_derevo_by_user_id(callback.from_user.id),
                      connect_DB().get_count_utka_by_user_id(callback.from_user.id),
                      connect_DB().get_count_shariki_by_user_id(callback.from_user.id),
                      connect_DB().get_count_metla_by_user_id(callback.from_user.id),
                      connect_DB().get_count_jet_by_user_id(callback.from_user.id),
                      connect_DB().get_count_shapka_by_user_id(callback.from_user.id),
                      connect_DB().get_count_zont_by_user_id(callback.from_user.id),
                      connect_DB().get_lang_by_user_id(callback.from_user.id))

        photo = FSInputFile(f"image_profile/{callback.from_user.id}.jpg")
        connector = get_connector(callback.from_user.id)
        connected = await connector.restore_connection()


        await bot.send_photo(callback.message.chat.id, photo=photo,
                             reply_markup=my_profile(connected))
        await callback.message.delete()

    if callback.data == "okey_en":
        profile_image(callback.from_user.id,
                      connect_DB().get_data_reg_by_user_id(callback.from_user.id),
                      connect_DB().count_referal(callback.from_user.id),
                      connect_DB().get_count_klen_by_user_id(callback.from_user.id),
                      connect_DB().get_count_ecoin_by_user_id(callback.from_user.id),
                      connect_DB().get_count_derevo_by_user_id(callback.from_user.id),
                      connect_DB().get_count_utka_by_user_id(callback.from_user.id),
                      connect_DB().get_count_shariki_by_user_id(callback.from_user.id),
                      connect_DB().get_count_metla_by_user_id(callback.from_user.id),
                      connect_DB().get_count_jet_by_user_id(callback.from_user.id),
                      connect_DB().get_count_shapka_by_user_id(callback.from_user.id),
                      connect_DB().get_count_zont_by_user_id(callback.from_user.id),
                      connect_DB().get_lang_by_user_id(callback.from_user.id))

        photo = FSInputFile(f"image_profile/{callback.from_user.id}.jpg")
        connector = get_connector(callback.from_user.id)
        connected = await connector.restore_connection()

        await bot.send_photo(callback.message.chat.id, photo=photo,
                             reply_markup=my_profile_en(connected))
        await callback.message.delete()

    if callback.data == "start_game_button":
        pass


    if callback.data == "start_game_button_en":
        await bot.answer_callback_query(callback.id, 'The game is in development', show_alert=True)
        await bot.answer_callback_query(callback.id)

    if callback.data == "my_profile_button":
        await bot.answer_callback_query(callback.id, '"Мой профиль" станет доступен,\n'
                                                     'после выхода игры', show_alert=True)
        await bot.answer_callback_query(callback.id)

    if callback.data == "my_profile_button_en":
        await bot.answer_callback_query(callback.id, '"My profile" will be available,\n'
                                                     'after the game is released', show_alert=True)
        await bot.answer_callback_query(callback.id)

    if callback.data == "referal_sustem_button":
        count_referal = connect_DB().count_referal(callback.from_user.id)
        photo = FSInputFile(f"image/referal_image.png")

        await bot.send_photo(callback.message.chat.id, photo=photo, reply_markup=referal_sustem_buttoms())
        await callback.message.delete()
    if callback.data == "referal_sustem_button_en":
        count_referal = connect_DB().count_referal(callback.from_user.id)
        photo = FSInputFile(f"image/referal_image.png")

        await bot.send_photo(callback.message.chat.id, photo=photo, reply_markup=referal_sustem_buttoms_en())
        await callback.message.delete()

    if callback.data == "zadania_ru":
        photo = FSInputFile(f"image/zadania_button.gif")
        user_boost =  await bot.get_user_chat_boosts(chat_id='@Hoary_Efim_Group', user_id=callback.from_user.id)
        for i in range(len(user_boost.boosts)):
            boosts_id =  connect_DB_boost().get_boost(user_boost.boosts[i].boost_id)
            if boosts_id == False:
                connect_DB_boost().add_boost_id(user_boost.boosts[i].boost_id,user_boost.boosts[i].source.user.id, False)






        #boost_id= ch_b[0].source.user.id


        await bot.send_animation(callback.message.chat.id, animation=photo, reply_markup=zadania_ru(boost_status=None))
        await callback.message.delete()
    if callback.data == "zadania_en":
        photo = FSInputFile(f"image/zadania_button.gif")
        user_boost = await bot.get_user_chat_boosts(chat_id='@Hoary_Efim_Group', user_id=callback.from_user.id)
        for i in range(len(user_boost.boosts)):
            boosts_id = connect_DB_boost().get_boost(user_boost.boosts[i].boost_id)
            if boosts_id == False:
                connect_DB_boost().add_boost_id(user_boost.boosts[i].boost_id, user_boost.boosts[i].source.user.id,
                                                False)

        # boost_id= ch_b[0].source.user.id

        await bot.send_animation(callback.message.chat.id, animation=photo, reply_markup=zadania_en(boost_status=None))
        await callback.message.delete()

    if callback.data == "connect_wallet_ru":
        # await callback.answer()
        # message = callback.message
        # data = callback.data
        #
        # data = data.split(':')
        # if data[0] == 'connect':
        #     await connect_wallet(message, data[1])
        #     print(message, data[1])

        count_referal = connect_DB().count_referal(callback.from_user.id)
        photo = FSInputFile(f"image/wallets.png")

        chat_id = callback.from_user.id
        connector = get_connector(chat_id)
        connected = await connector.restore_connection()

        mk_b = InlineKeyboardBuilder()
        if connected:
            mk_b.button(text='Send Transaction', callback_data='send_tr')
            mk_b.button(text='Disconnect', callback_data='disconnect')
            #await message.answer(text='You are already connected!', reply_markup=mk_b.as_markup())

        else:
            wallets_list = TonConnect.get_wallets()
            for wallet in wallets_list:
                mk_b.button(text=wallet['name'], callback_data=f'connect:{wallet["name"]}')
            mk_b.adjust(1, )
            #await message.answer(text='Какой кошелёк подключить?', reply_markup=mk_b.as_markup())

        await bot.send_photo(callback.message.chat.id, photo=photo, reply_markup=mk_b.as_markup())
        await callback.message.delete()

    if callback.data == "connect:Wallet":
        await callback.answer()
        message = callback.message
        data = callback.data

        data = data.split(':')
        if data[0] == 'connect':
            await connect_wallet(message, data[1])
            print(message, data[1])

    if callback.data == "connect:Tonkeeper":
        await callback.answer()
        message = callback.message
        data = callback.data

        data = data.split(':')
        if data[0] == 'connect':
            await connect_wallet(message, data[1],lang=connect_DB().get_lang_by_user_id(callback.from_user.id))
            print(message, data[1])


    if callback.data == "connect:MyTonWallet":
        await callback.answer()
        message = callback.message
        data = callback.data

        data = data.split(':')
        if data[0] == 'connect':
            await connect_wallet(message, data[1])
            print(message, data[1])

    if callback.data == "connect:Tonhub":
        await callback.answer()
        message = callback.message
        data = callback.data

        data = data.split(':')
        if data[0] == 'connect':
            await connect_wallet(message, data[1])
            print(message, data[1])

    if callback.data == "connect:DeWallet":
        await callback.answer()
        message = callback.message
        data = callback.data

        data = data.split(':')
        if data[0] == 'connect':
            await connect_wallet(message, data[1])
            print(message, data[1])

    if callback.data == "connect:Bitget Wallet":
        await callback.answer()
        message = callback.message
        data = callback.data

        data = data.split(':')
        if data[0] == 'connect':
            await connect_wallet(message, data[1])
            print(message, data[1])






    if callback.data == "connect_wallet_en":
        count_referal = connect_DB().count_referal(callback.from_user.id)
        photo = FSInputFile(f"image/wallets.png")

        chat_id = callback.from_user.id
        connector = get_connector(chat_id)
        connected = await connector.restore_connection()

        mk_b = InlineKeyboardBuilder()
        if connected:
            mk_b.button(text='Send Transaction', callback_data='send_tr')
            mk_b.button(text='Disconnect', callback_data='disconnect')
            # await message.answer(text='You are already connected!', reply_markup=mk_b.as_markup())

        else:
            wallets_list = TonConnect.get_wallets()
            for wallet in wallets_list:
                mk_b.button(text=wallet['name'], callback_data=f'connect:{wallet["name"]}')
            mk_b.adjust(1, )
            # await message.answer(text='Какой кошелёк подключить?', reply_markup=mk_b.as_markup())

        await bot.send_photo(callback.message.chat.id, photo=photo, reply_markup=mk_b.as_markup())
        await callback.message.delete()

    if callback.data == "create_referal_link":
        await callback.message.delete()
        adite = await callback.message.answer(text="Подождите,идёт генерация вашей ссылки")
        await asyncio.sleep(0.5)
        https1 = await bot.edit_message_text('https:', chat_id=callback.from_user.id, message_id=adite.message_id)
        await asyncio.sleep(0.5)
        https2 = await bot.edit_message_text('https://t.me:', chat_id=callback.from_user.id, message_id=https1.message_id)
        await asyncio.sleep(0.5)
        https3 = await bot.edit_message_text('https://t.me/Hoary', chat_id=callback.from_user.id, message_id=https2.message_id)
        await asyncio.sleep(0.5)
        https4 = await bot.edit_message_text('https://t.me/Hoary_Efim_bot', chat_id=callback.from_user.id, message_id=https3.message_id)
        await asyncio.sleep(0.5)
        https5 = await bot.edit_message_text('https://t.me/Hoary_Efim_bot?start=', chat_id=callback.from_user.id, message_id=https4.message_id)
        await asyncio.sleep(0.5)
        https6 = await bot.edit_message_text(f'https://t.me/Hoary_Efim_bot?start={callback.from_user.id}',
                                             chat_id=callback.from_user.id, message_id=https5.message_id)
        await asyncio.sleep(0.5)
        https7 = await bot.edit_message_text(chat_id=callback.from_user.id, message_id=https6.message_id,
                                             text=f"Готово!\n"
                                                  f"Ваша реферальная ссылка:\n"
                                                  f"<tg-spoiler>https://t.me/Hoary_Efim_bot?start={callback.from_user.id}</tg-spoiler>",
                                             parse_mode="HTML", reply_markup=referal_button())

    if callback.data == "create_referal_link_en":
        await callback.message.delete()
        adite = await callback.message.answer(text="Wait, your link is being generated")
        await asyncio.sleep(0.5)
        https1 = await bot.edit_message_text('https:', chat_id=callback.from_user.id, message_id=adite.message_id)
        await asyncio.sleep(0.5)
        https2 = await bot.edit_message_text('https://t.me:', chat_id=callback.from_user.id, message_id=https1.message_id)
        await asyncio.sleep(0.5)
        https3 = await bot.edit_message_text('https://t.me/Hoary', chat_id=callback.from_user.id, message_id=https2.message_id)
        await asyncio.sleep(0.5)
        https4 = await bot.edit_message_text('https://t.me/Hoary_Efim_bot', chat_id=callback.from_user.id, message_id=https3.message_id)
        await asyncio.sleep(0.5)
        https5 = await bot.edit_message_text('https://t.me/Hoary_Efim_bot?start=', chat_id=callback.from_user.id, message_id=https4.message_id)
        await asyncio.sleep(0.5)
        https6 = await bot.edit_message_text(f'https://t.me/Hoary_Efim_bot?start={callback.from_user.id}',
                                             chat_id=callback.from_user.id, message_id=https5.message_id)
        await asyncio.sleep(0.5)
        https7 = await bot.edit_message_text(chat_id=callback.from_user.id, message_id=https6.message_id,
                                             text=f"Done!\n"
                                                  f"Your referral link:\n"
                                                  f"<tg-spoiler>https://t.me/Hoary_Efim_bot?start={callback.from_user.id}</tg-spoiler>",
                                             parse_mode="HTML", reply_markup=referal_button_en())

    if callback.data == "kak_polushit_bolee":
        user_channel_status = await bot.get_chat_member(chat_id='@Hoary_Efim_Group', user_id=callback.from_user.id)
        print(user_channel_status)

        if user_channel_status.status != 'left':
            await callback.answer("Вы являетесь подписчиком нашего канала.\n"
                                  "У вас максимальный бонус")
        else:
            await bot.answer_callback_query(callback.id, f"Что-бы получить больше бонусов,\n"
                                                         "подпишитесь на нашу группу\n", show_alert=True)

    if callback.data == "kak_polushit_bolee_en":
        user_channel_status = await bot.get_chat_member(chat_id='@Hoary_Efim_Group', user_id=callback.from_user.id)
        print(user_channel_status)

        if user_channel_status.status != 'left':
            await callback.answer("You are a subscriber to our channel.\n"
                                  "You have the maximum bonus")
        else:
            await bot.answer_callback_query(callback.id, f"To get more bonuses,\n"
                                                         "subscribe to our group\n", show_alert=True)

    if callback.data == "information_buttom":
        photo = FSInputFile(f"image/information.jpg")
        await bot.send_photo(callback.message.chat.id, photo=photo, reply_markup=ecoin_info())
        await callback.message.delete()

    if callback.data == "information_buttom_en":
        photo = FSInputFile(f"image/information.jpg")
        await bot.send_photo(callback.message.chat.id, photo=photo, reply_markup=ecoin_info_en())
        await callback.message.delete()

    if callback.data == "contact_buttom":
        photo = FSInputFile(f"image/contact.jpg")
        await bot.send_photo(callback.message.chat.id, photo=photo, reply_markup=contackt_buttoms())
        await callback.message.delete()

    if callback.data == "contact_buttom_en":
        photo = FSInputFile(f"image/contact.jpg")
        await bot.send_photo(callback.message.chat.id, photo=photo, reply_markup=contackt_buttoms_en())
        await callback.message.delete()

    if callback.data == "partners_buttom":
        photo = FSInputFile(f"image/partners.jpg")
        await bot.send_photo(callback.message.chat.id, photo=photo, reply_markup=partners_buttoms())
        await callback.message.delete()

    if callback.data == "partners_buttom_en":
        photo = FSInputFile(f"image/partners.jpg")
        await bot.send_photo(callback.message.chat.id, photo=photo, reply_markup=partners_buttoms_en())
        await callback.message.delete()

    if callback.data == "My_profile":
        profile_image(callback.from_user.id,
                      connect_DB().get_data_reg_by_user_id(callback.from_user.id),
                      connect_DB().count_referal(callback.from_user.id),
                      connect_DB().get_count_klen_by_user_id(callback.from_user.id),
                      connect_DB().get_count_ecoin_by_user_id(callback.from_user.id),
                      connect_DB().get_count_derevo_by_user_id(callback.from_user.id),
                      connect_DB().get_count_utka_by_user_id(callback.from_user.id),
                      connect_DB().get_count_shariki_by_user_id(callback.from_user.id),
                      connect_DB().get_count_metla_by_user_id(callback.from_user.id),
                      connect_DB().get_count_jet_by_user_id(callback.from_user.id),
                      connect_DB().get_count_shapka_by_user_id(callback.from_user.id),
                      connect_DB().get_count_zont_by_user_id(callback.from_user.id),
                      connect_DB().get_lang_by_user_id(callback.from_user.id))
        await callback.message.delete()
        photo = FSInputFile(f"image_profile/{callback.from_user.id}.jpg")
        connector = get_connector(callback.from_user.id)
        connected = await connector.restore_connection()

        await bot.send_photo(callback.message.chat.id, photo=photo, reply_markup=my_profile(connected))

    if callback.data == "My_profile_en":
        profile_image(callback.from_user.id,
                      connect_DB().get_data_reg_by_user_id(callback.from_user.id),
                      connect_DB().count_referal(callback.from_user.id),
                      connect_DB().get_count_klen_by_user_id(callback.from_user.id),
                      connect_DB().get_count_ecoin_by_user_id(callback.from_user.id),
                      connect_DB().get_count_derevo_by_user_id(callback.from_user.id),
                      connect_DB().get_count_utka_by_user_id(callback.from_user.id),
                      connect_DB().get_count_shariki_by_user_id(callback.from_user.id),
                      connect_DB().get_count_metla_by_user_id(callback.from_user.id),
                      connect_DB().get_count_jet_by_user_id(callback.from_user.id),
                      connect_DB().get_count_shapka_by_user_id(callback.from_user.id),
                      connect_DB().get_count_zont_by_user_id(callback.from_user.id),
                      connect_DB().get_lang_by_user_id(callback.from_user.id))
        await callback.message.delete()
        photo = FSInputFile(f"image_profile/{callback.from_user.id}.jpg")
        connector = get_connector(callback.from_user.id)
        connected = await connector.restore_connection()

        await bot.send_photo(callback.message.chat.id, photo=photo, reply_markup=my_profile_en(connected))

    if callback.data == "dalle_wallet":


        await bot.answer_callback_query(callback.id, f"Вы подключили кошелёк!\n{connect_DB().get_wallet_addres_by_user_id(callback.from_user.id)}",show_alert=True)
        await bot.answer_callback_query(callback.id)
        profile_image(callback.from_user.id,
                      connect_DB().get_data_reg_by_user_id(callback.from_user.id),
                      connect_DB().count_referal(callback.from_user.id),
                      connect_DB().get_count_klen_by_user_id(callback.from_user.id),
                      connect_DB().get_count_ecoin_by_user_id(callback.from_user.id),
                      connect_DB().get_count_derevo_by_user_id(callback.from_user.id),
                      connect_DB().get_count_utka_by_user_id(callback.from_user.id),
                      connect_DB().get_count_shariki_by_user_id(callback.from_user.id),
                      connect_DB().get_count_metla_by_user_id(callback.from_user.id),
                      connect_DB().get_count_jet_by_user_id(callback.from_user.id),
                      connect_DB().get_count_shapka_by_user_id(callback.from_user.id),
                      connect_DB().get_count_zont_by_user_id(callback.from_user.id),
                      connect_DB().get_lang_by_user_id(callback.from_user.id))

        photo = FSInputFile(f"image_profile/{callback.from_user.id}.jpg")
        connector = get_connector(callback.from_user.id)
        connected = await connector.restore_connection()

        await bot.send_photo(callback.message.chat.id, photo=photo,
                             reply_markup=my_profile(connected))
        await callback.message.delete()

    if callback.data == "dalle_wallet_en":


        await bot.answer_callback_query(callback.id, f"You have connected your wallet!\n{connect_DB().get_wallet_addres_by_user_id(callback.from_user.id)}",show_alert=True)
        await bot.answer_callback_query(callback.id)
        profile_image(callback.from_user.id,
                      connect_DB().get_data_reg_by_user_id(callback.from_user.id),
                      connect_DB().count_referal(callback.from_user.id),
                      connect_DB().get_count_klen_by_user_id(callback.from_user.id),
                      connect_DB().get_count_ecoin_by_user_id(callback.from_user.id),
                      connect_DB().get_count_derevo_by_user_id(callback.from_user.id),
                      connect_DB().get_count_utka_by_user_id(callback.from_user.id),
                      connect_DB().get_count_shariki_by_user_id(callback.from_user.id),
                      connect_DB().get_count_metla_by_user_id(callback.from_user.id),
                      connect_DB().get_count_jet_by_user_id(callback.from_user.id),
                      connect_DB().get_count_shapka_by_user_id(callback.from_user.id),
                      connect_DB().get_count_zont_by_user_id(callback.from_user.id),
                      connect_DB().get_lang_by_user_id(callback.from_user.id))

        photo = FSInputFile(f"image_profile/{callback.from_user.id}.jpg")
        connector = get_connector(callback.from_user.id)
        connected = await connector.restore_connection()

        await bot.send_photo(callback.message.chat.id, photo=photo,
                             reply_markup=my_profile_en(connected))
        await callback.message.delete()

    if callback.data == "channel_boost":
        photo = FSInputFile(f"image/boost_chanel.mp4")
        await bot.send_animation(callback.message.chat.id, animation=photo, reply_markup=chanel_boost())
        await callback.message.delete()
    if callback.data == "channel_boost_en":
        photo = FSInputFile(f"image/boost_chanel.mp4")
        await bot.send_animation(callback.message.chat.id, animation=photo, reply_markup=chanel_boost_en())
        await callback.message.delete()
    if callback.data == "shop":
        await bot.answer_callback_query(callback.id, 'Магазин будет доступен чуть позже.\n',show_alert=True)
        await bot.answer_callback_query(callback.id)
    if callback.data == "shop_en":
        await bot.answer_callback_query(callback.id, 'The store will be available later.\n', show_alert=True)
        await bot.answer_callback_query(callback.id)
    if callback.data == "chek_boost":
        klens = 0
        user_boost = await bot.get_user_chat_boosts(chat_id='@Hoary_Efim_Group', user_id=callback.from_user.id)
        for i in range(len(user_boost.boosts)):
            boosts_id = connect_DB_boost().get_boost(user_boost.boosts[i].boost_id)
            if boosts_id == False:
                connect_DB_boost().add_boost_id(user_boost.boosts[i].boost_id, user_boost.boosts[i].source.user.id,
                                                False)
            nagrada = (connect_DB_boost().get_nagrada(user_boost.boosts[i].boost_id))
            if nagrada == "False":
                klen = connect_DB().get_count_klen_by_user_id(callback.from_user.id)
                connect_DB().add_klen_by_id(klen + 25,callback.from_user.id)
                connect_DB_boost().add_nagrada('True',user_boost.boosts[i].boost_id)
                klens+=25
        if klens !=0:
            await bot.answer_callback_query(callback.id, 'Поздравляем!,\n'
                                                         f'За буст нашего канала,вам добавлено: {klens} KLEN', show_alert=True)
            await bot.answer_callback_query(callback.id)
        if klens == 0:
            await bot.answer_callback_query(callback.id, 'Увы!,\n'
                                                         f'Пока новых голосов у вас нет!',
                                            show_alert=True)
            await bot.answer_callback_query(callback.id)

    if callback.data == "chek_boost_en":
        klens = 0
        user_boost = await bot.get_user_chat_boosts(chat_id='@Hoary_Efim_Group', user_id=callback.from_user.id)
        for i in range(len(user_boost.boosts)):
            boosts_id = connect_DB_boost().get_boost(user_boost.boosts[i].boost_id)
            if boosts_id == False:
                connect_DB_boost().add_boost_id(user_boost.boosts[i].boost_id, user_boost.boosts[i].source.user.id,
                                                False)
            nagrada = (connect_DB_boost().get_nagrada(user_boost.boosts[i].boost_id))
            if nagrada == "False":
                klen = connect_DB().get_count_klen_by_user_id(callback.from_user.id)
                connect_DB().add_klen_by_id(klen + 25,callback.from_user.id)
                connect_DB_boost().add_nagrada('True',user_boost.boosts[i].boost_id)
                klens+=25
        if klens !=0:
            await bot.answer_callback_query(callback.id, 'Congratulations!,\n'
                                                         f'For the boost of our channel, you have been added: {klens} KLEN', show_alert=True)
            await bot.answer_callback_query(callback.id)
        if klens == 0:
            await bot.answer_callback_query(callback.id, 'Alas!,\n'
                                                         f"You don't have any new voices yet!",
                                            show_alert=True)
            await bot.answer_callback_query(callback.id)
    if callback.data == "podpiska_na_parters":
        await bot.answer_callback_query(callback.id, 'Этот бонус пока не доступен.\n',show_alert=True)
        await bot.answer_callback_query(callback.id)
    if callback.data == "podpiska_na_parters_en":
        await bot.answer_callback_query(callback.id, 'This bonus is not available yet.\n',show_alert=True)
        await bot.answer_callback_query(callback.id)










###################################################################################################3
@dp.message(Command('klen'))
async def kleny(message: Message, state: FSMContext) -> None:
    if message.from_user.id == 6242910839 or message.from_user.id == 1048061854 or message.from_user.id == 977457213:
        mess = await message.answer('Кому отрправить klen?\n'
                                    'Если начисляете по username,\n'
                                    'то без @')
        await state.set_state(klen.username)
        await asyncio.sleep(10)
        await bot.delete_message(message.from_user.id, mess.message_id)
@dp.message(klen.username)
async def process_username(message: Message, state: FSMContext) -> None:
    username = message.text
    serch = connect_DB().user_name(message.text)
    global plzovatel
    plzovatel = True
    #print(serch)

    if serch == False:
        serch = connect_DB().users_id(message.text)
        if bool(serch) == False:
            await state.clear()
            mess = await message.answer('Такого пользователя нет')
            await asyncio.sleep(10)
            await bot.delete_message(message.from_user.id, mess.message_id)
            plzovatel = False
    #print(bool(serch))
    if plzovatel != False:
        await state.update_data(username=username)
        await state.set_state(klen.count)
        mess = await message.answer(f'Такой пользователь есть.\n'
                                    'Сколько начислить klen?')

        await asyncio.sleep(10)
        await bot.delete_message(message.from_user.id, mess.message_id)
@dp.message(klen.count)
async def process_count(message: Message, state: FSMContext) -> None:
    count = message.text
    await state.update_data(count=count)
    await state.set_state(klen.count)
    current_state = await state.get_data()
    #current_state = int(current_state['count'])
    try:
        username_get = connect_DB().user_name(current_state['username'])
        print(username_get)
        if username_get == False:
            user_id_get = connect_DB().get_count_klen_by_user_id(current_state['username'])
            upp = int(user_id_get) + int(current_state['count'])
            connect_DB().add_klen_by_id(upp, current_state['username'])
            try:
                coin = current_state["username"]
                coin1 = current_state['count']
                mess = await message.answer(f'Готово! Пользователю  {coin} начислено: {coin1}')


            except:
                pass

        if username_get == True:
            user_id_get = connect_DB().get_count_klen_by_user_name(current_state['username'])
            upp = int(user_id_get) + int(current_state['count'])
            connect_DB().add_klen_by_user_name(upp, current_state['username'])
            user_id_get = connect_DB().get_count_klen_by_user_name(current_state['username'])
            try:
                coin = current_state["username"]
                coin1 = current_state['count']
                mess = await message.answer(f'Готово! Пользователю  {coin} начислено: {coin1}\n')



            except:
                pass


    except:
        mess = await message.answer("Что-то пошло не так")
        await asyncio.sleep(5)
        await bot.delete_message(message.from_user.id, mess.message_id)
#####################################################################################################
#########################################################################################################
@dp.message(Command('ecoin'))
async def ecoiny(message: Message, state: FSMContext) -> None:
    if message.from_user.id == 6242910839 or message.from_user.id == 1048061854 or message.from_user.id == 977457213:
        mess = await message.answer('Кому отрправить ecoin?\n'
                                    'Если начисляете по username,\n'
                                    'то без @')
        await state.set_state(ecoin.username)
        await asyncio.sleep(10)
        await bot.delete_message(message.from_user.id, mess.message_id)
@dp.message(ecoin.username)
async def process_username(message: Message, state: FSMContext) -> None:
    username = message.text
    serch = connect_DB().user_name(message.text)
    global plzovatel1
    plzovatel1 = True
    #print(serch)

    if serch == False:
        serch = connect_DB().users_id(message.text)
        if bool(serch) == False:
            await state.clear()
            mess = await message.answer('Такого пользователя нет')
            await asyncio.sleep(10)
            await bot.delete_message(message.from_user.id, mess.message_id)
            plzovatel1 = False

    if plzovatel1 != False:
        await state.update_data(username=username)
        await state.set_state(ecoin.count)
        mess = await message.answer(f'Такой пользователь есть.\n'
                                    'Сколько начислить ecoin?')

        await asyncio.sleep(10)
        await bot.delete_message(message.from_user.id, mess.message_id)
@dp.message(ecoin.count)
async def process_count(message: Message, state: FSMContext) -> None:
    count = message.text
    await state.update_data(count=count)
    await state.set_state(ecoin.count)
    current_state = await state.get_data()

    try:
        username_get = connect_DB().user_name(current_state['username'])
        print(username_get)
        if username_get == False:
            user_id_get = connect_DB().get_count_ecoin_by_user_id(current_state['username'])
            print(user_id_get)
            upp = int(user_id_get) + int(current_state['count'])
            print(upp)
            connect_DB().add_ecoin_by_id(upp, current_state['username'])
            user_id_get = connect_DB().get_count_ecoin_by_user_id(current_state['username'])
            try:
                coin = current_state["username"]
                coin1 = current_state['count']
                mess = await message.answer(f'Готово! Пользователю  {coin} начислено: {coin1}')


            except:
                pass

        if username_get == True:
            user_id_get = connect_DB().get_count_ecoin_by_user_name(current_state['username'])
            print("1")
            upp = int(user_id_get) + int(current_state['count'])
            print("2")
            connect_DB().add_ecoin_by_user_name(upp, current_state['username'])
            print("3")
            user_id_get = connect_DB().get_count_ecoin_by_user_name(current_state['username'])
            print("4")
            try:
                coin = current_state["username"]
                coin1 = current_state['count']
                mess = await message.answer(f'Готово! Пользователю  {coin} начислено: {coin1}\nБаланс пользователя  {user_id_get} ecoin')



            except:
                pass


    except:
        mess = await message.answer("Что-то пошло не так")
        await asyncio.sleep(5)
        await bot.delete_message(message.from_user.id, mess.message_id)
#########################################################################################################
########################################################################################################
@dp.message(Command('profil'))
async def prof(message: Message, state: FSMContext) -> None:
    if message.from_user.id == 6242910839 or message.from_user.id == 1048061854 or message.from_user.id == 977457213:
        mess = await message.answer('Чей профиль показать?')
        await state.set_state(profil.username)
        await asyncio.sleep(10)
        await bot.delete_message(message.from_user.id, mess.message_id)
@dp.message(profil.username)
async def process_username(message: Message, state: FSMContext) -> None:
    username = message.text
    serch = connect_DB().user_name(message.text)

    global plzovatel1
    plzovatel1 = True
    #print(serch)

    if serch == False:
        serch = connect_DB().users_id(message.text)

        await state.update_data(username=username)
        mess = await message.answer(f'Пользователь {username}.\n'
                                    f'ID юзера: {username} \n'
                                    f'UserName: {connect_DB().get_username_by_user_id(username)}\n'
                                    f'Язык: {connect_DB().get_lang_by_user_id(username)}\n'
                                    f'Кошелёк: {connect_DB().get_wallet_addres_by_user_id(username)}\n'
                                    f'Дата регистрации: {connect_DB().get_data_reg_by_user_id(username)}\n'
                                    f'Реферал: {connect_DB().get_ref_by_user_id(username)}\n'
                                    f'Количество ecoin: {connect_DB().get_count_ecoin_by_user_id(username)}\n'
                                    f'Количество дерева: {connect_DB().get_count_derevo_by_user_id(username)}\n'
                                    f'Количество клен: {connect_DB().get_count_klen_by_user_id(username)}\n'
                                    f'Количество вып.заданий: {connect_DB().get_count_s_zad_by_user_id(username)}\n'
                                    f'Полётов на метле: {connect_DB().get_count_metla_by_user_id(username)}\n'
                                    f'Полётов на шапке: {connect_DB().get_count_shapka_by_user_id(username)}\n'
                                    f'Полётов на шариках: {connect_DB().get_count_shariki_by_user_id(username)}'
                                    f'Полётов на ранце: {connect_DB().get_count_jet_by_user_id(username)}\n'
                                    f'Полётов на утке: {connect_DB().get_count_utka_by_user_id(username)}\n'
                                    f'Полётов на зонтике: {connect_DB().get_count_zont_by_user_id(username)}\n'
                                    f'Количество игр: {connect_DB().get_count_game_by_user_id(username)}\n'
                                    f'Супер-топор: {connect_DB().get_s_axe_by_user_id(username)}\n'
                                    f'Бензопила: {connect_DB().get_benzo_by_user_id(username)}\n'
                                    f'Энергетик: {connect_DB().get_energy_by_user_id(username)}\n')
        plzovatel1 = False

        if bool(serch) == False:
            await state.clear()
            mess = await message.answer('Такого пользователя нет')
            await asyncio.sleep(10)
            await bot.delete_message(message.from_user.id, mess.message_id)
            plzovatel1 = False

    if plzovatel1 != False:
        await state.update_data(username=username)
        mess = await message.answer(f'Пользователь {username}.\n'
                                    f'ID юзера: {connect_DB().get_user_id_by_user_name(username)} \n'
                                    f'UserName: {username}\n'
                                    f'Язык: {connect_DB().get_lang_by_user_name(username)}\n'
                                    f'Кошелёк: {connect_DB().get_wallet_addres_by_user_name(username)}\n'
                                    f'Дата регистрации: {connect_DB().get_data_reg_by_user_name(username)}\n'
                                    f'Реферал: {connect_DB().get_ref_by_user_name(username)}\n'
                                    f'Количество ecoin: {connect_DB().get_count_ecoin_by_user_name(username)}\n'
                                    f'Количество дерева: {connect_DB().get_count_derevo_by_user_name(username)}\n'
                                    f'Количество клен: {connect_DB().get_count_klen_by_user_name(username)}\n'
                                    f'Количество вып.заданий: {connect_DB().get_count_s_zad_by_user_name(username)}\n'
                                    f'Полётов на метле: {connect_DB().get_count_metla_by_user_name(username)}\n'
                                    f'Полётов на шапке: {connect_DB().get_count_shapka_by_user_name(username)}\n'
                                    f'Полётов на шариках: {connect_DB().get_count_shariki_by_user_name(username)}\n'
                                    f'Полётов на ранце: {connect_DB().get_count_jet_by_user_name(username)}\n'
                                    f'Полётов на утке: {connect_DB().get_count_utka_by_user_name(username)}\n'
                                    f'Полётов на зонтике: {connect_DB().get_count_zont_by_user_name(username)}\n'
                                    f'Количество игр: {connect_DB().get_count_game_by_user_name(username)}\n'
                                    f'Супер-топор: {connect_DB().get_s_axe_by_user_name(username)}\n'
                                    f'Бензопила: {connect_DB().get_benzo_by_user_name(username)}\n'
                                    f'Энергетик: {connect_DB().get_energy_by_user_name(username)}\n')


#########################################################################################################
def zadania_ru(boost_status):
    buttons = [
        [
            types.InlineKeyboardButton(text='Буст канала (+25 KLEN)', callback_data='channel_boost'),

        ],
        [
            types.InlineKeyboardButton(text='Подписка на наших партнеров(+10 KLEN)', callback_data='podpiska_na_parters'),

        ],
        [
            types.InlineKeyboardButton(text='Назад', callback_data="My_profile"),

        ]

    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
def zadania_en(boost_status):
    buttons = [
        [
            types.InlineKeyboardButton(text='Channel Boost (+25 KLEN)', callback_data='channel_boost_en'),

        ],
        [
            types.InlineKeyboardButton(text='Subscribe to our partners(+10 KLEN)',
                                       callback_data='podpiska_na_parters_en'),

        ],
        [
            types.InlineKeyboardButton(text='Back', callback_data="My_profile_en"),

        ]

    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def chanel_boost():
    buttons = [
        [
            types.InlineKeyboardButton(text='Забустить',url="https://t.me/boost/Hoary_Efim_Group"),

        ],
        [
            types.InlineKeyboardButton(text='Проверить', callback_data='chek_boost'),

        ],
        [
            types.InlineKeyboardButton(text='Назад', callback_data='zadania_ru'),

        ]

    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
def chanel_boost_en():
    buttons = [
        [
            types.InlineKeyboardButton(text='To run',url="https://t.me/boost/Hoary_Efim_Group"),

        ],
        [
            types.InlineKeyboardButton(text='Check', callback_data='chek_boost_en'),

        ],
        [
            types.InlineKeyboardButton(text='Back', callback_data='zadania_en'),

        ]

    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
########################################################################################################
def select_language():
    buttons = [
        [
            types.InlineKeyboardButton(text='English 🇺🇸', callback_data='en_buttom'),
            types.InlineKeyboardButton(text='Русский 🇷🇺', callback_data='ru_buttom')

        ]

    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
def okey_en():
    buttons = [
        [
            types.InlineKeyboardButton(text='Great', callback_data='okey_en'),

        ]

    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
def okey():
    buttons = [
        [
            types.InlineKeyboardButton(text='Отлично', callback_data='okey'),

        ]

    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
def my_profile(connect):
    off_connected = [
        [
            types.InlineKeyboardButton(text='Начать игру', web_app=(WebAppInfo(url="https://hoary-efim.ru/")))

        ],
        [
            types.InlineKeyboardButton(text='Мой профиль', callback_data='my_profile_button'),

        ],
        [
            types.InlineKeyboardButton(text='Подключить кошелёк', callback_data='connect_wallet_ru'),

        ],
        [
            types.InlineKeyboardButton(text='Задания', callback_data='zadania_ru'),

        ],
        [
            types.InlineKeyboardButton(text='Реферальная система', callback_data='referal_sustem_button'),

        ],
        [
            types.InlineKeyboardButton(text='Информация', callback_data='information_buttom'),
            types.InlineKeyboardButton(text='Обновить', callback_data='My_profile')

        ]

    ]
    on_connected = [
        [
            types.InlineKeyboardButton(text='Начать игру', web_app=(WebAppInfo(url="https://hoary-efim.ru/")))

        ],
        [
            types.InlineKeyboardButton(text='Мой профиль', callback_data='my_profile_button'),

        ],
        [
            types.InlineKeyboardButton(text='Задания', callback_data='zadania_ru'),

        ],
        [
            types.InlineKeyboardButton(text='Реферальная система', callback_data='referal_sustem_button'),

        ],
        [
            types.InlineKeyboardButton(text='Магазин', callback_data='shop'),

        ],
        [
            types.InlineKeyboardButton(text='Информация', callback_data='information_buttom'),
            types.InlineKeyboardButton(text='Обновить', callback_data='My_profile')

        ]

    ]
    if connect == True:
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=on_connected)
        return keyboard
    elif connect == False:
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=off_connected)
        return keyboard

def my_profile_en(connect):
    off_connected = [
        [
            types.InlineKeyboardButton(text='Start the game',
                                       web_app=(WebAppInfo(url="https://hoary-efim.ru/")))

        ],
        [
            types.InlineKeyboardButton(text='My profile', callback_data='my_profile_button_en'),

        ],
        [
            types.InlineKeyboardButton(text='Connect wallet', callback_data='connect_wallet_en'),

        ],
        [
            types.InlineKeyboardButton(text='Tasks', callback_data='zadania_en'),

        ],
        [
            types.InlineKeyboardButton(text='Referral system', callback_data='referal_sustem_button_en'),

        ],
        [
            types.InlineKeyboardButton(text='Information', callback_data='information_buttom_en'),
            types.InlineKeyboardButton(text='Update', callback_data='My_profile_en')

        ]

    ]
    on_connected = [
        [
            types.InlineKeyboardButton(text='Start the game', web_app=(WebAppInfo(url="https://hoary-efim.ru/")))

        ],
        [
            types.InlineKeyboardButton(text='My profile', callback_data='my_profile_button_en'),

        ],
        [
            types.InlineKeyboardButton(text='Tasks', callback_data='zadania_en'),

        ],
        [
            types.InlineKeyboardButton(text='Referral system', callback_data='referal_sustem_button_en'),

        ],
        [
            types.InlineKeyboardButton(text='Shop', callback_data='shop_en'),

        ],
        [
            types.InlineKeyboardButton(text='Information', callback_data='information_buttom_en'),
            types.InlineKeyboardButton(text='Update', callback_data='My_profile_en')

        ]

    ]
    if connect == True:
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=on_connected)
        return keyboard
    elif connect == False:
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=off_connected)
        return keyboard
def referal_sustem_buttoms():
    buttons = [
        [
            types.InlineKeyboardButton(text='Информация о реферальной системе',url='https://telegra.ph/Referalnaya-sistema-06-10-6'),

        ],
        [
            types.InlineKeyboardButton(text='Создать реферальную ссылку', callback_data='create_referal_link')
        ],
        [
            types.InlineKeyboardButton(text='Назад', callback_data='okey')
        ]


    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
def referal_sustem_buttoms_en():
    buttons = [
        [
            types.InlineKeyboardButton(text='Information about the referral system',url='https://telegra.ph/Referral-system-06-11')

        ],
        [
            types.InlineKeyboardButton(text='Create a referral link', callback_data='create_referal_link_en')
        ],
        [
            types.InlineKeyboardButton(text='Back', callback_data='okey_en')
        ]


    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
def referal_button():
    buttons = [
        [
            types.InlineKeyboardButton(text='Назад', callback_data='referal_sustem_button'),
            types.InlineKeyboardButton(text='Получить больше Листиков', callback_data='kak_polushit_bolee')
        ]

    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
def referal_button_en():
    buttons = [
        [
            types.InlineKeyboardButton(text='Back', callback_data='referal_sustem_button_en'),
            types.InlineKeyboardButton(text='Get More leaves', callback_data='kak_polushit_bolee_en')
        ]

    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
def ecoin_info():
    buttons = [
        [
            types.InlineKeyboardButton(text='Информация о Ecoin',url='https://telegra.ph/E-coin-CHto-ehto-za-token-i-dlya-chego-on-nuzhen-06-10')
        ],

        # [
        #     types.InlineKeyboardButton(text='Информация о бустерах',url='https://telegra.ph/Magazin-busterov-06-10')
        #
        # ],
        [
            types.InlineKeyboardButton(text='Наши контакты', callback_data='contact_buttom'),
            types.InlineKeyboardButton(text='Наши партнёры', callback_data='partners_buttom')

        ],
        [
            types.InlineKeyboardButton(text='Назад',callback_data='okey')

        ],

    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
def ecoin_info_en():
    buttons = [
        [
            types.InlineKeyboardButton(text='Information about Ecoin',url='https://telegra.ph/E-coin-What-is-this-token-and-what-is-it-for-06-11')
        ],

        # [
        #     types.InlineKeyboardButton(text='Information about boosters',url='https://telegra.ph/Booster-shop-06-11')
        #
        # ],
        [
            types.InlineKeyboardButton(text='Our contacts', callback_data='contact_buttom_en'),
            types.InlineKeyboardButton(text='Our partners', callback_data='partners_buttom_en')

        ],
        [
            types.InlineKeyboardButton(text='Back',callback_data='okey_en')

        ],

    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
def contackt_buttoms():
    buttons = [
        [
            types.InlineKeyboardButton(text='PR MANAGER',url='https://t.me/PR_Hoary_Efim'),
            types.InlineKeyboardButton(text='MARKET MAKER',url='https://t.me/gororeldag'),
        ],
        [
            types.InlineKeyboardButton(text='Наш канал', url='https://t.me/Hoary_Efim_Group')
        ],
        [
            types.InlineKeyboardButton(text='Назад', callback_data='information_buttom')
        ]


    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
def contackt_buttoms_en():
    buttons = [
        [
            types.InlineKeyboardButton(text='PR MANAGER',url='https://t.me/PR_Hoary_Efim'),
            types.InlineKeyboardButton(text='MARKET MAKER',url='https://t.me/gororeldag'),
        ],
        [
            types.InlineKeyboardButton(text='Our channel', url='https://t.me/Hoary_Efim_Group')
        ],
        [
            types.InlineKeyboardButton(text='Back', callback_data='information_buttom_en')
        ]


    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
def partners_buttoms():
    buttons = [
        [
            types.InlineKeyboardButton(text='Keep Signals',url='https://t.me/keepsignals'),
            types.InlineKeyboardButton(text='TON MOON 🚀🌒',url='https://t.me/ton1moon')
        ],
        [
            types.InlineKeyboardButton(text='Бабки, дропы, два битка', url='https://t.me/Drop_NFT_Farm'),
            types.InlineKeyboardButton(text='Дьявольская Ферма💢', url='https://t.me/devilferm')
        ],
        [
            types.InlineKeyboardButton(text='TON Эликсир', url='https://t.me/TON_Elixir'),
            types.InlineKeyboardButton(text='Crypto QuickNet ⚡️', url='https://t.me/cryptoquicknetuakh')
        ],
        [
            types.InlineKeyboardButton(text='Назад', callback_data='information_buttom')
        ]


    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
def partners_buttoms_en():
    buttons = [
        [
            types.InlineKeyboardButton(text='Keep Signals',url='https://t.me/keepsignals'),
            types.InlineKeyboardButton(text='TON MOON 🚀🌒',url='https://t.me/ton1moon')
        ],
        [
            types.InlineKeyboardButton(text='Бабки, дропы, два битка', url='https://t.me/Drop_NFT_Farm'),
            types.InlineKeyboardButton(text='Дьявольская Ферма💢', url='https://t.me/devilferm')
        ],
        [
            types.InlineKeyboardButton(text='TON Эликсир', url='https://t.me/TON_Elixir'),
            types.InlineKeyboardButton(text='Crypto QuickNet ⚡️', url='https://t.me/cryptoquicknetuakh')
        ],
        [
            types.InlineKeyboardButton(text='Back', callback_data='information_buttom_en')
        ]


    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
def enter_wallet(lang):
    if lang == "RU":
        buttons = [
            [
                types.InlineKeyboardButton(text='Продолжить', callback_data="dalle_wallet")
            ]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    if lang == "EN":
        buttons = [
            [
                types.InlineKeyboardButton(text='Continue', callback_data="dalle_wallet_en")
            ]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard
def profile_image(user_id,data_reg,referal,listik,ecoin,derevo,utka,sharik,metla,ranec,shapka,zontick,language):
    print(user_id,data_reg,referal,listik,ecoin,derevo,utka,sharik,metla,ranec,shapka,zontick,language)
    if language == "RU":
        image = Image.open("image/image.jpeg")
        # Количество Ecoin
        font = ImageFont.truetype("arial.ttf", 50)
        drawer = ImageDraw.Draw(image)
        drawer.text((230, 430), f"{ecoin}", font=font, fill='black')
        # Количество дерева
        font = ImageFont.truetype("arial.ttf", 50)
        drawer = ImageDraw.Draw(image)
        drawer.text((150, 723), f"{derevo}", font=font, fill='black')
        # Количество листочков
        font = ImageFont.truetype("arial.ttf", 50)
        drawer = ImageDraw.Draw(image)
        drawer.text((350, 723), f"{listik}", font=font, fill='black')
        # Количество рефералов
        font = ImageFont.truetype("arial.ttf", 35)
        drawer = ImageDraw.Draw(image)
        drawer.text((570, 210), f"Количество рефералов:{referal} ", font=font, fill='black')
        # Дата регистрации
        font = ImageFont.truetype("arial.ttf", 35)
        drawer = ImageDraw.Draw(image)
        drawer.text((570, 540), f"Дата регистрации:  {data_reg} ", font=font, fill='black')
        # Выполненые задания
        font = ImageFont.truetype("arial.ttf", 35)
        drawer = ImageDraw.Draw(image)
        drawer.text((570, 370), "Выполненые задания:0 ", font=font, fill='black')
        image.save(f'image_profile/{user_id}.jpg')

        if metla >= 1000:
            img = Image.open(f'image_profile/{user_id}.jpg')
            watermark = Image.open('image/metlaG.png').resize((159, 159))
            img.paste(watermark, (48, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
        else:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/metlaNG.png').resize((159, 159))
            img.paste(watermark, (48, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")

        # Шапка
        if shapka >= 1000:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/shapkaG.png').resize((159, 159))
            img.paste(watermark, (252, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
        else:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/shapkaNG.png').resize((159, 159))
            img.paste(watermark, (252, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
        # Шарики
        if sharik >= 1000:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/sharikG.png').resize((159, 159))
            img.paste(watermark, (456, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
        else:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/sharikNG.png').resize((159, 159))
            img.paste(watermark, (456, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
        # Ранец
        if ranec >= 1000:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/ranecG.png').resize((159, 159))
            img.paste(watermark, (660, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
        else:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/ranecNG.png').resize((159, 159))
            img.paste(watermark, (660, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
        # Утка
        if utka >= 1000:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/utkaG.png').resize((159, 159))
            img.paste(watermark, (864, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
        else:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/utkaNG.png').resize((159, 159))
            img.paste(watermark, (864, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
        # Зонтик
        if zontick >= 1000:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/zontoikG.png').resize((159, 159))
            img.paste(watermark, (1070, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
        else:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/zontoikNG.png').resize((159, 159))
            img.paste(watermark, (1070, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")

    elif language == "EN":
        image = Image.open("image/image.jpeg")
        # Количество Ecoin
        font = ImageFont.truetype("arial.ttf", 50)
        drawer = ImageDraw.Draw(image)
        drawer.text((230, 430), f"{ecoin}", font=font, fill='black')
        # Количество дерева
        font = ImageFont.truetype("arial.ttf", 50)
        drawer = ImageDraw.Draw(image)
        drawer.text((150, 723), f"{derevo}", font=font, fill='black')
        # Количество листочков
        font = ImageFont.truetype("arial.ttf", 50)
        drawer = ImageDraw.Draw(image)
        drawer.text((350, 723), f"{listik}", font=font, fill='black')
        # Количество рефералов
        font = ImageFont.truetype("arial.ttf", 35)
        drawer = ImageDraw.Draw(image)
        drawer.text((570, 210), f"Number of referrals:{referal} ", font=font, fill='black')
        # Дата регистрации
        font = ImageFont.truetype("arial.ttf", 35)
        drawer = ImageDraw.Draw(image)
        drawer.text((570, 540), f"Date of registration:  {data_reg} ", font=font, fill='black')
        # Выполненые задания
        font = ImageFont.truetype("arial.ttf", 35)
        drawer = ImageDraw.Draw(image)
        drawer.text((570, 370), "Completed tasks:0 ", font=font, fill='black')
        image.save(f'image_profile/{user_id}.jpg')

        if metla >= 1000:
            img = Image.open(f'image_profile/{user_id}.jpg')
            watermark = Image.open('image/metlaG.png').resize((159, 159))
            img.paste(watermark, (48, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
        else:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/metlaNG.png').resize((159, 159))
            img.paste(watermark, (48, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")

        # Шапка
        if shapka >= 1000:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/shapkaG.png').resize((159, 159))
            img.paste(watermark, (252, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
        else:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/shapkaNG.png').resize((159, 159))
            img.paste(watermark, (252, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
        # Шарики
        if sharik >= 1000:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/sharikG.png').resize((159, 159))
            img.paste(watermark, (456, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
        else:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/sharikNG.png').resize((159, 159))
            img.paste(watermark, (456, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
        # Ранец
        if ranec >= 1000:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/ranecG.png').resize((159, 159))
            img.paste(watermark, (660, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
        else:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/ranecNG.png').resize((159, 159))
            img.paste(watermark, (660, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
        # Утка
        if utka >= 1000:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/utkaG.png').resize((159, 159))
            img.paste(watermark, (864, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
        else:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/utkaNG.png').resize((159, 159))
            img.paste(watermark, (864, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
        # Зонтик
        if zontick >= 1000:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/zontoikG.png').resize((159, 159))
            img.paste(watermark, (1070, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
        else:
            img = Image.open(f"image_profile/{user_id}.jpg")
            watermark = Image.open('image/zontoikNG.png').resize((159, 159))
            img.paste(watermark, (1070, 800), watermark)
            img.save(f"image_profile/{user_id}.jpg")
async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)
########################################################################################################################
########################################################################################################################
# .env
MANIFEST_URL='https://hankgalt1.github.io/Hoary_Efim/tonconnect-manifest.json'
########################################################################################################################
# tc_storage.py
from pytonconnect.storage import IStorage, DefaultStorage


storage = {}


class TcStorage(IStorage):

    def __init__(self, chat_id: int):
        self.chat_id = chat_id

    def _get_key(self, key: str):
        return str(self.chat_id) + key

    async def set_item(self, key: str, value: str):
        storage[self._get_key(key)] = value

    async def get_item(self, key: str, default_value: str = None):
        return storage.get(self._get_key(key), default_value)

    async def remove_item(self, key: str):
        storage.pop(self._get_key(key))
########################################################################################################################
# connector.py

def get_connector(chat_id: int):
    return TonConnect(MANIFEST_URL, storage=TcStorage(chat_id))

########################################################################################################################
@dp.message(Command('wallet'))
async def command_start_handler(message: Message):
    chat_id = message.chat.id
    connector = get_connector(chat_id)
    connected = await connector.restore_connection()


    mk_b = InlineKeyboardBuilder()
    if connected:
        mk_b.button(text='Send Transaction', callback_data='send_tr')
        mk_b.button(text='Disconnect', callback_data='disconnect')
        await message.answer(text='You are already connected!', reply_markup=mk_b.as_markup())

    else:
        wallets_list = TonConnect.get_wallets()
        for wallet in wallets_list:
            mk_b.button(text=wallet['name'], callback_data=f'connect:{wallet["name"]}')
        mk_b.adjust(1, )
        await message.answer(text='Какой кошелёк подключить?', reply_markup=mk_b.as_markup())





async def send_transaction(message: Message):
    connector = get_connector(message.chat.id)
    connected = await connector.restore_connection()
    if not connected:
        await message.answer('Connect wallet first!')
        return

    transaction = {
        'valid_until': int(time.time() + 3600),
        'messages': [
            get_comment_message(
                destination_address='0:0000000000000000000000000000000000000000000000000000000000000000',
                amount=int(0.01 * 10 ** 9),
                comment='hello world!'
            )
        ]
    }

    await message.answer(text='Approve transaction in your wallet app!')
    try:
        await asyncio.wait_for(connector.send_transaction(
            transaction=transaction
        ), 300)
    except asyncio.TimeoutError:
        timeout = await message.answer(text='Время подключения истекло.')
        await bot.delete_message(message.from_user.id,timeout.message_id)
    except pytonconnect.exceptions.UserRejectsError:
        await message.answer(text='You rejected the transaction!')
    except Exception as e:
        await message.answer(text=f'Unknown error: {e}')


async def connect_wallet(message: Message, wallet_name: str,lang):

    connector = get_connector(message.chat.id)

    wallets_list = connector.get_wallets()
    wallet = None

    for w in wallets_list:
        if w['name'] == wallet_name:
            wallet = w

    if wallet is None:
        raise Exception(f'Unknown wallet: {wallet_name}')

    generated_url = await connector.connect(wallet)

    mk_b = InlineKeyboardBuilder()
    if lang == "RU":
        mk_b.button(text='Подключить', url=generated_url)
    if lang == "EN":
        mk_b.button(text='Connect', url=generated_url)


    if wallet_name == "":
        pass

    print(f"wallet_name: {wallet_name}")
    if wallet_name =="Wallet":
        await message.edit_reply_markup(reply_markup=mk_b.as_markup())
        photo = FSInputFile(f"image/Wallet.png")

        await message.edit_media(InputMediaPhoto(media=photo), reply_markup=mk_b.as_markup())
    if wallet_name =="Tonkeeper":
        await message.edit_reply_markup(reply_markup=mk_b.as_markup())
        photo = FSInputFile(f"image/tonkiper.png")

        await message.edit_media(InputMediaPhoto(media=photo), reply_markup=mk_b.as_markup())
    if wallet_name =="MyTonWallet":
        await message.edit_reply_markup(reply_markup=mk_b.as_markup())
        photo = FSInputFile(f"image/MyTonWallet.png")

        await message.edit_media(InputMediaPhoto(media=photo), reply_markup=mk_b.as_markup())
    if wallet_name =="Tonhub":
        await message.edit_reply_markup(reply_markup=mk_b.as_markup())
        photo = FSInputFile(f"image/Tonhub.png")

        await message.edit_media(InputMediaPhoto(media=photo), reply_markup=mk_b.as_markup())
    if wallet_name =="DeWallet":
        await message.edit_reply_markup(reply_markup=mk_b.as_markup())
        photo = FSInputFile(f"image/DeWallet.png")

        await message.edit_media(InputMediaPhoto(media=photo), reply_markup=mk_b.as_markup())
    if wallet_name =="Bitget Wallet":
        await message.edit_reply_markup(reply_markup=mk_b.as_markup())
        photo = FSInputFile(f"image/Bitget Wallet.png")

        await message.edit_media(InputMediaPhoto(media=photo), reply_markup=mk_b.as_markup())



    mk_b = InlineKeyboardBuilder()
    mk_b.button(text='Start', callback_data='start')

    for i in range(1, 180):
        await asyncio.sleep(1)
        if connector.connected:
            if connector.account.address:
                wallet_address = connector.account.address
                wallet_address = Address(wallet_address).to_str(is_bounceable=False)
                ##Добавить ефима с кошельком
                connect_DB().add_w_addr_by_id(wallet_address, message.chat.id)
                if wallet_name == "Wallet":
                    photo = FSInputFile(f"image/Wallet_connect.png")
                    await message.edit_media(InputMediaPhoto(media=photo), reply_markup=enter_wallet(lang))
                if wallet_name == "Tonkeeper":
                    photo = FSInputFile(f"image/tonkiper_connect.png")
                    await message.edit_media(InputMediaPhoto(media=photo), reply_markup=enter_wallet(lang))
                if wallet_name == "MyTonWallet":
                    photo = FSInputFile(f"image/MyTonWallet_connect.png")
                    await message.edit_media(InputMediaPhoto(media=photo), reply_markup=enter_wallet(lang))
                if wallet_name == "Tonhub":
                    photo = FSInputFile(f"image/Tonhub_connect.png")
                    await message.edit_media(InputMediaPhoto(media=photo), reply_markup=enter_wallet(lang))
                if wallet_name == "DeWallet":
                    photo = FSInputFile(f"image/DeWallet_connect.png")
                    await message.edit_media(InputMediaPhoto(media=photo), reply_markup=enter_wallet(lang))
                if wallet_name == "Bitget Wallet":
                    photo = FSInputFile(f"image/Bitget Wallet_connect.png")
                    await message.edit_media(InputMediaPhoto(media=photo), reply_markup=enter_wallet(lang))



            return

    await message.answer(f'Timeout error!', reply_markup=mk_b.as_markup())


async def disconnect_wallet(message: Message):
    connector = get_connector(message.chat.id)
    await connector.restore_connection()
    await connector.disconnect()
    await message.answer('You have been successfully disconnected!')








########################################################################################################################
if __name__ == "__main__":
    asyncio.run(main())