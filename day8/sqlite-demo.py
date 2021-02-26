from flask import Flask, request, jsonify, make_response 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app) 
ma = Marshmallow(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	username = db.Column(db.String(255))
	password = db.Column(db.String(255))

	def __init__(self, name, username, password):
		self.name = name
		self.username = username
		self.password = password

class UserSchema(ma.Schema):
	class Meta:
		fields = ("id", "name", "username")

user_schema = UserSchema()

user=User("yamini","yamini67890","wertyu")
db.create_all()
db.session.add(user) 
db.session.commit() 
user1=User.query.filter_by(name = "yamini").first()
print(user_schema.dump(user1))

if __name__ == "__main__": 
	app.run(debug = True)

