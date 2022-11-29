from dataclasses import dataclass
from datetime import datetime
import random
from faker import Faker


@dataclass
class Customer:
    mail: str
    name: str
    surname: str
    date_of_birth: datetime
    description: str


def generate():
    profile = Faker().simple_profile()
    fname, lname = profile.get('name').split(' ')[:2]
    mail = random.choice(["gmail", "outlook", "yahoo"])
    return Customer(
        f'{fname}.{lname}@{mail}.com'.lower(),
        fname,
        lname,
        profile.get('birthdate'),
        f'This user is a {Faker().job()}'
    )


if __name__ == '__main__':
    print(generate())
