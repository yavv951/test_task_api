# Проект по автоматизации API тестирования для ivi. 
<a target="_blank" href="https://rest.test.ivi.ru/v2">Ссылка на ivi test</a>

## :memo: Содержание:

- [Реализованные проверки](#boom-Реализованные-проверки)
- [Технологии](#classical_building-Технологии)
- [Запуск из терминала](#electron-Запуск-тестов-из-терминала)
- [Allure отчет](#bar_chart-Allure-отчет)

## :boom: Реализованные проверки

- ✓ Проверка поиск всех персонажей
- ✓ Проверка поиск персонажа по имени
- ✓ Проверка поиск персонажа, которого нет в БД
- ✓ Проверка добавление персонажа
- ✓ Проверка удаление персонажа
- ✓ Проверка удаление персонажа, которого нет в БД


## :classical_building: Технологии

<p align="center">
<img width="6%" title="Pycharm" src="images/logo/Pycharm.svg">
<img width="6%" title="Python" src="images/logo/Python.svg">
<img width="6%" title="Allure Report" src="images/logo/Allure.svg">
<img width="6%" title="Pytest" src="images/logo/Pytest.svg">
<img width="6%" title="GitHub" src="images/logo/GitHub.svg">
</p>


## :electron: Запуск тестов из терминала

Локальный запуск:

Create and activate virtual environments

```
для Linux
python3 -m venv venv
source venv/bin/activate

для OC Windows
python -m venv venv
venv\Scripts\activate
```

Run in terminal

```
pip install -r requirements.txt
```

### Run all tests

```
pytest
```

## :bar_chart: Allure-отчет
<img src="images/logo/Allure.svg" width="25" height="25"  alt="Allure"/></a> Отчет в <a target="_blank" href="https://jenkins.autotests.cloud/job/store_api_test/allure/#graph">Allure report</a>
<p align="center">
<a href="https://jenkins.autotests.cloud/job/store_api_test/allure/"><img src="images/image/Allure3.jpg" alt="Allure-отчет"/></a>
</p>
