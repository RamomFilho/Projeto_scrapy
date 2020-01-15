import sqlite3
import datetime
import time

connection = sqlite3.connect('tutorial.db')
c = connection.cursor()

data_id = 4
keyword = 'Python is awesome!'

value = 4


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS dados (id integer, unix real, keyword text, datestamp text, value real )')


create_table()

def dataentry():
    # c.execute("INSERT INTO dados  VALUES(1, 13243123424.288, 'Python Sentiment', '2013-04-14 10:09:41', 5)")
    # c.execute("INSERT INTO dados VALUES(2, 123424252.905, 'Python Sentiment', '2013-04-14 10:10:57', 6)")
    # c. execute("INSERT INTO dados VALUES(3, 13294328.123, 'Python Sentiment', '2013-04-14 10:11:41', 4)")

    date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
    
    c.execute('INSERT INTO dados(id, unix, keyword, datestamp, value) VALUES(?,?,?,?,?)', (data_id, time.time(), keyword, date, value))
    
    connection.commit()

dataentry()