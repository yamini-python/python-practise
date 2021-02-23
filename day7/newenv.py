from flask import Flask, request
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app)

data = [
    {
        'name' : 'beans',
        'quantity': 15
    },
    {
        'name' : 'carrot',
        'quantity': 8
    },
    {
        'name' : 'tomato',
        'quantity': 20
    },
    {
        'name' : 'onion',
        'quantity': 9
    }
]

class First(Resource):

    def get(self):
        return data
    
    def post(self):
        added = {}
        added['name'] = request.json['name']
        added['quantity'] = request.json['quantity']
        data.append(added)
        return data

class Second(Resource):
    
    def get(self, item):
        
        for items in data:
            if item == items['name']:
                return items
        else:
            abort(404, message="Item Not Found")
    
    def delete(self, item):
        for key,items in enumerate(data):
             if item == items["name"]:
                 data.pop(key)
                 return data
             else:
                 abort(404, message="Item Not Found")
    
    def put(self, item):
        for items in data:
            if item == items['name']:
                items['quantity'] = request.json['quantity']
                return data
        else:
            abort(404, message="Item Not Found")   

api.add_resource(First,'/groceries')
api.add_resource(Second,'/groceries/<item>')

if(__name__=="__main__"):
    app.run(debug=True)