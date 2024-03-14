from src.hh_api import HeadHunterAPI
from src.saver import JSONSaver


def user_choice_hh():
    keyword = input('Введите название профессии: \n')
    hh_api = HeadHunterAPI()
    print('Сколько вывести страниц? \n')
    pages = int(input())
    from_hh = hh_api.get_vacancies(keyword, pages)
    print('Список вакансий с сайта "HeadHunter": \n')
    for i in from_hh:
        print(i)
    print('Записать данные в JSON файл (отсортировано по зарплате)? \n')
    user_answer = input('y/n \n').lower()
    if user_answer not in ['y']:
        print('Спасибо за использование программы')
    else:
        jsonfile_hh = JSONSaver()
        jsonfile_hh.add_vacancies(from_hh)
        jsonfile_hh.sort_vacancies_by_salary()
        jsonfile_hh.file_writer()
        return jsonfile_hh