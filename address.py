from dataclasses import dataclass
import random
from faker import Faker


@dataclass
class Address:
    country: str
    city: str
    state: str
    street: str
    street_number: int
    apartment_number: int
    postal_code: str


def generate():
    faker = Faker()
    return Address(
        faker.country(),
        faker.city(),
        faker.state(),
        faker.street_name(),
        random.randint(1, 99),
        random.randint(1, 99),
        f'{random.randint(10, 99)}-{random.randint(100, 999)}',
    )


if __name__ == '__main__':
    print(generate())
