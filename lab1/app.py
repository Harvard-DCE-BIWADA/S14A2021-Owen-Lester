from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    bestClassEver = 'Best Class Ever'
    return render_template('index.html', bCE=bestClassEver)


@app.route('/world')
def hello_world():
    return render_template('layout.html', text = 'Hello, World!')


@app.route('/<you>')
def hello_you(you):
    return render_template('layout.html', text = 'Hello, ' +you + '!')