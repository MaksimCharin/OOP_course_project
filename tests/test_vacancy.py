import pytest
from src.vacancy import Vacancy

def test_vacancy_initialization():
    """Тест инициализации с обязательными параметрами"""
    vacancy = Vacancy("Dev", 0, 0, "url")
    assert vacancy.name == "Dev"
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 0
    assert vacancy.url == "url"
    assert vacancy.requirements == "Требования не указаны"


@pytest.mark.parametrize("req_input,expected", [
    (None, "Требования не указаны"),
    ("", "Требования не указаны"),
    ("Some reqs", "Some reqs"),
])
def test_requirements_validation(req_input, expected):
    """Параметризованный тест валидации требований"""
    vacancy = Vacancy("Dev", 0, 0, "url", req_input)
    assert vacancy.requirements == expected


def test_vacancy_comparison(sample_vacancy):
    """Тест сравнения вакансий по зарплате"""
    higher_vacancy = Vacancy("Senior", 150000, 200000, "url2")
    lower_vacancy = Vacancy("Junior", 50000, 80000, "url3")

    assert sample_vacancy < higher_vacancy
    assert sample_vacancy > lower_vacancy
    assert not sample_vacancy == higher_vacancy


def test_invalid_comparison(sample_vacancy):
    """Тест сравнения с невалидным типом"""
    with pytest.raises(TypeError, match="Можно сравнивать только вакансии между собой"):
        sample_vacancy < 100000


def test_repr_formatting(sample_vacancy):
    """Тест строкового представления"""
    expected = "Vacancy(Python Developer, salary: 100000-150000, url: https://hh.ru/vacancy/123)"
    assert repr(sample_vacancy) == expected


def test_str_formatting(sample_vacancy):
    """Тест пользовательского строкового представления"""
    expected = (
        "Python Developer\n"
        "Зарплата: 100000-150000\n"
        "Требования: Опыт работы с Python 3+\n"
        "Ссылка: https://hh.ru/vacancy/123"
    )
    assert str(sample_vacancy) == expected


def test_create_from_api_valid():
    """Тест создания из полных API данных"""
    api_data = {
        "name": "API Job",
        "salary": {"from": 100, "to": 200},
        "alternate_url": "api_url",
        "snippet": {"requirements": "API skills"}
    }
    vacancy = Vacancy.create_from_api(api_data)
    assert vacancy.name == "API Job"
    assert vacancy.salary_from == 100
    assert vacancy.salary_to == 200
    assert vacancy.url == "api_url"
    assert vacancy.requirements == "API skills"


def test_create_from_api_missing_fields():
    """Тест создания из неполных API данных"""
    api_data = {
        "name": "Job",
        "alternate_url": "url",
        "salary": None,
        "snippet": None
    }
    vacancy = Vacancy.create_from_api(api_data)
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 0
    assert vacancy.requirements == "Требования не указаны"


def test_to_dict_conversion(sample_vacancy):
    """Тест конвертации в словарь"""
    expected = {
        "name": "Python Developer",
        "salary_from": 100000,
        "salary_to": 150000,
        "url": "https://hh.ru/vacancy/123",
        "requirements": "Опыт работы с Python 3+"
    }
    assert sample_vacancy.to_dict() == expected


def test_salary_validation():
    """Тест валидации зарплаты"""
    assert Vacancy._validate_salary(100000) == 100000
    assert Vacancy._validate_salary(None) == 0
    assert Vacancy._validate_salary("invalid") == 0
    assert Vacancy._validate_salary(-50000) == 0