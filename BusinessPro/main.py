from flask import Flask, render_template, request, redirect, flash, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
@app.route('/main', methods=['POST', 'GET'])
def index():
    global current_page
    current_page = "main"
    # if request.method == 'POST':
    #     user_name = request.form['user_name']
    #     user_mail = request.form['user_mail']
    #     user_number = request.form['user_number']
    #     user_idea = request.form['user_idea']
    return render_template("mainpage.html")


@app.route('/contacts')
def contacts():
    global current_page
    current_page = "main"
    if request.method == 'POST':
        search_movie = request.form['search_movie'] + "%"
        search_string = search_movie.replace(' ', '').replace(',', '').replace('.', '').replace(':', '').replace(';', '').replace('?', '').replace('!', '').replace('-', '')

        return redirect('/search=' + search_string)
    else:
        return render_template("contactspage.html")


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    global logged_in_user_name
    logged_in_user_name = "NaN"
    global current_page
    current_page = "notmain"
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_mail = request.form['user_password']
        user_number = request.form['user_number']
        user_idea = request.form['user_idea']
    else:
        return render_template("reg.html")


if __name__ == '__main__':
    app.run(debug=True)
