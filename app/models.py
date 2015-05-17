from app import db

class Archives(db.Model):
    archive_id = db.Column(db.Integer, primary_key=True)
    archive_name = db.Column(db.String(64), index=True, unique=True)
    archive_short = db.Column(db.String(5), index=True, unique=True)
    archive_collects = db.Column(db.Integer, index=True, unique=False)
    archive_creation_date = db.Column(db.DateTime, default='NULL')
    threads = db.relationship('Threads', backref='board')

class Threads(db.Model):
	thread_id = db.Column(db.Integer, primary_key=True)
	replies = db.Column(db.Integer)
	images = db.Column(db.Integer)
	archive_id = db.Column(db.Integer, db.ForeignKey('archives.archive_id'))
	visits = db.Column(db.Integer)
	json_file = db.Column(db.String(50), index=True, unique=True)
	takedown = db.relationship('Takedowns', backref='takedown_request')

class Takedowns(db.Model):
	takedown_id = db.Column(db.Integer, primary_key=True)
	URI = db.Column(db.String(40), index=True, unique=True)
	add_infos = db.Column(db.String(200), index=True)
	reason = db.Column(db.String(100), index=True)
	thread_id = db.Column(db.Integer, db.ForeignKey('threads.thread_id'))

#def __repr__(self):
 #  return '<Archives %r>' % (self.nickname)
