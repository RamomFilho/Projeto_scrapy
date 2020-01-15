import sqlite3

connection = sqlite3.connect('tutorial.db')
c = connection.cursor()

sql = 'SELECT * FROM dados WHERE keyword = ?'

sql2 = 'SELECT *FROM dados WHERE keyword = ? and value = ?'

def read_data(wordUsed):
    for row in c.execute(sql, (wordUsed,)):
        print (row)

    print('----')

    for row in c.execute(sql2, ('Python Sentiment', 4)):
        print(row)

read_data('Python Sentiment')