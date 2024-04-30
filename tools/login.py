import flask_login
import random
from flask import request, redirect, Blueprint, render_template

app_file_login = Blueprint('app_file_login',__name__)

class User(flask_login.UserMixin):
    def __init__(self, user, password):
        self.id = user
        self.password = password

login_manager = flask_login.LoginManager()
    
users = {"admin": User("admin", "1234")}
invite_code = 1000

def init_login(app):
    global invite_code
    login_manager.init_app(app)
    login_manager.login_view = '/'
    invite_code = random.randrange(1000, 9999)
    print("New invite code is " + str(invite_code))

@login_manager.user_loader
def user_loader(id):
    return users.get(id)

@app_file_login.route('/login/', methods=['GET', 'POST'])
def login():
    user = users.get(request.form["user"])

    if user is None or user.password != request.form["pass"]:
        return redirect("/")

    flask_login.login_user(user)
    return redirect("/mainpage")

@app_file_login.route('/register/')
def register():
    return render_template('/register.html')

@app_file_login.route('/new_user/', methods=['GET', 'POST'])
def new_user():
    user = User(request.form["user"], request.form["pass"])
    user_code = int(request.form["code"])
    print(user_code, " vs ", invite_code)

    if user_code != invite_code:
        return redirect("/")
    
    users[user.id] = user
    print("New user ", user.id)
    flask_login.login_user(user)
    return redirect("/mainpage")