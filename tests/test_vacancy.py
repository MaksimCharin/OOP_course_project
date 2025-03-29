import unittest
from src.vacancy import Vacancy

def test_vacancy_initialization():
    vacancy = Vacancy("Python Developer", 100000, 150000, "https://hh.ru/vacancy/123456", "Moscow")
    assert vacancy.name_vacancy == "Python Developer"
    assert vacancy.salary_from == 100000
    assert vacancy.salary_to == 150000
    assert vacancy.url == "https://hh.ru/vacancy/123456"
    assert vacancy.city == "Moscow"

def test_vacancy_comparison():
    vacancy1 = Vacancy("Python Developer", 100000, 150000, "https://hh.ru/vacancy/123456", "Moscow")
    vacancy2 = Vacancy("Java Developer", 120000, 180000, "https://hh.ru/vacancy/789012", "Moscow")
    assert vacancy1 < vacancy2

def test_vacancy_repr():
    # Создаем экземпляр класса Vacancy
    vacancy = Vacancy("Вакансия 1", 50000, 60000, "url1", "Город1")

    # Ожидаемая строка представления
    expected_repr = (
        "\nНазвание вакансии: Вакансия 1\n"
        "Зарплата от: 50000\n"
        "Зарплата до: 60000\n"
        "Город: Город1\n"
        "URL: url1\n"
    )

    # Проверка, что __repr__ возвращает ожидаемую строку
    assert repr(vacancy) == expected_repr, f"Ожидалось: {expected_repr}, Получено: {repr(vacancy)}"


def test_get_vacancy_list():
    # Очистка списка вакансий перед тестом
    Vacancy.list_vacancies.clear()

    # Пример данных
    list_vacancy = [
        {"name": "Вакансия 1", "alternate_url": "url1", "area": {"name": "Город1"}, "salary": {"from": 50000, "to": 60000}},
        {"name": "Вакансия 2", "alternate_url": "url2", "area": {"name": "Город2"}, "salary": {"from": 70000, "to": 80000}},
        {"name": "Вакансия 3", "alternate_url": "url3", "area": {"name": "Город1"}, "salary": None},
    ]

    # Вызов метода класса
    Vacancy.get_vacancy_list(list_vacancy, "Город1", 40000)

    # Проверка, что список вакансий содержит ожидаемое количество элементов
    assert len(Vacancy.list_vacancies) == 2

    # Проверка, что первая вакансия соответствует ожиданиям
    vacancy = Vacancy.list_vacancies[0]
    assert vacancy.name_vacancy == "Вакансия 1"
    assert vacancy.salary_from == 50000
    assert vacancy.salary_to == 60000
    assert vacancy.url == "url1"
    assert vacancy.city == "Город1"