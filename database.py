import sqlite3

conn = sqlite3.connect('my-lib-books.db')

c = conn.cursor()

#c.execute("""CREATE TABLE books_table_one (
#    book_title text,
#    author text,
#    book_location text,
#    genre text,
#    series text,
#    pages text,
#    book_language text,
#    book_type text
#)""")
