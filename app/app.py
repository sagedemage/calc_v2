from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/soc')
def soc():
    return render_template('soc.html')


@app.route('/testing_tools')
def testing_tools():
    return render_template('testing_tools.html')
