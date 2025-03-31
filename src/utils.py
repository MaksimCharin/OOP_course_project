import re
from typing import List
from src.vacancy import Vacancy

def filter_by_salary(vacancies: List[Vacancy], min_salary: int) -> List[Vacancy]:
    """Фильтрует вакансии по минимальной зарплате"""
    return [v for v in vacancies if v.salary_to >= min_salary]


def filter_by_keyword(vacancies: List[Vacancy], keyword: str) -> List[Vacancy]:
    """Фильтрует вакансии по ключевому слову"""
    if not keyword or not keyword.strip():
        return vacancies

    keyword_lower = keyword.lower().strip()
    pattern = re.compile(r'<[^>]+>|&[a-z]+;')

    filtered = []
    for vacancy in vacancies:
        # Ищем в названии
        name = vacancy.name.lower() if vacancy.name else ""
        if keyword_lower in name:
            filtered.append(vacancy)
            continue

        # Ищем в требованиях
        if vacancy.requirements:
            requirements = pattern.sub(' ', vacancy.requirements).lower()
            if keyword_lower in requirements:
                filtered.append(vacancy)
                continue

        # Ищем в описании (если есть поле description)
        if hasattr(vacancy, 'description') and vacancy.description:
            description = pattern.sub(' ', vacancy.description).lower()
            if keyword_lower in description:
                filtered.append(vacancy)

    return filtered

def get_top_vacancies(vacancies: List[Vacancy], top_n: int) -> List[Vacancy]:
    """Возвращает топ N вакансий по зарплате (по убыванию)"""
    return sorted(vacancies, reverse=True)[:top_n]

def convert_to_dicts(vacancies: List[Vacancy]) -> List[dict]:
    """Конвертирует список вакансий в список словарей"""
    return [v.to_dict() for v in vacancies]