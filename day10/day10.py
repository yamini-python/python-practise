from flask import Flask, request,abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api,Resource
from marshmallow import fields
from marshmallow.validate import Length

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
api=Api(app)


db =SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    name=db.Column(db.String(80), primary_key=True)
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

def abort_User_doesnt_exist(name):
    if not User.query.get(name):
          abort(400, "User doesn't exist")

schemamany=UserSchema(many=True)
schemaone=UserSchema()

class UserCreation(Resource):
    def get(self):
        userlist=User.query.all()
        if userlist is not None:
            return schemamany.dump(userlist)
        else:
            return "No user exist"


    def post(self):
        error = schemaone.validate(request.json)
        if error:
            abort(400,str(error))
        name = request.json['name']
        password = request.json['password']
        user=User(name,password)
        db.session.add(user)
        db.session.commit()
        return "User registered successfully"


class ViewUser(Resource):
    def get(self,name):
        abort_User_doesnt_exist(name)
        user=User.query.get(name)
        return schemaone.dump(user)

    def delete(self,name):
        abort_User_doesnt_exist(name)
        user=User.query.get(name)
        db.session.delete(user)
        db.session.commit()
        return "User Deleted"

    def put(self,name):
        abort_User_doesnt_exist(name)
        user=User.query.get(name)
        user.password=request.json['password']
        db.session.commit()
        return "password updated"

api.add_resource(UserCreation,'/user')
api.add_resource(ViewUser,'/user/<name>')

if __name__ == "__main__": 
	app.run(debug = True) #py day10.py