# Import library
from main import bot, dp
from aiogram import types
from aiogram.types import Message
import pymysql
from config import dbHost, dbUser, dbPassword, dbName

keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)

connection = pymysql.Connection(dbHost, dbUser, dbPassword, dbName)

# Array for keyboard
array_keyboard = ['Button1', 'Button2']

# Send message to admin
async def send_to_admin(dp):
	await bot.send_message(chat_id=admin_id, text="Bot start")

# Function of start bot
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
        keyboard_markup.add(*(types.KeyboardButton(text) for text in array_keyboard))
        await message.answer(text='Привет, как у тебя дела?', reply_markup=keyboard_markup)

def analytic(nickname, tgid, fullname, command):
	cursor = connection.cursor.cursor()
	cursor.execute("INSERT INTO users(user_nickname, user_tgid, user_fullname, user_command) VALUES ('%s', '%s', '%s', '%s')" % (nickname, tgid, fullname, command))
	connection.commit()
	cursor.close()	
