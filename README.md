# JobParser
Данный проект предназначен для поиска вакансий на сайтах hh.ru и superjob.ru по заданному поисковому запросу и вывода топ N вакансий с зарплатами, соответствующими ключевым словам фильтрации.

При запуске пользователю предлагается ввести поисковый запрос, количество вакансий для вывода в топ N и ключевые слова для фильтрации вакансий. Затем происходит обращение к API hh.ru и superjob.ru для получения вакансий по заданному запросу. После этого происходит фильтрация полученных вакансий по ключевым словам и наличию зарплаты, сортировка по убыванию зарплаты и выбор первых top N вакансий. Наконец, происходит вывод выбранных вакансий в консоль.

Также проект содержит класс Vacancy для представления вакансии, классы HeadHunterAPI и SuperJobAPI для получения вакансий через API hh.ru и superjob.ru соответственно, класс JSONSaver для добавления/удаления вакансий из файла vacancies.json и абстрактные классы AbstractVacanciesAPI и AbstractJSONSaver для определения интерфейсов классов.

ДЛЯ ЗАПУСКА ПРОЕКТА НЕОБХОДИМО УСТАНОВИТЬ ЗАВИСИМОСТИ ИЗ ФАЙЛА requirements.txt И ОБЯЗАТЕЛЬНО ПОЛУЧИТЬ КЛЮЧ НА САЙТЕ superjob.ru ИНФОРМАЦИЮ ПОЛУЧИТЬ МОЖНО ПЕРЕЙДЯ ПО ЭТОЙ ССЫЛКИ https://api.superjob.ru/