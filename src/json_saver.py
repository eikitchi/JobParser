import json

from parser.abstract_api import AbstractJSONSaver
from vacancy import Vacancy


class JSONSaver(AbstractJSONSaver):
    """
    Класс для добавления/удаления вакансий из vacancies.json
    """
    def add_vacancy(self, vacancy):
        """
        Добавляет класс вакансии в vacancies.json
        """
        try:
            with open("vacancies.json", "r", encoding="windows-1251") as f:
                data = json.load(f)
        except json.decoder.JSONDecodeError:
            data = []

        data.append(vars(vacancy))

        with open("vacancies.json", "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def get_vacancies_by_salary(self, salary):
        """
        Возвращает список вакансий по указанной зарплате
        """
        with open("vacancies.json", "r", encoding="windows-1251") as f:
            salaries = json.load(f)
            matching_vacancies = [vacancy for vacancy in salaries if vacancy["salary"] == salary]
            return [Vacancy(**vacancy) for vacancy in matching_vacancies]

    def delete_vacancy(self, vacancy):
        """
        Удаление класса вакансии из vacancies.json
        """
        with open("vacancies.json", "r", encoding="windows-1251") as f:
            vacancies = json.load(f)

        undel_vacancies = [obj for obj in vacancies if obj["url"] != vars(vacancy)["url"]]

        with open("vacancies.json", "w") as f:
            json.dump(undel_vacancies, f, indent=2, ensure_ascii=False)