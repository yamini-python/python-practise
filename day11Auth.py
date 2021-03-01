from flask import Flask, request,abort,make_response,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api,Resource
from marshmallow import fields
from marshmallow.validate import Length
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4
import jwt
import datetime
from functools import wraps


app=Flask(__name__)
app.config['SECRET_KEY'] = "yamini"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
api=Api(app)


db =SQLAlchemy(app)
ma = Marshmallow(app)

def abort_User_doesnt_exist(name):
    if not User.query.get(name):
          abort(400, "User doesn't exist")

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),nullable=False)
    password=db.Column(db.String(80),nullable=False)
    def __init__(self, name, password):
        self.name = name
        self.password = password


class UserSchema(ma.SQLAlchemySchema):
    name = fields.Str(required = True, validate = Length(min=3,max=10))
    password = fields.Str(required = True, validate = Length(min=3,max=10))
    
    class Meta:
        fields = ("name","password")

    
db.create_all()

def token_required(f):
    @wraps(f)

    def wrapper(*args, **kwargs):
        token = None
        
        if 'token' in request.headers:
            token = request.headers['token']
        if not token:
            return "Enter the token"

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms = "HS256")
            current_user = User.query.filter_by(id = data['public_id']).first()
            print(data)
            print(current_user)
        except:
            return "Invalid Token"
        return f(current_user, *args, *kwargs)
    
    return wrapper

class Register(Resource):

    def post(self):
        errors = userSchema.validate(request.json)
        if errors:
            abort(400, str(errors))
        user= User(request.json['username'],generate_password_hash(request.json['password'], method='sha256'))
        db.session.add(user)
        db.session.commit()
        return "User registered successfully"

class Login(Resource):
    def post(self):
        auth = request.form 
        if not auth or not auth.get('name') or not auth.get('password'): 
            return make_response('Could not verify', 401) 


        user = User.query.filter_by(name = auth.get("name")).first()
        if user is None:
            return "user doesnot exist"

        if check_password_hash(user.password, auth.get("password")):
            token = jwt.encode({'public_id':user.id, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return token
        
        return "Not Verified", 401


schemamany=UserSchema(many=True)
schemaone=UserSchema()

class UserCreation(Resource):
    @token_required
    def get(self):
        userlist=User.query.all()
        if userlist is not None:
            return schemamany.dump(userlist)
        else:
            return "No user exist"


class ViewUser(Resource):
    @token_required
    def get(self,name):
        abort_User_doesnt_exist(name)
        user=User.query.get(name)
        return schemaone.dump(user)
    
    @token_required
    def delete(self,name):
        abort_User_doesnt_exist(name)
        user=User.query.get(name)
        db.session.delete(user)
        db.session.commit()
        return "User Deleted"

    @token_required
    def put(self,name):
        abort_User_doesnt_exist(name)
        user=User.query.get(name)
        user.password=request.json['password']
        db.session.commit()
        return "password updated"

api.add_resource(UserCreation,'/user')
api.add_resource(ViewUser,'/user/<name>')
api.add_resource(Register,"/user/register")
api.add_resource(Login,"/user/login")

if __name__ == "__main__": 
	app.run(debug = True) 
