# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import sqlite3 as lite
import requests
import pprint


# полезная информация по методу request.form/request.form.get/request.args/get получения данных из форм и их публикация
# на другой странице HTML https://qastack.ru/programming/10434599/get-the-data-received-in-a-flask-request


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
    URL = 'https://api.hh.ru/vacancies'
    parameters = {'text': city and keywords} # фильтрация данных по переменным, вводимым в форме
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
    avg_salary_1 = total_salary / data_num
    avg_salary = int(avg_salary_1)
    data_link = (URL[12:17])

# Создание базы данных и записи данных в нее
    connect = None
    try:
        connect = lite.connect('parcing_HH.db', check_same_thread=False)
        cur = connect.cursor()
    except lite.Error as e:
        print(f"Error {e.args[0]}:")
        sys.exit(1)

    connect = lite.connect('parcing_HH.db')
    cur = connect.cursor()
 # Если база не существует, то создается новая, иначе пропускаем процесс ее создания
    try:
        cur.execute(
            "CREATE TABLE parcing_HH (id TEXT,source TEXT, key_word TEXT, location_req TEXT, Num_job INT, av_salary INT)")
        connect.commit()
    except lite.OperationalError:
        pass
# Считаем количество записей в базе для их нумерации
    sqlite_select_query = """SELECT * FROM parcing_HH"""
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    data_numb = len(records)

    if data_numb == 0:
        w = 1
    else:
        w = data_numb + 1
    data_link_f = str(data_link)
    keywords_f = str(keywords)
    city_f = str(city)
    data_num_f = int(data_numb+1)
    avg_salary_f = int(avg_salary)
    cur.execute("INSERT INTO parcing_HH VALUES(?,?,?,?,?,?)",
                (w, data_link_f, keywords_f, city_f, data_num_f, avg_salary_f))

    # проверяем, что занесено в базу данных
    with connect:
        cur = connect.cursor()
        cur.execute('SELECT * FROM parcing_HH')
        while True:
            row = cur.fetchone()
            if row == None:
                break
            print(row[0], row[1], row[2], row[3], row[4], row[5])

    print('Всего записей:', data_num_f)
    connect.close()

    return render_template('results.html', data=data, avg_salary=avg_salary, data_num=data_num, data_link=data_link)



@app.route('/contacts')
def contact_page():
    return render_template('contacts.html')


if __name__ == "__main__":
    app.run()
