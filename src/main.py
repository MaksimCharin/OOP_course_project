import time

from src.api_hh import GetApiHh
from src.utils import get_top_vacancies, filter_by_salary, filter_by_keyword, convert_to_dicts
from src.vacancy import Vacancy
from src.json_saver import JsonSaver


def user_interaction() -> None:
    """Основная функция взаимодействия с пользователем"""
    print("Программа для поиска вакансий с HeadHunter")

    # Инициализация компонентов
    hh_api = GetApiHh()
    saver = JsonSaver()

    # Ввод параметров
    search_query = input("Введите поисковый запрос (например 'Python'): ")
    top_n = int(input("Введите количество вакансий для вывода: "))
    min_salary = int(input("Введите минимальную зарплату: "))

    # Получение данных
    print("\nПолучаем вакансии с hh.ru...")
    api_data = hh_api.get_vacancy_from_api(search_query)
    vacancies = [Vacancy.create_from_api(v) for v in api_data]

    # Фильтрация и сортировка через utils
    filtered = filter_by_salary(vacancies, min_salary)

    keyword = input("\nВведите ключевое слово для фильтрации (или Enter): ")
    filtered = filter_by_keyword(filtered, keyword)

    top_vacancies = get_top_vacancies(filtered, top_n)

    # Сохранение результатов
    saver.add_vacancies(convert_to_dicts(top_vacancies))

    # Вывод результатов
    time.sleep(1)
    print(f"\nНайдено {len(top_vacancies)} вакансий:")
    for i, vacancy in enumerate(top_vacancies, 1):
        print(f"\n{i}. {vacancy}")

    # Удаление вакансии
    if top_vacancies:
        print("\nХотите удалить вакансию?")
        url_to_delete = input("Введите URL вакансии для удаления: ")
        if url_to_delete:
            saver.delete_vacancy(url_to_delete)
            print("Вакансия удалена!")


if __name__ == "__main__":
        user_interaction()
