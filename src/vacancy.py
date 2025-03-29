class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ['name_vacancy', 'salary_from', 'salary_to', 'url', 'city']
    list_vacancies = []

    def __init__(self, name_vacancy: str, salary_from: int, salary_to: int, url: str, city: str):
        self.name_vacancy = name_vacancy
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.url = url
        self.city = city
        self.list_vacancies.append(self)

    def __repr__(self):
        return (f"\nНазвание вакансии: {self.name_vacancy}\n"
                f"Зарплата от: {self.salary_from}\n"
                f"Зарплата до: {self.salary_to}\n"
                f"Город: {self.city}\n"
                f"URL: {self.url}\n")

    def __lt__(self, other):
        return self.salary_to < other.salary_to

    @classmethod
    def get_vacancy_list(cls, list_vacancy: list, city: str, salary_from: int) -> list:
        """Получение списка с вакансиями"""
        for vacancy in list_vacancy:
            name_vacancy = vacancy["name"]
            url = vacancy["alternate_url"]
            if vacancy["area"]["name"] == city:
                city = vacancy["area"]["name"]
            if vacancy["salary"] is None:
                continue
            elif vacancy["salary"]["to"] is not None and vacancy["salary"]["from"]:
                if vacancy["salary"]["from"] >= salary_from:
                    salary_from = vacancy["salary"]["from"]
                    salary_to = vacancy["salary"]["to"]
                    cls(name_vacancy, salary_from, salary_to, url, city)
        return cls.list_vacancies
