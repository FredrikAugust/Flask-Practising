# Simple form project using flask
__author__ = 'Fredrik A. Madsen-Malmo'

from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response
from flask import request
import json

app = Flask(__name__)

def get_data():
	try:
		data = json.loads(request.cookies.get('person'))
	except (TypeError):
		data = {}

	return data

@app.route('/')
def index():
	data = get_data()
	return render_template('index.html', saves = data)

@app.route('/save', methods=['POST'])
def save():
	response = make_response(redirect(url_for('index')))
	data = get_data()
	data.update(dict(request.form.items()))
	response.set_cookie('person', json.dumps(dict(data)))
	return response

app.run(debug=True, host='0.0.0.0', port=8080)