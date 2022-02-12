from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/hello/<int:number>')
def hello2(number):
    return f'Hello number {number}'

@app.route('/motd', methods=['GET'])
def motd():
    name = request.args.get('name', default='')
    age = request.args.get('age', default=0)
    return redirect(url_for('secret'))
@app.route('/secret', methods=['GET'])
def secret():
    return 'You found a secret!'