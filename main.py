from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("/landing_page.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)