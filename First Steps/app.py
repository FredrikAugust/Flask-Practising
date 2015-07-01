# Getting the basic gist of Flask, a python lightweight web framework
__author__ = 'Fredrik A. Madsen-Malmo'

from flask import Flask
from flask import request

app = Flask(__name__)  # Magic stuff I'm not prepared to understand

# INDEX #

@app.route('/')  # This is a decorator, kinda like attributes in C#
@app.route('/<name>')  # You can now visit /fredrik to get same effect as GET-string
def index(name='Unassigned'):
	return 'This is {} testing Flask!'.format(name)

# CONCAT PAGE #

@app.route('/concat/<part1>/<part2>')
def concat(part1, part2):
	return 'If you concatenate {} and {}, you will get {}'.format(part1, part2, part1+part2)

# ADD PAGE #

@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
	return '{} + {} = {}'.format(num1, num2, num1 + num2)

app.run(debug=True, port=8080, host='0.0.0.0')  # Debug updates when I make changes, neat