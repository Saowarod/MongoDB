from flask import Flask, request, jsonify
# from bson import json_util
import pymongo

#Init app
app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://admin:CDVfxi72080@10.100.2.124")
mydb = myclient["MongoDB"]
mycollection = mydb["user"]
# admin:CDVfxi72080@node9147-advweb-09.app.ruk-com.cloud

# mydic = {"no":"01","name":"Saowarod Sommo","position":"IT Support","age":"21"}
# x = mycollection.insert_one(mydic)

# mylist = [{ "no" : "02", "name" : "Taeyeon Kim", "position" : "HR", "age" : "30" },
#           { "no" : "03", "name" : "Tiffany Hwang", "position" : "CEO", "age" : "30" },
#           ]
# x = mycollection.insert_many(mylist)
# print(x.inserted_ids)

# myquery = {"position":{"$regex":"^C"} }
# mycollection.delete_one(myquery)

# mydoc = mycollection.find(myquery)

# for x in mydoc:
#     print(x)

# myquery = {"no":"01"}
# newvalue = {"$set": {"no":"04"}}
# mycollection.update_one(myquery,newvalue)
# mydoc = mycollection.find(myquery).limit(1)

# mydoc = mycollection.find(myquery)
# mydoc = mycollection.delete_one(myquery)


@app.route('/user', methods=['GET'])
def get_user():
   user = []
   for f in mycollection.find():
       user.append({'no' : f['no'], 'name' : f['name']})
   return jsonify({'result' : user})

@app.route('/user', methods=['POST'])
def add_user():
   no = request.json['no']
   name = request.json['name']
   position = request.json['position']
   age = request.json['age']
   user_id = mycollection.insert({'no': no, 'name':name, 'position': position, 'age': age})
   new_user = mycollection.find_one({'_id': user_id})
   output = {'no' : new_user['no'], 'name' : new_user['name'], 'position' : new_user['position'], 'age' : new_user['age']}
   return jsonify({'result' : output})

@app.route('/user', methods=['DELETE'])
def delete_user():
    number = {'no' : request.args["no"]}
    print(number)
    user = mycollection.delete_one(number)
    return jsonify({'result' : "delete"})

@app.route('/user', methods=['PUT'])
def update_user():
   no = request.json['no']
   name = request.json['name']
   position = request.json['position']
   age = request.json['age']
#    user = mycollection.find_one({'no': no})
   newuser = mycollection.update_one({'no': no},{'$set': {'no': no, 'name':name, 'position': position, 'age': age}})
#    output = {'no' : newuser['no'], 'name' : newuser['name'], 'position' : newuser['position'], 'age' : newuser['age']}
   return jsonify({'result' : "update"})



@app.route('/', methods=['GET'])
def get():
    return jsonify({'ms': 'Hello'})

# Run Server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)



















