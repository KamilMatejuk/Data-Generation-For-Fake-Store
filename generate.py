from customer import generate as generate_customer
from address import generate as generate_address
from photo import generate as generate_photo
from offer import generate as generate_offer
from purchase import generate as generate_purchase
from delivery import generate as generate_delivery
from data import TABLE_FIELDS, CATEGORIES

import random
import oracledb


def insert(cursor, table, values):
    fields = TABLE_FIELDS.get(table)
    fields_names = ", ".join(fields)
    fields_placeholders = ", ".join(map(str, range(1, len(fields) + 1)))
    if not isinstance(values, tuple):
        values = tuple([getattr(values, f) for f in fields])
    cursor.execute(
        f"insert into {table} ({fields_names}) values ({fields_placeholders})",
        values)
    print(f"insert into {table} ({fields_names}) values ({fields_placeholders})", values)


def generate(cursor, number: int):
    insert(cursor, 'Category', (CATEGORIES[0], f'This category groups food subcategories', None))
    for cat in CATEGORIES[1:3]:
        insert(cursor, 'Category', (cat, f'In this category we sell {cat}, is is subcategory of {CATEGORIES[0]}', 1))
    for cat in CATEGORIES[3:]:
        insert(cursor, 'Category', (cat, f'In this category we sell {cat}', None))
        
    customer_id = 0
    address_id = 0
    offer_id = 0
    photo_id = 0
    purchase_id = 0
    delivery_id = 0
    for _ in range(number):
        # try:
        # create customer
        customer = generate_customer()
        customer_id += 1
        insert(cursor, 'Customer', (customer.mail, customer.name, customer.surname, customer.date_of_birth, customer.description))
        for _ in range(random.randint(1, 2)):
            # for each customer create 1-2 addresses
            address = generate_address()
            address_id += 1
            insert(cursor, 'Address', (address.country, address.city, address.state, address.street, address.street_number, address.apartment_number, address.postal_code, customer_id))
        for _ in range(random.randint(0, 2)):
            # for each customer create up to 2 offers
            category = random.choice(CATEGORIES)
            offer = generate_offer(category)
            if offer is None: continue
            offer_id += 1
            insert(cursor, 'Offer', (offer.name, offer.description, offer.price, offer.offer_date, offer.quantity, customer_id, CATEGORIES.index(category)))
            for _ in range(random.randint(0, 3)):
                # for each offer create up to 3 photos
                photo = generate_photo()
                photo_id += 1
                insert(cursor, 'Photo', (photo.name, photo.file_name, photo.upload_date, photo.file_extension, offer_id))
        for _ in range(random.randint(0, 4)):
            # for each customer create up to 4 purchases and deliveries
            purchase = generate_purchase()
            purchase_id += 1
            insert(cursor, 'Purchase', (purchase.quantity, purchase.additional_info, purchase.rating, purchase.purchase_date, offer_id, customer_id))
            delivery = generate_delivery()
            delivery_id += 1
            insert(cursor, 'Delivery', (delivery.expected_arrival, delivery.delivery_type, delivery.status, delivery.sent_date, address_id, purchase_id))
        # except: pass


if __name__ == '__main__':
    with oracledb.connect(
            user="user123",
            password="password",
            host="localhost",
            port=1521,
            service_name="service",
        ) as connection:
        print(connection.version)
        with connection.cursor() as cursor:
            generate(cursor, int(input("How many to generate? ")))
