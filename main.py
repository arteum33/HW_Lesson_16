from flask import Flask, render_template, request
import requests
import pprint
import jinja2



app = Flask(__name__)

@app.route('/')
@app.route('/main')
def start_page():
    return render_template('main_page.html')

@app.route('/form', methods = ['POST','GET'])
def form_page():

    return render_template('form.html')


@app.route('/results', methods=['GET','POST'])
def results():
    # print(request.form)
    where = request.form.get('where')
    query_string = request.form.get('query_string')
    a = query_string
    b = where
    # data = {
    #         'location': where,
    #         'key_word': query_string}
    # #парсинг данных с HH
    # data_list = []
    # total_salary = 0
    # data_num = 0
    # # Cкачивание вакансий
    # URL = 'https://api.hh.ru/vacancies'
    # # параметры запроса по ключевому слову Python
    # parameters = {'text': 'NAME:(Python) AND (Москва)'}
    # data_collection = requests.get(URL, params=parameters).json()
    # data_list.append(data_collection)
    # for j in data_list:
    #     y = j['items']
    #     # объявляем переменную n для подсчета собранных по параметрам запроса зарплатных данных
    #     n = 0
    #     # создаем переменную для подсчета, суммы зарплат в вакансиях
    #     sum_of_salary = 0
    #
    #     for i in y:  # цикл переборки вакансий
    #         # проверка наличия указанных зарплат в словаре по ключу "salary"
    #         if i['salary'] != None:
    #             # записываем значение в переменную s
    #             s = i['salary']
    #             # проверяем есть ли в вакансии данные по минимальной зп
    #             if s['from'] != None:
    #                 # считаем количество обработанных вакансий в которых указана минимальная ЗП
    #                 n += 1
    #                 # получаем минимальную ЗП по ключу from
    #                 s['from']
    #                 # считаем сумму найденных ЗП по вакансиям
    #                 sum_of_salary += s['from']
    #     # общая сумма ЗП
    #     total_salary += sum_of_salary
    #     # добавляем сумму "n" по количеству найденных ЗП
    #     data_num += n
    #     # считаем среднюю ЗП
    # avg_salary = total_salary / data_num
    # print('Данные собраны на: ', str(URL[12:17]))
    # print('Регион сбора данных: Москва')
    # print('Для расчета использовано: ', data_num, 'вакансий')
    # print('Средняя зарплата по запросу "Python": ', int(avg_salary), 'руб.')
    return render_template('results.html', a=a, b=b)


@app.route('/contacts')
def contact_page():
    return render_template('contacts.html')


# @app.route('/form')
# def cars():
#      model = 'Volvo'
#      price = 1.5
#      data = {
#              'model': 'Volvo',
#              'price': 1.5}
#      return render_template('cars.html', data=data)
#
# @app.route('/cars_form', methods = ['POST'])
# def cars_form():
#      brand = request.form['brand']
#      price = request.form['price']
#      data = {
#              'model': brand,
#              'price': price}
#      return render_template('cars_form.html', data=data)
#
#
# @app.route('/moto')
# def motos():
#
#      data = {
#              'model': 'BMW',
#              'price': 0.8}
#      return render_template('moto.html', **data)


if __name__ == "__main__":
    app.run()



# model = 'Volvo'
#      price = 1.5
#      data = {
#              'model': 'Volvo',
#              'price': 1.5}