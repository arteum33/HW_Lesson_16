import requests
import pprint

data_list=[]
total_salary = 0
data_num = 0
# Cкачивание вакансий
URL = 'https://api.hh.ru/vacancies'

# выбор из списка
where = input('Где искать вакансию?')
# текст
query_string = input('Строка запроса?')

#параметры запроса по ключевому слову Python
# parameters = {'text': 'NAME:(Python) AND (Москва)'}
parameters = {'text': NAME: (query_string) AND (where)}
data_collection = requests.get(URL, params=parameters).json()
data_list.append(data_collection)
for j in data_list:
    y = j['items']
    #объявляем переменную n для подсчета собранных по параметрам запроса зарплатных данных
    n=0
    #создаем переменную для подсчета, суммы зарплат в вакансиях
    sum_of_salary=0

    for i in y: #цикл переборки вакансий
        # проверка наличия указанных зарплат в словаре по ключу "salary"
        if i['salary'] !=None:
            # записываем значение в переменную s
            s=i['salary']
            # проверяем есть ли в вакансии данные по минимальной зп
            if s['from'] !=None:
                # считаем количество обработанных вакансий в которых указана минимальная ЗП
                n+=1
                # получаем минимальную ЗП по ключу from
                s['from']
                # считаем сумму найденных ЗП по вакансиям
                sum_of_salary +=s['from']
    # общая сумма ЗП
    total_salary +=sum_of_salary
    #добавляем сумму "n" по количеству найденных ЗП
    data_num +=n
    #считаем среднюю ЗП
avg_salary=total_salary/data_num
print('Данные собраны на: ', str(URL[12:17]))
print('Регион сбора данных: Москва')
print('Для расчета использовано: ', data_num, 'вакансий')
print('Средняя зарплата по запросу "Python": ', int(avg_salary), 'руб.')




# Проверка данных для оптимизации назначения ключевых слов
# URL = 'https://api.hh.ru/vacancies'
# search_parameters = {'text': 'Python',
#           'page': 1}
# result = requests.get(URL, params = search_parameters).json()
# pprint.pprint(result)
# pprint.pprint(result['found'])