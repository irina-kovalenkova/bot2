from main import bot, dp
from aiogram.types import Message
from config import admin_id
import telebot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from choice_buttons import choice_xo


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")

@dp.message_handler()
async def echo(message:Message):
    global table_dict, counter
    text = f"Привет, ты написал:{message.text}"

    await bot.send_message(chat_id=message.from_user.id, text=text)
    table_dict = {i: k for i, k in zip(range(1, 10), "123456789")}
    counter = 0
    await message.answer(text="Let's play. Choice your sign",
                         reply_markup=choice_xo)
#
#     await message.answer(text=text)
#
# @dp.message_handler()
# async def echo(message:Message):
#     text = f"Привет, ты написал:{message.text}"
#     await bot.send_message(chat_id=message.from_user.id, text=text, reply_markup=fun_choice())


#keyboard = telebot.types.InlineKeyboardButton()
# keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),
#              telebot.types.InlineKeyboardButton('C', callback_data='C'),
#              telebot.types.InlineKeyboardButton('<=', callback_data='<='),
#              telebot.types.InlineKeyboardButton('/', callback_data='/'))
#
# keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
#              telebot.types.InlineKeyboardButton('8', callback_data='8'),
#              telebot.types.InlineKeyboardButton('9', callback_data='9'),
#              telebot.types.InlineKeyboardButton('*', callback_data='*'))
#
# keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
#              telebot.types.InlineKeyboardButton('5', callback_data='5'),
#              telebot.types.InlineKeyboardButton('6', callback_data='6'),
#              telebot.types.InlineKeyboardButton('-', callback_data='-'))

# keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
#              telebot.types.InlineKeyboardButton('2', callback_data='2'),
#              telebot.types.InlineKeyboardButton('3', callback_data='3'),
#              telebot.types.InlineKeyboardButton('+', callback_data='+'))
#
# keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),
#              telebot.types.InlineKeyboardButton('0', callback_data='0'),
#              telebot.types.InlineKeyboardButton(',', callback_data=','),
#              telebot.types.InlineKeyboardButton('=', callback_data='='))
