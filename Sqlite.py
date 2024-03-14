import sqlite3
import random

conn = sqlite3.connect('books.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Book
             (name TEXT, pages INTEGER, cover_type TEXT, category TEXT)''')

books = []
for _ in range(10):
    name = f"Book {_ + 1}"
    pages = random.randint(100, 500)
    cover_type = random.choice(['Hardcover', 'Paperback', 'Leathercover', 'E-book'])
    category = random.choice(['Fiction', 'Non-fiction', 'Science Fiction', 'Fantasy', 'Mystery', 'Thriller', 'History', 'Romance', 'Adventure', 'Humor'])
    books.append((name, pages, cover_type, category))

c.executemany('INSERT INTO Book VALUES (?,?,?,?)', books)

conn.commit()

c.execute('SELECT AVG(pages) FROM Book')
average_pages = c.fetchone()[0]
print("Average number of pages:", average_pages)

c.execute('SELECT name FROM Book WHERE pages = (SELECT MAX(pages) FROM Book)')
largest_book_name = c.fetchone()[0]
print("Name of the largest book:", largest_book_name)

conn.close()
