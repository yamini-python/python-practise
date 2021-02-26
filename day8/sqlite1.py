from flask import Flask, request, jsonify, make_response 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'yamini'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Data1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app) 
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	username = db.Column(db.String(255))
	password = db.Column(db.String(255))

	def __init__(self, name, username, password):
		self.name = name
		self.username = username
		self.password = password

	def __repr__(self):
		return '<User %r>' % self.username



user=User("yamini","yamini67890","wertyu")
db.create_all()
db.session.add(user) 
db.session.commit() 
print(User.query.all())