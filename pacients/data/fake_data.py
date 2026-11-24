from faker import Faker
import random

from data.manager import Patient

fake = Faker("ru_RU")


def generate_patients(count=30):
    patients = []

    for _ in range(count):
        gender = random.choice(["Мужской", "Женский"])

        if gender == "Мужской":
            name = fake.name_male()
        else:
            name = fake.name_female()

        age = random.randint(18, 85)
        height = round(random.uniform(150, 195), 1)

        # Генерируем реалистичный диапазон ИМТ
        bmi = random.uniform(18.5, 32)
        weight = round(bmi * (height / 100) ** 2, 1)

        patient = Patient(
            name=name,
            age=age,
            gender=gender,
            height=height,
            weight=weight
        )

        patients.append(patient)

    return patients