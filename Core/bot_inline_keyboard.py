from telebot import TeleBot, types
#from bot_main_file import TEST_ITEMS, TEST_ORDER_LIST


def __build_menu(buttons, n_cols,
                 header_buttons=None,
                 footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu


def catalog_inline_keyboard_creator(items):
    order_list, item_list = [], []

    for order, item in enumerate(items): #???? unpacking dictionary
        item_list.append(item[0])
        order_list.append(order+1)

    buttons = [types.InlineKeyboardButton(text=order, callback_data=item)
               for order, item in zip(order_list, item_list)]

    menu = __build_menu(buttons, 10)      # creating Inline menu for Catalog to display items for sell

    markup_inline = types.InlineKeyboardMarkup(row_width=10)
    for i in menu:
        markup_inline.row(*i)           #unpacking menu  buttons
    print("inline catalog called", item_list)
    return markup_inline


def basket_inline_keyboard():
    order_conf = '1'
    order_cancel = '2'
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="Buy", callback_data=order_conf))
    markup.add(types.InlineKeyboardButton(text='Cancel order', callback_data=order_cancel))
    return markup


def inline_keyboard_catalog_creator():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="Add item", callback_data='add'),
               types.InlineKeyboardButton(text="Edit item", callback_data='edit'),
               types.InlineKeyboardButton(text="Delete item", callback_data='delete')
               )
    markup.add(types.InlineKeyboardButton(text='Apply', callback_data='apply'),
               types.InlineKeyboardButton(text='Cancel', callback_data='cancel')
               )
    return markup

