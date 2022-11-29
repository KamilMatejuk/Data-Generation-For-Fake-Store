from dataclasses import dataclass
import random
from datetime import datetime
from faker import Faker

from data import CATEGORIES


@dataclass
class Offer:
    name: str
    description: str
    price: float
    offer_date: datetime
    quantity: int


def generate(category: str):
    faker = Faker()
    if category == 'Fruit': name = random.choice(["Banana", "Strawberry", "Grape", "Apple", "Watermelon", "Orange", "Blueberrie", "Lemon"]) + " " + random.choice(["Fresh", "1kg", "Natural", "Green"])
    elif category == 'Vegetable': name = random.choice(["potatoe", "tomatoe", "onion", "carrot", "bell", "broccoli", "cucumber"]) + " " + random.choice(["Fresh", "1kg", "Natural", "Green"])
    elif category == 'Electronics': name = random.choice(["TV", "Phone", "Monitor"]) + " " + faker.company() + " " + faker.numerify("@!###@")
    elif category == 'AGD': name = random.choice(["Washing machine", "Freezer", "Oven"]) + " " + faker.company() + " " + faker.numerify("@@-%#")
    elif category == 'Clothes': name = random.choice(["Shirt", "Blause", "Trousers"]) + " " + faker.company() + " " + random.choice(["XS", "S", "M", "L", "XL"])
    else: return None
    return Offer(
        name,
        faker.paragraph(nb_sentences=5),
        float(f'{random.random() * 100:.2f}'),
        faker.date_this_decade(),
        random.randint(1, 999),
    )


if __name__ == '__main__':
    print(generate('Fruit'))
