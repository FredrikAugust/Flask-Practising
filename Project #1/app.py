# Simple form project using flask
__author__ = 'Fredrik A. Madsen-Malmo'

from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response
from flask import request
from flask import flash
import json
from options import DEFAULTS

app = Flask(__name__)
app.secret_key = 'si734fop8q3w9f7eglkbpoqjwgqf3r80h!@(*#!@&%#$o8irygfhjbekfv]'

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

@app.route('/builder')
def builder():
	return render_template('builder.html', saves = get_data(), options = DEFAULTS)

@app.route('/delete')
def delete():
	flash('Deleted character')
	response = make_response(redirect(url_for('index')))
	response.set_cookie('person', '', expires=0)
	return response

@app.route('/save', methods=['POST'])
def save():
	flash('Saved changes')
	response = make_response(redirect(url_for('builder')))
	data = get_data()
	data.update(dict(request.form.items()))
	response.set_cookie('person', json.dumps(dict(data)))
	return response

app.run(debug=True, host='0.0.0.0', port=8080)