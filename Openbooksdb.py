import sqlite3

conn = sqlite3.connect('books.db')
c = conn.cursor()

c.execute('SELECT * FROM Book')
books = c.fetchall()
for book in books:
    print(book)

conn.close()