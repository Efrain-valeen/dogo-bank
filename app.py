from flask import Flask, render_template, request, jsonify
from entities.user import User

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    User.save(name, email, password)

    return jsonify({"success": True,})

# underscore methods and properties
if __name__ == '__main__':
    app.run()

