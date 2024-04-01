import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import random
from tools.read_audio import transcribe_file

# Todo manage the tmp folder (delete the files an so on) 
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


# from flask documentation: https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/
ALLOWED_EXTENSIONS = {'mp3'}
UPLOAD_FOLDER = './tmp'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
@app.route('/mainpage/file/', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file_audio' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file_audio']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            data={'abstract' : transcribe_file(filepath)}
            return render_template("/main_page.html", data=data)
    return '''
    <!doctype html>
    <title>ERROR</title>
    <h1>ERROR</h1>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)