from customer import generate as generate_customer
from address import generate as generate_address
from photo import generate as generate_photo
from offer import generate as generate_offer
from purchase import generate as generate_purchase
from delivery import generate as generate_delivery
from data import TABLE_FIELDS, CATEGORIES

import random
import oracledb

def show_tables(cursor):
    tables = list(cursor.execute('SELECT owner, table_name FROM all_tables').fetchall())
    print('tables of user SYS:', ', '.join(name for owner, name in tables if owner == 'SYS'))
    print('tables of user MDSYS:', ', '.join(name for owner, name in tables if owner == 'MDSYS'))
    print('tables of user CTXSYS:', ', '.join(name for owner, name in tables if owner == 'CTXSYS'))
    print('tables of user SYSTEM:', ', '.join(name for owner, name in tables if owner == 'SYSTEM'))
    print('tables of other users:\n\t' + '\n\t'.join(f'{owner}: {name}' for owner, name in tables if owner not in ['SYS', 'MDSYS', 'CTXSYS', 'SYSTEM']))


def insert(cursor, table, values):
    fields = TABLE_FIELDS.get(table)
    fields_names = ", ".join(fields)
    fields_placeholders = ", ".join(map(lambda i: f':{i}', range(1, len(fields) + 1)))
    if not isinstance(values, tuple):
        values = tuple([getattr(values, f) for f in fields])
    cmd = f"insert into {table} ({fields_names}) values ({fields_placeholders})"
    print(cmd, values)
    cursor.execute(cmd, values)


def generate_categories(cursor):
    category_id = 0
    category_id += 1
    insert(cursor, 'Category', (category_id, CATEGORIES[0], f'This category groups food subcategories', None))
    for cat in CATEGORIES[1:3]:
        category_id += 1
        insert(cursor, 'Category', (category_id, cat, f'In this category we sell {cat}, is is subcategory of {CATEGORIES[0]}', 1))
    for cat in CATEGORIES[3:]:
        category_id += 1
        insert(cursor, 'Category', (category_id, cat, f'In this category we sell {cat}', None))


def generate(connection, cursor, number: int):
    get_number = lambda table: len(list(cursor.execute(f'select * from {table}').fetchall()))
    customer_id = get_number('Customer')
    address_id = get_number('Address')
    offer_id = get_number('Offer')
    photo_id = get_number('Photo')
    purchase_id = get_number('Purchase')
    delivery_id = get_number('Delivery')
    for _ in range(number):
        try:
            # create customer
            customer = generate_customer()
            customer_id += 1
            insert(cursor, 'Customer', (customer_id, customer.mail, customer.name, customer.surname, customer.date_of_birth, customer.description))
            for _ in range(random.randint(1, 2)):
                # for each customer create 1-2 addresses
                address = generate_address()
                address_id += 1
                insert(cursor, 'Address', (address_id, address.country, address.city, address.state, address.street, address.street_number, address.apartment_number, address.postal_code, customer_id))
            for _ in range(random.randint(0, 2)):
                # for each customer create up to 2 offers
                category = random.choice(CATEGORIES)
                offer = generate_offer(category)
                if offer is None: continue
                offer_id += 1
                insert(cursor, 'Offer', (offer_id, offer.name, offer.description, offer.price, offer.offer_date, offer.quantity, customer_id, CATEGORIES.index(category)))
                for _ in range(random.randint(0, 3)):
                    # for each offer create up to 3 photos
                    photo = generate_photo()
                    photo_id += 1
                    insert(cursor, 'Photo', (photo_id, photo.name, photo.file_name, photo.upload_date, photo.file_extension, offer_id))
            for _ in range(random.randint(0, 4)):
                # for each customer create up to 4 purchases and deliveries
                purchase = generate_purchase()
                purchase_id += 1
                insert(cursor, 'Purchase', (purchase_id, purchase.quantity, purchase.additional_info, purchase.rating, purchase.purchase_date, offer_id, customer_id))
                delivery = generate_delivery()
                delivery_id += 1
                insert(cursor, 'Delivery', (delivery_id, delivery.expected_arrival, delivery.delivery_type, delivery.status, delivery.sent_date, address_id, purchase_id))
        except: pass
        connection.commit()


if __name__ == '__main__':
    with oracledb.connect(
            user="user_zsbd",
            password="password",
            host="localhost",
            port=1521,
            service_name="XEPDB1",
        ) as connection:
        print(connection.version)
        with connection.cursor() as cursor:
            # show_tables(cursor)
            # generate_categories(cursor) # RUN ONCE
            generate(connection, cursor, int(input("How many to generate? ")))
        connection.commit()
