from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(200))
    job = db.Column(db.String(100))
    applications = db.relationship('application', backref='owner', lazy=True)

    def __init__(self, firstname, lastname, age, email, job):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.job = job

class application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appname = db.Column(db.String(100))
    username = db.Column(db.String(100))
    lastconnection = db.Column(db.TIMESTAMP(timezone=True))
    user_id = db.Column(db.Integer, db.ForeignKey('owner.id'))
    owner = db.relationship('owner', backref=db.backref('applications', lazy=True))

    def __init__(self, appname, username, lastconnection, user_id):
        self.appname = appname
        self.username = username
        self.lastconnection = lastconnection
        self.user_id = user_id
