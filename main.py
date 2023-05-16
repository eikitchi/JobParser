from functions import filter_vacancies, sort_vacancies, get_top_vacancies, print_vacancies
from parser.hh_api import HeadHunterAPI
from parser.sj_api import SuperJobAPI


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
