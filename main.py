import os
from flask import Flask, flash, request, redirect, url_for, render_template, abort
from werkzeug.utils import secure_filename
import random

from tools.read_audio import transcribe_file
from tools.text_to_text import summarize_text

# TODO manage the tmp folder (delete the files an so on)
if not os.path.exists('tmp'):
    print('Creando el directorio tmp')
    os.makedirs('tmp')

app = Flask(__name__)
app.config['SECRET_KEY'] = str(random.getrandbits(32))

@app.route('/')
def langing_page():
    return render_template("/landing_page.html")

@app.route('/mainpage/')
def main_page():
    return render_template("/main_page.html")

ALLOWED_EXTENSIONS = {'mp3'}
UPLOAD_FOLDER = './tmp'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/mainpage/file/', methods=['POST', 'GET'])
def upload_file():
    try:
        if request.method == 'POST':
            if 'file_audio' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file_audio']
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                file.save(filepath)

                res = transcribe_file(filepath)
                print(f"respuesta: {res}")
                data = ''
                if res.results:
                    for result in res.results:
                        data += result.alternatives[0].transcript + ' '
                    data = str(summarize_text(data))
                else:
                    print(f"Ha habido un problema con el audio: {res}")

                print(data)

                return render_template("/main_page.html", data={"abstract" : data})

        #TODO por dios devolver un error más descriptivo y con fotos de gatitos
        return '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Error Genérico con Gatitos</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        h1 {
            color: #333;
        }
        img {
            width: 200px;
            height: auto;
            margin: 20px;
        }
    </style>
</head>
<body>
    <h1>¡Ups! Algo salió mal.</h1>
    <p>Lo sentimos, pero parece que hubo un error. Por favor, intenta de nuevo más tarde.</p>
</body>
</html>
    '''
    except Exception as e:
        print(f"Error: {e}")
        abort(500, description="Ha ocurrido un error interno. Por favor, intenta de nuevo más tarde.")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
