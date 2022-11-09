from dataclasses import dataclass
import random
from datetime import datetime
from faker import Faker


@dataclass
class Photo:
    name: str
    file_name: str
    upload_date: datetime
    file_extension: str


def generate():
    faker = Faker()
    name = faker.sentence(nb_words=4).replace('.', '')
    ext = random.choice(['jpg', 'jpeg', 'png'])
    return Photo(
        name,
        f'{name.replace(" ", "_")}.{ext}',
        faker.date_this_decade(),
        ext
    )


if __name__ == '__main__':
    print(generate())
