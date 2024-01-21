import allure
import pytest
from allure_commons.types import Severity
from faker import Faker

from endpoints_models.characters.model import MessageResponse, DataGetCharacter, DataCharacterInfo, AuthInvalidResponse

fake = Faker()


@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Vadim')
@allure.feature('Testing api ivi characters')
@allure.story(f'Тест кейс 001 Получение персонажей')
@allure.link('https://github.com/yavv951', name='Owner')
@pytest.mark.smoke
def test_get_characters(app):
    data = DataGetCharacter.random()
    res = app.character.get_characters(data=data, type_response=MessageResponse)
    assert res.status_code == 200, "Check code 200"


@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Vadim')
@allure.feature('Testing api ivi characters')
@allure.story(f'Тест кейс 002 Получение персонажа по имени')
@allure.link('https://github.com/yavv951', name='Owner')
@pytest.mark.smoke
def test_get_character(get_characters):
    app, res, data = get_characters
    response_data = res.json()
    data.name = response_data["result"][0]["name"]
    res = app.character.get_character(data=data, type_response=MessageResponse)
    assert res.status_code == 200, "Check code 200"


@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Vadim')
@allure.feature('Testing api ivi characters')
@allure.story(f'Тест кейс 003 Получение персонажа которого нет в БД')
@allure.link('https://github.com/yavv951', name='Owner')
def test_no_character_in_db(get_characters):
    app, res, data = get_characters
    data.name = fake.name()
    res = app.character.get_character(data=data, type_response=AuthInvalidResponse)
    assert res.status_code == 400, "Check code 400"
    assert res.json().get("error") == f"{'No such name'}", "Ожидалась ошибка - No such name"


@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Vadim')
@allure.feature('Testing api ivi characters')
@allure.story(f'Тест кейс 004 Добавление нового персонажа')
@allure.link('https://github.com/yavv951', name='Owner')
@pytest.mark.bug
def test_add_character(get_characters):
    app, res, data = get_characters
    data_ch = DataCharacterInfo.random()
    res = app.character.post_character(data_ch=data_ch, data=data, type_response=MessageResponse)
    assert res.status_code == 200, "Check code 200"


@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Vadim')
@allure.feature('Testing api ivi characters')
@allure.story(f'Тест кейс 005 Удаление персонажа')
@allure.link('https://github.com/yavv951', name='Owner')
@pytest.mark.smoke
def test_delete_character(get_characters):
    app, res, data = get_characters
    response_data = res.json()
    data.name = response_data["result"][0]["name"]
    res = app.character.delete_character(data=data, type_response=MessageResponse)
    assert res.status_code == 200, "Check code 200"
    assert res.json().get("result") == f"Hero {data.name} is deleted", f"Ожидался результат Hero {data.name} is deleted"


@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Vadim')
@allure.feature('Testing api ivi characters')
@allure.story(f'Тест кейс 006 Удаление персонажа,которого нет в БД')
@allure.link('https://github.com/yavv951', name='Owner')
def test_character_not_delete(get_characters):
    app, res, data = get_characters
    data.name = fake.name()
    res = app.character.delete_character(data=data, type_response=AuthInvalidResponse)
    assert res.status_code == 400, "Check code 400"
    assert res.json().get("error") == f"{'No such name'}", "Ожидалась ошибка - No such name"
