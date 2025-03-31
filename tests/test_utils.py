from src.vacancy import Vacancy
from src.utils import filter_by_salary, filter_by_keyword, get_top_vacancies, convert_to_dicts


def test_filter_by_salary(sample_vacancies):

    filtered = filter_by_salary(sample_vacancies, 100000)
    assert len(filtered) == 3
    assert filtered[0].name == "Python Developer"
    assert filtered[-1].name == "Data Scientist"


def test_filter_by_keyword(sample_vacancies):

    filtered = filter_by_keyword(sample_vacancies, "Python")
    assert len(filtered) == 2
    assert all("Python" in v.requirements for v in filtered)

    html_vacancy = [Vacancy("Dev", 0, 0, "url", "<b>Python</b> skills")]
    assert len(filter_by_keyword(html_vacancy, "Python")) == 1


def test_get_top_vacancies(sample_vacancies):

    top = get_top_vacancies(sample_vacancies, 2)
    assert len(top) == 2
    assert top[0].name == "Data Scientist"
    assert top[1].name == "Python Developer"


def test_convert_to_dicts(sample_vacancies):

    dicts = convert_to_dicts(sample_vacancies)
    assert len(dicts) == 4
    assert all(isinstance(v, dict) for v in dicts)
    assert dicts[0]["name"] == "Python Developer"
