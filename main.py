from flask import Flask, render_template, request
import requests
import pprint

'''
полезная информация по методу request.form/request.form.get/request.args/get получения данных из форм и их публикация на другой странице HTML
https://qastack.ru/programming/10434599/get-the-data-received-in-a-flask-request
'''


app = Flask(__name__)

@app.route('/')
@app.route('/main_page')
def main_page():
    return render_template('main_page.html')


@app.route('/form')
def form_page():
    return render_template('form.html')


@app.route('/results', methods = ['GET','POST'])
def results():
    city = request.args.get('city')
    keywords = request.args.get('keywords')
    data = {
            'location1': city,
            'keyword1': keywords}

    data_list = []
    total_salary = 0
    data_num = 0
    # Cкачивание вакансий
    # URL = 'https://api.hh.ru/vacancies'
    # parameters = {'text': data[keywords],
    #               'area': data[city]
    #               }
    # data_collection = requests.get(URL, params=parameters).json()

    # оригинальный код
    URL = 'https://api.hh.ru/vacancies'
    parameters = {'text': 'NAME: (менеджер) AND (Москва)'}
    data_collection = requests.get(URL, params=parameters).json()
    # print(data_collection)
    data_list.append(data_collection)
    for j in data_list:
        y = j['items']
        # объявляем переменную n для подсчета собранных по параметрам запроса зарплатных данных
        n = 0
        # создаем переменную для подсчета, суммы зарплат в вакансиях
        sum_of_salary = 0

        for i in y:  # цикл переборки вакансий
            # проверка наличия указанных зарплат в словаре по ключу "salary"
            if i['salary'] != None:
                # записываем значение в переменную s
                s = i['salary']
                # проверяем есть ли в вакансии данные по минимальной зп
                if s['from'] != None:
                    # считаем количество обработанных вакансий в которых указана минимальная ЗП
                    n += 1
                    # получаем минимальную ЗП по ключу from
                    s['from']
                    # считаем сумму найденных ЗП по вакансиям
                    sum_of_salary += s['from']
        # общая сумма ЗП
        total_salary += sum_of_salary
        # добавляем сумму "n" по количеству найденных ЗП
        data_num += n
        # считаем среднюю ЗП
    avg_salary = total_salary / data_num
    data_link = (URL[12:17])
    # print('Данные собраны на: ', str(URL[12:17]))
    # print('Регион сбора данных: Москва')
    print('Для расчета использовано: ', data_num, 'вакансий')
    print('Средняя зарплата по запросу "Python": ', int(avg_salary), 'руб.')

    return render_template('results.html', data=data, avg_salary=avg_salary, data_num=data_num, data_link=data_link)


@app.route('/contacts')
def contact_page():
    return render_template('contacts.html')


if __name__ == "__main__":
    app.run()
