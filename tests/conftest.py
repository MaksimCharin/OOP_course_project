import os
from tempfile import mktemp

import pytest

from src.vacancy import Vacancy


@pytest.fixture
def sample_vacancy():

    return Vacancy(
        name="Python Developer",
        salary_from=100000,
        salary_to=150000,
        url="https://hh.ru/vacancy/123",
        requirements="Опыт работы с Python 3+",
    )


@pytest.fixture
def sample_vacancies():

    return [
        Vacancy("Python Developer", 100000, 150000, "url1", "Need Python skills"),
        Vacancy("Java Developer", 90000, 120000, "url2", "Java experience required"),
        Vacancy("Data Scientist", 150000, 200000, "url3", "Python and ML skills"),
        Vacancy("Frontend Developer", 80000, 0, "url4", "JavaScript required"),
    ]


@pytest.fixture
def temp_file():
    # Создаем временный файл
    temp = mktemp()
    yield temp
    if os.path.exists(temp):
        os.remove(temp)


@pytest.fixture
def sample_vacancies_2():
    """Фикстура с тестовыми вакансиями"""
    return [
        {
            "name": "Python Developer",
            "salary_from": 100000,
            "salary_to": 150000,
            "url": "https://hh.ru/vacancy/1",
            "requirements": "Опыт работы с Python",
        },
        {
            "name": "Java Developer",
            "salary_from": 90000,
            "salary_to": 120000,
            "url": "https://hh.ru/vacancy/2",
            "requirements": "Опыт работы с Java",
        },
    ]
