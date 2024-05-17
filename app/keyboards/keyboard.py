from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

'''
Replies
'''
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🔍Найти лавочку'), KeyboardButton(text='➕Создать лавочку')],
    # [KeyboardButton(text='✏️Изменить лавочку'), KeyboardButton(text='🗑️Удалить лавочку')]
], resize_keyboard=True, input_field_placeholder="???")

geo = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить геолокацию', request_location=True)],
    [KeyboardButton(text='Отмена❌')]
], resize_keyboard=True, input_field_placeholder="Отправьте геолокацию")

cancel = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отмена❌')]], resize_keyboard=True)

reply_rm = ReplyKeyboardRemove()

