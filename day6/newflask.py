from flask import Flask,jsonify,request,render_template
data={'carrot':'10','beetroot':'8','beans':'54','tomato':'5'}

app = Flask(__name__)

@app.route('/')
def view_developers():
    dev_list= ["abc","bcd","feh"]
    return render_template('index.html', dev_list=dev_list)

@app.route('/groceries',methods=['GET','POST'])
def displaygroceries():
    if request.method=='GET':
        return jsonify(data)
    else:           # add a new item
        data['onion']=100
        return jsonify(data) 

@app.route('/groceries/<string:name>',methods=['GET','DELETE'])
def findgrocery(name):
    if request.method=='GET':
        if name in data.keys():
            return data[name]
        else:
            return 'Grocery is not found', 404
    else:
        if name in data.keys(): #delete the item
            del data[name]
            return jsonify(data)
        else:
            return 'Grocery is not found for delete', 404
        