from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ContentType, Message
from aiogram.utils import executor
import markups as nav
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Привет! Выбери свою категорию👇',reply_markup=nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'АБИТУРИЕНТ':
        await message.reply('Привет, абитуриент!\nДанный чат-бот предназначен дня информирования абитуриентов ОмГТУ о направлениях подготовки и специальностях, по которым университет ведет подготовки, а также об условиях приема в вуз',reply_markup=nav.otherMenu)

    elif message.text == '👈ГЛАВНОЕ МЕНЮ':
        await message.reply('Выбери свою категорию👇',reply_markup=nav.mainMenu)
    elif message.text == 'ПЕРВОКУРСНИК':
        await message.reply('Привет, студент Омского государственного технического университета!',reply_markup=nav.otherMenu2)
    elif message.text == '📌МИН БАЛЛЫ ЕГЭ 2023':
        await message.reply("Минимальные баллы для поступления в ОмГТУ:\n\nРусский язык 40\nМатематика(профиль) 39\nФизика 39\nИнформатика и ИКТ 44\nОбществознание 45\nХимия 39\nИностранные языки 30")
    elif message.text == '📌ИНФОРМАЦИЯ О ВУЗЕ':
        await message.reply("Сайт: https://www.omgtu.ru\n\nАдрес ОмГТУ: 644050, Сибирский федеральный округ, Омская область, г. Омск, Пр. Мира, д. 11\n\nРежим и график работы:\nПонедельник - пятница с 9.00 до 17.30;\nсуббота, воскресенье - выходные дни\n\nТел.: +7 (3812) 65-34-07\nФакс.: +7 (3812) 65-26-98\nЭл. почта: info@omgtu.ru")
    elif message.text == '📌НАПРАВЛЕНИЯ ПОДГОТОВКИ И СПЕЦИАЛЬНОСТЕЙ':
            chat_id = message.from_user.id
            photo1_file_id = 'AgACAgIAAxkBAANiZDKAHNxjAAGpUq3OoVLfiZkXpNkaAAJRxTEb6bmZSfDkwuy2O8dsAQADAgADdwADLwQ'
            photo2_file_id = 'AgACAgIAAxkBAANkZDKAq2qyv1gKcaSOcoMax4SpIBAAAlrFMRvpuZlJwUHCDkw10TMBAAMCAAN3AAMvBA'
            await dp.bot.send_photo(chat_id=chat_id, photo=photo1_file_id)
            await dp.bot.send_photo(chat_id=chat_id, photo=photo2_file_id)
    elif message.text == '📌ПРИЕМНАЯ КОМИССИЯ':
        await message.reply("Cвязь с приемной комиссией\n\nАдрес: Пр. Мира, 11, 8 корпус,1 этаж, каб. 8-115\nТелефон:  +7 (3812) 72-90-55 \nЭлектронная почта: pk@omgtu.ru\nПонедельник - пятница: с 10.00 до 17.00, суббота и воскресенье - выходной")
    elif message.text == '📌ИНФОРМАЦИЯ О ХОДЕ ПРИЕМА':
        await message.reply("Информация о количестве поданных заявлений: https://www.omgtu.ru/s1c2/Informaciya_O_Kolichestve_Podannyh_Zayavlenij.html\n\nРанжированные списки поступающих (бакалавриат и специалитет), по договорам: https://omgtu.ru/s1c2/Ranzhirovannyye_Spiski_bachelor_k.html")
    elif message.text == '📌СХЕМА РАСПОЛОЖЕНИЯ КОРПУСОВ':
        chat_id = message.from_user.id
        photo1_file_id = 'AgACAgIAAxkBAAIBEWRPnfHj7lRK3AJzgfUzpwpNb9mlAAJhyjEbD5d4Sqn3Vk1BtT4xAQADAgADdwADLwQ'
        await dp.bot.send_photo(chat_id=chat_id, photo=photo1_file_id)
    elif message.text == '📌АДРЕСА КОРПУСОВ':
        chat_id = message.from_user.id
        photo_file_id = 'AgACAgIAAxkBAAIBE2RPnfxMub2kQ9U9ccgpOdTliQsRAAJiyjEbD5d4SicZX4uOyr1GAQADAgADdwADLwQ'
        await dp.bot.send_photo(chat_id=chat_id, photo=photo_file_id)
    elif message.text == '📌РАСПИСАНИЕ ЗАНЯТИЙ':
        await message.reply('https://rasp.omgtu.ru')
@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):
    await message.reply(message.photo[-1].file_id)
def main():
    executor.start_polling(dp, skip_updates=True)