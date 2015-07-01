# Getting the basic gist of Flask, a python lightweight web framework
__author__ = 'Fredrik A. Madsen-Malmo'

from flask import Flask
from flask import request

app = Flask(__name__)  # Magic stuff I'm not prepared to understand

@app.route('/')  # This is a decorator, kinda like attributes in C#
def index(name='Unassigned'):
	name = request.args.get('name', name)  # This get's the name variable frmo the GET req.
	return 'This is {} testing Flask!'.format(name)

app.run(debug=True, port=8080, host='0.0.0.0')  # Debug updates when I make changes, neat