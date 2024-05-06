from datetime import datetime
import flask_login
import random, os
from flask import jsonify, request, redirect, Blueprint, render_template
from google.cloud import logging, bigquery
from werkzeug.security import generate_password_hash, check_password_hash


from flask import flash

PROJECT = os.environ.get('PROJECT')
# Verifica si la variable de entorno existe
if PROJECT is None:
    from credentials.ids import PROJECT

REGION = os.environ.get('REGION')
if PROJECT is None:
    from credentials.ids import REGION

app_file_login = Blueprint('app_file_login',__name__)
# Inicializa los clientes de Google Cloud
client = logging.Client(project=PROJECT)
client_bq = bigquery.Client(project=PROJECT)

class User(flask_login.UserMixin):
    def __init__(self, user, password):
        self.id = user
        self.password = password

login_manager = flask_login.LoginManager()
users = {"admin": User("admin", "1234")}
invite_code = 1000

def save_user_to_bigquery(user):
    table_id = f"{PROJECT}.appstract.users"

    # Define los campos de la tabla
    fields = [
        bigquery.SchemaField("id", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("password", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("creation_timestamp", "TIMESTAMP", mode="REQUIRED")
    ]

    # Crea la tabla si no existe
    table = bigquery.Table(table_id, schema=fields)
    try:
        client_bq.create_table(table)  # Crea la tabla si no existe
    except Exception:
        pass

    # comprueba usuarios duplicados
    query = f"SELECT id FROM `{table_id}` WHERE id = '{user.id}'"
    query_job = client_bq.query(query)
    results = list(query_job)
    if results:
        return jsonify({"error": f"el usuario {user.id} ya existe en la base de datos."}), 400

    current_timestamp = datetime.now().timestamp()
    rows_to_insert = [
        dict(
            id=user.id,
            password=user.password,
            creation_timestamp=current_timestamp
        )
    ]

    errors = client_bq.insert_rows_json(table, rows_to_insert)
    if errors == []:
        print("Nuevo usuario guardado en BigQuery.")
    else:
        print("Error al guardar el usuario en BigQuery:", errors)

def user_exists_in_bigquery(user_id):
    query = f"""
        SELECT id, password
        FROM `{PROJECT}.appstract.users`
        WHERE id = '{user_id}'
    """
    try:
        query_job = client_bq.query(query)
        result = query_job.result()
        rows = [dict(row) for row in result]
        if rows:
            user_id = rows[0]['id']
            password_hash = rows[0]['password']
            return True, user_id, password_hash
        else:
            return False, None, None
    except Exception as e:
        print(f"Error al consultar BigQuery: {e}")
        return  False, None, None

def init_login(app):
    global invite_code
    login_manager.init_app(app)
    login_manager.login_view = '/'
    invite_code = random.randrange(1000, 9999)
    print("New invite code is " + str(invite_code))
    client.logger('default').log_text("New invite code is " + str(invite_code))

@login_manager.user_loader
def user_loader(id):
    return users.get(id)

@app_file_login.route('/login/', methods=['GET', 'POST'])
def login():
    try:
        user_id = request.form["user"]
        password = request.form["pass"]
    except KeyError as e:
        return jsonify({"error": f"Falta el campo {e.args[0]} en el formulario."}), 400


    # Verifica si el usuario existe en BigQuery
    exist, user_id_bq, password_bq = user_exists_in_bigquery(user_id)
    if not exist:
        return jsonify({"error": "Usuario no encontrado"}), 400
    
    user = User(user_id, password)
    # Verifica si la contraseña es correcta
    if not exist or not check_password_hash(password_bq, password):
        return jsonify({"error": "Usuario o contraseña incorrectos"}), 400

    # Inicia sesión con éxito
    flask_login.login_user(user)
    return redirect("/mainpage")

@app_file_login.route('/register/')
def register():
    return render_template('/register.html')

@app_file_login.route('/new_user/', methods=['GET', 'POST'])
def new_user():
    user_id = request.form["user"]
    password = request.form["pass"]
    password_hash = generate_password_hash(password)  # Genera el hash aquí
    user = User(user_id, password_hash)
    user_code = request.form.get("code", type=int)
    client.logger('default').log_text(f"{user_code} vs {invite_code}")

    if user_code!= invite_code:
        return jsonify({"error": "El código de invitación no coincide."}), 400

    users[user.id] = user
    print("New user ", user.id)
    flask_login.login_user(user)

    save_user_to_bigquery(user)

    return redirect("/mainpage")