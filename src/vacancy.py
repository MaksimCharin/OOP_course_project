class Vacancy:
    """Класс для представления вакансии"""
    __slots__ = ("name", "salary_from", "salary_to", "url", "requirements")

    def __init__(self, name: str, salary_from: int, salary_to: int, url: str, requirements: str = None):
        self.name = self._validate_name(name)
        self.salary_from = self._validate_salary(salary_from)
        self.salary_to = self._validate_salary(salary_to)
        self.url = self._validate_url(url)
        self.requirements = self._validate_requirements(requirements)

    @staticmethod
    def _validate_name(value: str) -> str:
        """Валидация названия вакансии"""
        return value if value else "Без названия"

    @staticmethod
    def _validate_salary(value: int) -> int:
        """Валидация зарплаты"""
        return value if isinstance(value, int) and value >= 0 else 0

    @staticmethod
    def _validate_url(value: str) -> str:
        """Валидация URL"""
        return value if value else ""

    @staticmethod
    def _validate_requirements(value: str) -> str:
        """Валидация требований"""
        return value if value else "Требования не указаны"

    @classmethod
    def create_from_api(cls, api_data: dict) -> 'Vacancy':
        """Создает экземпляр Vacancy из данных API с полной обработкой"""
        try:
            # Безопасное извлечение данных
            salary = api_data.get("salary") or {}
            snippet = api_data.get("snippet") or {}

            return cls(
                name=api_data.get("name"),
                salary_from=salary.get("from"),
                salary_to=salary.get("to"),
                url=api_data.get("alternate_url"),
                requirements=snippet.get("requirements")
            )
        except Exception:
            return cls(
                name="Невалидная вакансия",
                salary_from=0,
                salary_to=0,
                url="",
                requirements="Данные неполные или повреждены"
            )

    def __lt__(self, other) -> bool:
        """Сравнение по зарплате"""
        if not isinstance(other, Vacancy):
            raise TypeError("Можно сравнивать только вакансии между собой")
        return self.salary_to < other.salary_to

    def __gt__(self, other) -> bool:
        """Сравнение по зарплате"""
        if not isinstance(other, Vacancy):
            raise TypeError("Можно сравнивать только вакансии между собой")
        return self.salary_to > other.salary_to

    def __str__(self) -> str:
        """Строковое представление вакансии"""
        return (f"{self.name}\n"
                f"Зарплата: {self.salary_from}-{self.salary_to}\n"
                f"Требования: {self.requirements}\n"
                f"Ссылка: {self.url}")

    def to_dict(self) -> dict:
        """Преобразует вакансию в словарь для сохранения"""
        return {
            "name": self.name,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "url": self.url,
            "requirements": self.requirements
        }

    def __repr__(self) -> str:
        return f"Vacancy({self.name}, salary: {self.salary_from}-{self.salary_to}, url: {self.url})"
