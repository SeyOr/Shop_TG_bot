from telebot import types


def main_keyboard_creator():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add(types.KeyboardButton(text="/catalog_editor"))
    markup.add(types.KeyboardButton(text="Catalog"), types.KeyboardButton(text="Basket"))
    markup.add(types.KeyboardButton(text='FAQ'), types.KeyboardButton(text='Get Help'))
    return markup




