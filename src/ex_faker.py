from faker import Faker
import json
from random import randint


def examples():
    fake = Faker()

    print(fake.name())  # 'Adaline Reichel'    uv add Faker
    print(fake.address())  # '426 Jordy Lodge, Cartwrightshire, SC 88120-6700'
    print(fake.email())  # 'vwilson@hotmail.com'
    print(fake.latitude())  # '26.5687745'
    print(fake.url())  # 'http://www.turner.com/'


def generate_students(n=3):
    fake = Faker()
    data = {
        i: {
            "id": randint(1, 100),
            "name": fake.name(),
            "email": fake.email(),
            "address": fake.address(),
            "latitude": str(fake.latitude()),
            "longitude": str(fake.longitude()),
        }
        for i in range(n)
    }
    with open("students.json", "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    generate_students()