import json
from pathlib import Path


class Patient:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    @property
    def bmi(self):
        if not self.height or self.height <= 0:
            return None
        height_m = self.height / 100
        return round(self.weight / height_m ** 2, 2)

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


FILE_PATH = Path("data/patients.json")


def save_patients(patients):
    FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

    data = [p.to_dict() for p in patients]

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_patients():
    if not FILE_PATH.exists():
        return []

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [Patient.from_dict(item) for item in data]