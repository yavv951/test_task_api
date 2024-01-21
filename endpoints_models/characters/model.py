import random

from faker import Faker
from pydantic import BaseModel

fake = Faker()


class DataGetCharacter(BaseModel):
    """Модель для авторизации."""

    username: str
    password: str
    name: str

    @staticmethod
    def random():
        """Генерация данных для авторизации."""
        return DataGetCharacter(username=fake.email(), password="APZrVp83vFNk5F", name="")


class Result(BaseModel):
    education: str
    height: float
    identity: str
    name: str
    universe: str
    weight: int  # Изменено на float, так как в модели Result вес указан как float


class DataCharacterInfo(BaseModel):
    """Модель для регистрации."""
    result: Result

    @staticmethod
    def random():
        """Генерация данных для регистрации."""
        education = fake.city()
        height = round(random.uniform(50.0, 100.0), 1)
        identity = fake.word()
        name = fake.name()
        universe = fake.word()
        weight = random.randint(1, 100)
        return DataCharacterInfo(result=Result(education=education, height=height, identity=identity, name=name,
                                               universe=universe, weight=weight))


class MessageResponse(BaseModel):
    """Модель для ответа, поставил пока pass, но нужно описывать для каждого объекта отдельно."""
    pass


class AuthInvalidResponse(BaseModel):
    """Модель для ответа для негативных сценариев."""
    error: str
