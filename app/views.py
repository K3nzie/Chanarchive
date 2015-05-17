from flask import render_template, flash, redirect
from app import app
from .forms import SendLink

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title="ChanArchive",boards=app.config['CHAN_BOARDS'])

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/faq')
def faq():
	return render_template('faq.html',title="Frequently Asked Questions")