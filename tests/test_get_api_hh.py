from unittest.mock import patch

import requests

from src.api_hh import ApiHH


def test_get_vacancy_from_api():
    with patch("src.api_hh.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "items": [
                {
                    "name": "Test Vacancy",
                    "area": {"name": "Moscow"},
                    "salary": {"from": 100000, "to": 150000},
                    "alternate_url": "https://hh.ru/vacancy/123456",
                }
            ]
        }

        api = ApiHH()
        vacancies = api.get_vacancy_from_api("Test")

        assert len(vacancies) == 1
        assert vacancies[0]["name"] == "Test Vacancy"


def test_repr():
    # Создаем экземпляр класса с известными данными
    api = ApiHH()
    api._all_vacancy = [{"name": "Вакансия 1"}, {"name": "Вакансия 2"}]

    # Ожидаемая строка представления
    expected_repr = "[{'name': 'Вакансия 1'}, {'name': 'Вакансия 2'}]"

    # Проверка, что __repr__ возвращает ожидаемую строку
    assert repr(api) == expected_repr, f"Ожидалось: {expected_repr}, Получено: {repr(api)}"


def test_get_all_vacancies():
    # Создаем экземпляр класса с известными данными
    api = ApiHH()
    api._all_vacancy = [{"name": "Вакансия 1"}, {"name": "Вакансия 2"}]

    # Проверка, что метод возвращает ожидаемый список вакансий
    assert (
        api.get_all_vacancies() == api._all_vacancy
    ), "Метод get_all_vacancies не возвращает ожидаемый список вакансий"


def test_connect_to_api_failure():
    """Тест обработки ошибки подключения к API"""
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {}

        # Создаем экземпляр класса
        api = ApiHH()

        # Вызываем метод через экземпляр
        result = api._connect_to_api({"text": "test"})

        # Проверяем что возвращается пустой список при ошибке
        assert result == []


def test_connect_to_api_request_exception(capsys):
    """Тест обработки ошибки RequestException с проверкой вывода сообщения"""
    test_exception = requests.RequestException("Test connection error")

    with patch("requests.get") as mock_get:
        mock_get.side_effect = test_exception

        api = ApiHH()
        result = api._connect_to_api({"text": "test"})

        # Проверяем что возвращается пустой список
        assert result == []

        # Проверяем вывод сообщения об ошибке
        captured = capsys.readouterr()
        assert "Ошибка при запросе к API: Test connection error" in captured.out
