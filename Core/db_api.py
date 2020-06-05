import sqlalchemy as db
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import sessionmaker
import os

print(os.getcwd())

META = db.MetaData()


def db_creator(meta_data):
    create_database('sqlite:///data.db')
    print('db created')
    meta = meta_data
    catalog = db.Table('catalog', meta,
                       db.Column('id', db.Integer, primary_key=True, autoincrement=True),
                       db.Column('item_name', db.Text),
                       db.Column('item_description', db.Text),
                       db.Column('item_price', db.Integer),
                       db.Column('item_quantity', db.Integer))
    basket = db.Table('basket', meta,
                      db.Column('id', db.Integer, primary_key=True, autoincrement=True),
                      db.Column('item_name', db.Text),
                      db.Column('item_description', db.Text),
                      db.Column('item_order', db.Integer))
    log = db.Table('log', meta,
                   db.Column('id', db.Integer, primary_key=True, autoincrement=True),
                   db.Column('user_id', db.Text),
                   db.Column('item_name', db.Text),
                   db.Column('total_bought', db.Integer))
    print("-----------------")
    return catalog, basket, log


if not database_exists('sqlite:///data.db'):
    db_creator(META)
    ENGINE = db.create_engine('sqlite:///data.db')
    META.create_all(ENGINE)
else:
    ENGINE = db.create_engine('sqlite:///data.db')

Session = sessionmaker(bind=ENGINE)


item_test = {'item_name': 'a', 'item_description': 'b',
             'item_price': 0, 'item_quantity': 0}


def get_catalog():
    s = Session()
    items = s.execute("SELECT item_name, item_description, item_price FROM catalog").fetchall()
    return items


def add_item(item={}):
    s = Session()
    connection = ENGINE.connect()
    key, value = '', ''
    for keys, values in item.items():
        key += keys+", "
        value += '"'+str(values)+'", '
    command = "INSERT INTO catalog("+key[:-2]+") VALUES ("+value[:-2]+")"
    s.execute(command)
    s.commit()


def edith_item(): return None


def delete_item():
    def get_item(db_table):
        item = {}
        return item


def buy_item(db_table,item):
    return None

def get_basket():
    return None

def get_statisticks():
    db_list = db_creator()
    return None