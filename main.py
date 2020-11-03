from flask import Flask, url_for, request, render_template, redirect 
import json
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/main', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return render_template('main.html', title='Kotosharing')
    else:
        return redirect('/form')


@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
        return render_template('form.html', title='Kotosharing')
    elif request.method == 'POST':
        user = User()
        user.email = request.form['email']
        user.phone = request.form['phone_number']
        user.name = request.form['name']
        user.address = request.form['address']
        user.cat = request.form['cat']
        user.about = request.form['about']
        session = db_session.create_session()
        session.add(user)
        session.commit()        
        return render_template('request.html', title='Kotosharing')


if __name__ == '__main__':
    db_session.global_init("db/Kotosharing.sqlite")
    app.run(port=5000, host='127.0.0.1')