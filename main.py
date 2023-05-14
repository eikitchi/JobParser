from hh_api import HeadHunterAPI
from sj_api import SuperJobAPI
from vacancy import Vacancy


def filter_vacancies(hh_vacancies, superjob_vacancies, filter_words):
    """
    Функция для фильтрации вакансий по ключевым словам
    """
    vacancies = []
    for v in hh_vacancies:
        for word in filter_words:
            if word.lower() in v["name"].lower():
                try:
                    vacancies.append(
                        Vacancy(v["name"], v["alternate_url"], v["salary"]["from"], v["snippet"]["responsibility"]))
                except TypeError:
                    continue

    for v in superjob_vacancies:
        for word in filter_words:
            if word.lower() in v["profession"]:
                vacancies.append(Vacancy(v["profession"], v["link"], v["payment_from"], v["candidat"]))
    return vacancies


def sort_vacancies(filtered_vacancies):
    """
    Функция для сортировки списка вакансий по зарплате
    """
    return sorted(filtered_vacancies, key=lambda v: v.salary or 0, reverse=True)


def get_top_vacancies(sorted_vacancies, top_n):
    """
    Получение первых top_n вакансий
    """
    return sorted_vacancies[:top_n]


def print_vacancies(vacancies):
    """
    Вывод всех вакансий
    """
    count = 0
    for v in vacancies:
        count += 1
        print(f'{count}.{v}')


def user_interaction():
    """
    Основной блок проекта.
    """
    hh_api = HeadHunterAPI()
    sj_api = SuperJobAPI()
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    hh_vacancies = hh_api.get_vacancies(search_query)
    sj_vacancies = sj_api.get_vacancies(search_query)
    filtered_vacancies = filter_vacancies(hh_vacancies, sj_vacancies, filter_words)

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == '__main__':
    user_interaction()
