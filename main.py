from flask import Flask
from flask import render_template
import os

# Todo manage the tmp folder (delete the files an so on) 
if not os.path.exists('tmp'):
    print('Creando el directorio tmp')
    os.makedirs('tmp')

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("/main_page.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)