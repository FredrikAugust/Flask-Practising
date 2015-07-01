# Getting the basic gist of Flask, a python lightweight web framework
__author__ = 'Fredrik A. Madsen-Malmo'

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'This is me testing Flask!'

app.run(debug=True, port=8080, host='0.0.0.0')