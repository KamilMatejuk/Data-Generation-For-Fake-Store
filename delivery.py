from dataclasses import dataclass
import random
from datetime import datetime
from faker import Faker


@dataclass
class Delivery:
    expected_arrival: datetime
    delivery_type: str
    status: str
    sent_date: datetime


def generate():
    faker = Faker()
    return Delivery(
        faker.date_this_decade(),
        random.choice(["truck", "ship", "plain", "train", "pick up"]),
        random.choice(["preparing for delivery", "picked up by delivery man", "delivered"]),
        faker.date_this_decade(),
    )


if __name__ == '__main__':
    print(generate())
