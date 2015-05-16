from app import db

class Archives(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    archive_name = db.Column(db.String(64), index=True, unique=True)
    archive_short = db.Column(db.String(5), index=True, unique=True)
    archive_collects = db.Column(db.Integer, index=True, unique=False)
    archive_creation_date = date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Archives %r>' % (self.nickname)