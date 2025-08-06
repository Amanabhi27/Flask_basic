from flask import Flask, jsonify, request, abort
app=Flask(__name__)
# in-memory database
items=[
    {"id": 1, "name": "Laptop","price":50000},
    {"id": 2, "name": "Realme","price":60000},
]

@app.route("/")
def home():
    return {"message":"welcome to FLASK REST API. "}

# get all items
@app.route("/items",methods=["GET"])
def getitems():
    return jsonify(items)
    
    
 #get item by id  
@app.route("/items/<int:itemid>",methods = ["GET"])
def getitem(itemid):
    item=next((i for i in items if i["id"]==itemid),None)
    if item:
        return jsonify(item)
    abort(404,decription="item not found!")


@app.route("/items",methods=["POST"])
def createitems():
    data=request.get_json()
    if not data or 'name' not in data or 'price' not in data:
        abort(404,decription="invalid input!")
    newid=items[-1]['id']+1 if items else 1
    item={
        'id':newid,
        'name':request.json['name'],
        'price':request.json['price']
    }

    items.append(item)
    return jsonify(item),201

@app.route('/items/<int:itemid>',methods=['PUT'])
def update_item(itemid):
    item=next((i for i in items if i['id']==itemid),None)
    if item is None:
        abort(404)
    if not request.json:
        abort(404)
    item['name']=request.json.get('name',item['name'])
    item['price']=float(request.json.get('price',item['price']))
    return jsonify(item)
    
 #delete items
@app.route('/items/<int:itemid>',methods=['DELETE'])
def deleteitems(itemid):
    global items
    item=next((i for i in items if i['id']==itemid))
    return jsonify({'message':"Item deleted"})
    
if __name__ == "__main__":
    app.run(debug=True)



                             