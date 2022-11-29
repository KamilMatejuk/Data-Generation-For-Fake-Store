from dataclasses import dataclass
import random
from datetime import datetime
from faker import Faker


@dataclass
class Purchase:
    quantity: int
    additional_info: str
    rating: int
    purchase_date: datetime


def generate():
    faker = Faker()
    return Purchase(
        random.randint(1, 999),
        faker.paragraph(nb_sentences=2),
        random.randint(1, 5),
        faker.date_this_decade()
    )


if __name__ == '__main__':
    print(generate())
