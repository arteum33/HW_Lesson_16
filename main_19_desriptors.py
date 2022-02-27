# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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

# Если база не существует, то создается новая, иначе пропускаем процесс ее создания
    try:
        engine = create_engine('sqlite:///orm.sqlite', echo=True)
        Base = declarative_base()
    except lite.OperationalError:
        pass

    # # Дескриптор
    # class NonData:
    #     def __init__(self, value=0):
    #         self._value = 0
    #
    #     def __get__(self, instance, owner):
    #         # if value == 'None':
    #         if value is None:
    #             raise ValueError('ОШИБКА: Не заполнена форма!')
    #         self._value = value
    #         # return self._value
    #
    #     def __set__(self, instance, value):
    #         # if value == 'None':
    #         if value is None:
    #             raise ValueError('ОШИБКА: Не заполнена форма!')
    #         self._value = value

    class Vacancy(Base):
        # key_word = NonData()
        # location_reg = NonData()

        __tablename__ = 'salary'
        id = Column(Integer, primary_key = True)
        source = Column(String)
        key_word = Column(String)
        location_reg = Column(String)
        num_job = Column(Integer)
        av_salary = Column(Integer)

        def __init__(self, source, key_word, location_reg, num_job, av_salary):
            self.source = source
            self.key_word = key_word
            self.location_reg = location_reg
            self.num_job = num_job
            self.av_salary = av_salary

        def __str__(self):
           return f'{self.id}, {self.source}, {self.key_word}, {self.location_reg}, {self.num_job}, {self.av_salary}'
    Base.metadata.create_all(engine)


    Session = sessionmaker(bind = engine)
    session = Session()
    data_link_f = str(data_link)
    keywords_f = str(keywords)
    city_f = str(city)
    data_num_f = int(data_num)
    avg_salary_f = int(avg_salary)

    # input_data = Vacancy(data_link_f, keywords_f, city_f, data_num_f, avg_salary_f)
    # session.add(input_data)
    # session.commit()

    # Код очистки базы данных от ошибочных данных
    if keywords_f != 'None' and city_f != 'None':
        input_data = Vacancy(data_link_f, keywords_f, city_f, data_num_f, avg_salary_f)
        session.add(input_data)
        session.commit()
    else:
        pass


    # вывод внесенных в таблицу данных
    salary_query = session.query(Vacancy)
    for sal_avg in salary_query:
        print(sal_avg)

    return render_template('results.html', data=data, avg_salary=avg_salary, data_num=data_num, data_link=data_link)



@app.route('/contacts')
def contact_page():
    return render_template('contacts.html')


if __name__ == "__main__":
    app.run()
