from flask import render_template, flash, redirect, config, request, json, url_for
from app import app
import string
from .forms import SendLink
from app import db
from .models import *
from sqlalchemy import *

@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
	form = SendLink()
	if request.method == 'POST':
		if form.validate_on_submit():
			redirect(url_for('archive'))
	return render_template('index.html',title='ChanArchive',form=form)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/faq')
def faq():
	return render_template('faq.html',title="Frequently Asked Questions")


@app.route('/archive', methods=['POST'])
def archive():
	form = SendLink()
	link = form.link.data
	#if link.startswith('http://') or link.startswith('https://'):
		#link = link[-7:]
	#data = link.split('/')
	data = link.split('/')
	return render_template('archive.html', form=form, data=data)


@app.errorhandler(404)
def not_found(self):
	return render_template('404.html'), 404

