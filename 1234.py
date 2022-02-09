import sqlite3 as lite
from main import *

connect = None
    try:
        connect = lite.connect('parcing_HH.db')
        cur = connect.cursor()
    except lite.Error as e:
        print(f"Error {e.args[0]}:")
        sys.exit(1)
# создадим таблицу
cur.execute("CREATE TABLE hh_parc (NN INT,source TEXT, key_word TEXT, location_req TEXT, Num_job INT, av_salary INT)")
# наполняем данными
n = 0
cur.execute("INSERT INTO hh_parc VALUES(?,?,?,?,?,?)",
            (n, data_link, data['keyword1'], data['location1'], data_num, avg_salary))

for row in records:
    n = n + 1
    cur.execute("UPDATE hh_parc SET NN=? WHERE id=?", (n))

# посмотрим, что получилось
sqlite_select_query = """SELECT *from hh_parc"""
cur.execute(sqlite_select_query)

records = cur.fetchall()

for row in records:
    print(row)

