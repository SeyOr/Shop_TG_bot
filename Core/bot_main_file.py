from settings import TG_TOKEN
from telebot import TeleBot, types
import bot_main_keyboard as mk
import bot_inline_keyboard as ik
import time
import db_api as db

bot = TeleBot('{}'.format(TG_TOKEN))


@bot.message_handler(commands=['start'])
def bot_start_handler(msg):
    main_keyboard = mk.main_keyboard_creator()
    bot.send_message(msg.chat.id, text="Welcome to Shopping Bot", reply_markup=main_keyboard)


@bot.message_handler(commands=['catalog_editor'])
def editor_call(msg):
    keyboard = ik.inline_keyboard_catalog_creator()
    print('--------------')
    bot.send_message(msg.chat.id, text='Welcome to editor', reply_markup=keyboard)


@bot.message_handler(regexp='Catalog')
def catalog_call(msg):
    catalog_list = db.get_catalog()
    keyboard = ik.catalog_inline_keyboard_creator(catalog_list)
    bot.send_message(msg.chat.id, text='Welcome to Catalog\nChoose what you like', reply_markup=keyboard)


@bot.message_handler(regexp=f'Basket')
def basket_call(msg):
    keyboard = ik.basket_inline_keyboard()
    full_order = ordered_items(TEST_ORDER_LIST, TEST_ITEMS)
    print('------------------OK---------------')
    print(full_order)
    bot.send_message(msg.chat.id, text=full_order, reply_markup=keyboard)


@bot.message_handler(regexp=f'FAQ')
def faq_call(msg):
    faq_text = 'This is Shopping bot\nUse catalog to select item and choose ' \
               'what you need.\nAfter - push "Basket" to check and confirm order'
    bot.send_message(msg.chat.id, text=faq_text)


@bot.message_handler(regexp=f'Get Help')
def help_call(msg):
    text = 'Help request has been sent to admin'
    bot.send_message(msg.chat.id, text=text)


@bot.callback_query_handler(func=lambda item: item.data in [c[0] for c in db.get_catalog()])
def show_item(item):
    print("--------In catalog---------")
    catalog_list = db.get_catalog()
    keyboard = ik.catalog_inline_keyboard_creator(catalog_list)
    description = get_item_description(item.data)
    bot.send_message(item.from_user.id, text=description, reply_markup=keyboard)


command_catalog_list = ['add', 'edit', 'delete', 'apply', 'cancel']


@bot.callback_query_handler(func=lambda command: command.data in command_catalog_list)
def catalog_command_user(command):

    if command.data == 'add':
        request = {'Item name': 'str', 'Item description': 'str', 'Item price': int(1), 'Item quantity': int(2)}
        for key in request.keys():
            bot.send_message(command.from_user.id, text='Pls enter: '+key)
            time.sleep(10)

            @bot.message_handler(func=lambda lst:True)
            def message(msg):
                print(msg.text)
                i = 0
                while type(msg.text) != type(request[key]) or msg.text == '':
                    if type(msg.text) != type(request[key]):
                        bot.send_message(command.from_user.id, text='Wrong format')
                    time.sleep(4)
                    print('error')
                    i += 1
                    if i > 5:
                        bot.send_message(chat_id=id, text="Time out")
                        return None
                item[key] = msg.text
                print(msg.text)

        db.add_item(item)
        bot.send_message(command.from_user.id, text="new item saved")

    elif command.data == 'edit':
        return None
    elif command.data == 'delete':
        return None
    elif command.data == 'apply':
        return None
    elif command.data == 'cancel':
        bot.send_message(command.from_user.id, text='Canceling all changes. '
                                                    'Returning to main menu')


def ordered_items(order_list, items):
    full_order = 'Your order is:\n'
    total_price = 0
    for item, item_count in order_list.items():
        total_price += items[item]*item_count
        full_order += '''{item}: {item_count}pcs \n'''.format(item=item, item_count=item_count)

    full_order += 'Total price: {}'.format(total_price)
    return full_order


def get_item_description(get_item):
    catalog = db.get_catalog()
    for item in catalog:
        if get_item in item[0]:
            description = '''{item} \n\nPrice per pc: {price}'''.format(item=item[1], price=item[2])
            print(description)
            return description


bot.polling()
