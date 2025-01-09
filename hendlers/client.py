from asyncore import dispatcher
from imaplib import Commands

from aiogram import Dispatcher, types
from create_bot import bot, dp
from client_kb import kb_client

@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.message):
	try:
		await bot.send_message(message.from_user.id, 'Приятного апетита', reply_markup= kb_client)
		await message.delete()
	except:
		await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Bebrulik_NiuhBot')

@dp.message_handler(commands=['Режим_работы'])
async def bebrulik_open_command(message: types.Message):
	await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00' )

@dp.message_handler(commands=['Росположение'])
async def bebrulik_place_command(message: types.message):
	await bot.send_message(message.from_user.id, 'ул. Колбасная 15')

#@dpmessage_handler(commands=['Меню'])
#async ddef bebrulik_menu_command(message: types.message):
#	for ret in cur.execute('SELECT * FROM menu').fetchall():
#	await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')	


def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start', 'help'])
	dp.register_message_handler(bebrulik_open_command, commands=['Режим_работы'])
	dp.register_message_handler(bebrulik_place_command, commands=['Расположение'])