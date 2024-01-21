import pytest
from faker import Faker

from endpoints_models.app import StoreApp
from endpoints_models.characters.model import DataGetCharacter, MessageResponse

fake = Faker()


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="api url",
        default="http://rest.test.ivi.ru/v2",
    )


@pytest.fixture(autouse=True)
def app(request) -> StoreApp:
    url = request.config.getoption("--api-url")
    return StoreApp(url)


@pytest.fixture
def get_characters(app):
    data = DataGetCharacter.random()
    res = app.character.get_characters(data=data, type_response=MessageResponse)
    return app, res, data
