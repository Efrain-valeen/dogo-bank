from flask import Flask, render_template, request, jsonify, redirect, url_for
from entities.log import Log
from entities.user import User
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from dotenv import load_dotenv
import os
from entities.account import Account
from enums.log_type import LogType

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'index'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/welcome')
@login_required
def welcome():
    account = Account.get_account_by_user(current_user.id)

    balance = 0
    if account:
        balance = account.get_balance()

    return render_template('welcome.html', account=account, balance=balance)


@app.route('/api/user', methods=['POST'])
def create_user():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if User.check_email_exists(email):
        return jsonify({"success": False}), 409

    if User.save(name, email, password):
        return jsonify({"success": True}), 201

    return jsonify({"success": False}), 500


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = User.check_login(email, password)

    if user:
        login_user(user)
        Log.save_log(user, "Inicio de sesión", LogType.LOGIN)

        return jsonify({"success": True}), 200

    return jsonify({"success": False}), 401


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()