# Testing templates in Flask
__author__ = 'Fredrik A. Madsen-Malmo'

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name='Undefined'):
	context = {
		'name': name
	}  # This is just a cleaner way of passing vars to render_template

	return render_template('index.html', **context)

app.run(debug=True, port=8080, host='0.0.0.0')