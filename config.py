import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

CHAN_BOARDS = [
    {'name': 'Random','short': '/b/'},
    {'name': 'ANime & Manga','short': '/a/'},
    {'name': 'Fitness','short': '/fit/'},
    {'name': 'Shit 4chan Says','short': '/s4s/'},
    {'name': 'Hentai','short': '/h/'}
    ]
