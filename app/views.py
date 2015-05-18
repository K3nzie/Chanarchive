from flask import render_template, flash, redirect, config, request, json, url_for
from app import app
import string
from .forms import SendLink
from app import db
from .models import *
from sqlalchemy import *
import json
from urllib.parse import urlparse

@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
	form = SendLink()
	if request.method == 'POST':
		if request['link']:
			return redirect(url_for('archive'))
	else: 
		return render_template('index.html',title='ChanArchive',form=form)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/faq')
def faq():
	return render_template('faq.html',title="Frequently Asked Questions")


@app.route('/archive', methods=['POST'])
def archive():
	json_link = 'https://a.4cdn.org'
	form = SendLink()
	link = form.link.data
	# Check if valid link block
	parse = urlparse(link)
	if link == '':
		flash('The field can\'t be empty')
		return redirect(url_for('index'))
	if parse.scheme != 'http':
		flash('Insert a valid URL')
		return redirect(url_for('index'))
	data = link.split('/')
	if data == False:
		flash('The link you provided is not a valid 4chan link')
		return redirect(url_for('index'))

	elif data[2] != 'boards.4chan.org' or len(data[3]) == 0:

		flash('The link you provided is not a valid 4chan link')
		return redirect(url_for('index'))
	# end check block
	j_link = json_link + '/'+ data[3] + '/thread/' + data[5] + '.json'
 
	return render_template('archive.html', form=form)


@app.errorhandler(404)
def not_found(self):
	return render_template('404.html'), 404


@app.errorhandler(500)
def not_found(self):
	return render_template('500.html'), 500

