import flask_login
from flask import request, redirect, Blueprint

app_file_login = Blueprint('app_file_login',__name__)

class User(flask_login.UserMixin):
    def __init__(self, user, password):
        self.id = user
        self.password = password

login_manager = flask_login.LoginManager()
    
users = {"admin": User("admin", "1234")}

def init_login(app):
    login_manager.init_app(app)
    login_manager.login_view = '/'

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