from flask import render_template, flash, redirect, config, request, json
from app import app
from .forms import SendLink
from app import db

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title="ChanArchive")

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/faq')
def faq():
	return render_template('faq.html',title="Frequently Asked Questions")

@app.route('/<board>/<thread>')
def show(board, thread):
	chan =  Archives.query.filter_by(archive_short=board)
	if chan == None:
		flash('Board %s not found' % board)
		return redirect(url_for(404))

	data = json.load('jsons/'+thread+'.json')
	return data