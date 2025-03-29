import unittest
from unittest.mock import patch
from src.get_api_hh import GetApiHh

def test_get_vacancy_from_api():
    with patch('src.get_api_hh.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'items': [{'name': 'Test Vacancy', 'area': {'name': 'Moscow'}, 'salary': {'from': 100000, 'to': 150000}, 'alternate_url': 'https://hh.ru/vacancy/123456'}]}

        api = GetApiHh()
        vacancies = api.get_vacancy_from_api('Test')

        assert len(vacancies) == 1
        assert vacancies[0]['name'] == 'Test Vacancy'

def test_repr():
    # Создаем экземпляр класса с известными данными
    api = GetApiHh()
    api._all_vacancy = [{"name": "Вакансия 1"}, {"name": "Вакансия 2"}]

    # Ожидаемая строка представления
    expected_repr = "[{'name': 'Вакансия 1'}, {'name': 'Вакансия 2'}]"

    # Проверка, что __repr__ возвращает ожидаемую строку
    assert repr(api) == expected_repr, f"Ожидалось: {expected_repr}, Получено: {repr(api)}"

def test_get_all_vacancies():
    # Создаем экземпляр класса с известными данными
    api = GetApiHh()
    api._all_vacancy = [{"name": "Вакансия 1"}, {"name": "Вакансия 2"}]

    # Проверка, что метод возвращает ожидаемый список вакансий
    assert api.get_all_vacancies() == api._all_vacancy, "Метод get_all_vacancies не возвращает ожидаемый список вакансий"

def test_connect_to_api_failure():
    # Мокируем requests.get, чтобы он возвращал статус-код, отличный от 200
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {}

        # Вызов метода _connect_to_api
        result = GetApiHh._connect_to_api({})

        # Проверка, что метод возвращает пустой список при ошибке подключения
        assert result == [], "Метод _connect_to_api должен возвращать пустой список при ошибке подключения"