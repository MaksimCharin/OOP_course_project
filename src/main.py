from src.get_api_hh import GetApiHh
from src.json_saver import JsonSaver
from src.vacancy import Vacancy


def user_interaction() -> None:
    """Функция для взаимодействия с пользователем"""
    response = GetApiHh()
    file_json = JsonSaver()

    while True:
        user_vacancy = input("Введите ключевые слова для фильтрации вакансий: \n")
        user_city = input("Введите название города для запроса:\n")
        if user_vacancy.isalpha() and user_city.isalpha():
            break
        print("Название должно содержать только буквы.")

    while True:
        user_salary = input("Введите минимальную зарплату: \n")
        if user_salary.isdigit():
            break
        print("Запрос должен содержать целое число.")

    response.get_vacancy_from_api(user_vacancy)
    file_json.save_file(response.get_all_vacancies())
    file_vacancies = file_json.read_file()

    vacancy_list = Vacancy.get_vacancy_list(file_vacancies, user_city, int(user_salary))
    sorted_vacancies = sorted(vacancy_list, reverse=True)  # Сортируем по убыванию зарплаты

    # Цикл для ввода количества вакансий для вывода
    while True:
        count = input("Введите количество вакансий для вывода: \n")
        if count.isdigit():
            count = int(count)
            break
        print("Запрос должен содержать целое число.")

    # Выводим заданное количество вакансий
    print(f"Выводим {count} вакансий:")
    for vacancy in sorted_vacancies[:count]:
        print(vacancy)


if __name__ == "__main__":
    user_interaction()
