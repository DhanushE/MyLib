from flask import Flask, render_template, session, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, NumberRange
import sqlite3 # DB

app = Flask(__name__)

app.config["SECRET_KEY"] = "DHANUSH-EASHWAR-LIBRARY"


class AddBookForm(FlaskForm):

    book_title = TextAreaField('Enter the book title:', validators=[DataRequired()])
    author = TextAreaField('Enter the author of the book:', validators=[DataRequired()])
    location = TextAreaField('Enter the location of the book:', validators=[DataRequired()])
    genre = TextAreaField('Enter the main genre of the book:', validators=[DataRequired()])
    series = TextAreaField('Enter the series which the book is in (type None is there the book is not in a series):', validators=[DataRequired()])
    pages = TextAreaField('Enter the total pages:', validators=[DataRequired()])
    language = TextAreaField('Enter the language of the book:', validators=[DataRequired()])
    type_book = TextAreaField('Enter the type of book (e.g. paperback):', validators=[DataRequired()])
    submit = SubmitField('Add/Submit')

class RemoveBookForm(FlaskForm):
    pass


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-books/', methods=['GET', 'POST'])
def addbooks():

    add_book_form = AddBookForm()

    if add_book_form.validate_on_submit():
        
        session['book_title'] = add_book_form.book_title.data
        session['author'] = add_book_form.author.data
        session['book_location'] = add_book_form.location.data
        session['genre'] = add_book_form.genre.data
        session['series'] = add_book_form.series.data
        session['pages'] = add_book_form.pages.data
        session['language'] = add_book_form.language.data
        session['type'] = add_book_form.type_book.data

        sqliteConnection = sqlite3.connect('my-lib-books.db')
        cursor = sqliteConnection.cursor()
        enter_books = [(session['book_title'], session['author'], session['book_location'], session['genre'], session['series'], session['pages'], session['language'], session['type'])]
        cursor.executemany("INSERT INTO books_table_one VALUES (?,?,?,?,?,?,?,?)", enter_books)
        
        sqliteConnection.commit()
        sqliteConnection.close()

        sqliteConnection = sqlite3.connect('my-lib-books.db')
        cursor = sqliteConnection.cursor()
        sqlite_select_Query = "SELECT rowid, * FROM books_table_one ORDER BY book_title"
        cursor.execute(sqlite_select_Query)
        session['books'] = cursor.fetchall()
        print(session['books'])
        session['amount_of_books'] = len(session['books'])

        return redirect(url_for('books', add_book_form=add_book_form))

    return render_template('addbooks.html', add_book_form=add_book_form)

@app.route('/my-books/')
def books():
    return render_template('books.html')

if __name__ == "__main__":
    app.run() # RUN THE APPLICATION