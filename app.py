from flask import Flask, request, jsonify
# from bson import json_util
import pymongo

#Init app
app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://admin:CDVfxi72080@10.100.2.124") #เชื่อมต่อ Mongo จาก Ruk-com
mydb = myclient["MongoDB"] #ชื่อ Database ใน Mongo
mycollection = mydb["user"] #ชื่อตารางใน Mongo
mycol = mydb["time"]
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

# Get user
@app.route('/user', methods=['GET'])
def get_user(): #ชื่อ Function
   user = [] #สร้างตัวแปรมาเก็บข้อมูลใน Array
   for f in mycollection.find(): #ใช้ Loop for ในการดึงข้อมูลมาเก็บ
       user.append({'no' : f['no'], 'name' : f['name'], 'position' : f['position'], 'age' : f['age']})
   return jsonify({'result' : user}) #return ข้อมูลมาแสดง

# Get time
@app.route('/time', methods=['GET'])
def get_time(): #ชื่อ Function
   time = [] #สร้างตัวแปรมาเก็บข้อมูลใน Array
   for t in mycollection.find(): #ใช้ Loop for ในการดึงข้อมูลมาเก็บ
       time.append({'no' : t['no'], 'id_time' : t['id_time'], 'time' : t['time']})
   return jsonify({'result' : time}) #return ข้อมูลมาแสดง

#Create user
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

#delete user
@app.route('/user', methods=['DELETE'])
def delete_user():
    number = {'no' : request.args["no"]}
    print(number)
    user = mycollection.delete_one(number)
    return jsonify({'result' : "delete"})

#update user
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


#หน้าแรกให้แสดงข้อความ
@app.route('/', methods=['GET'])
def get():
    return jsonify({'ms': '"welcome to MongoDB'})

# Run Server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)



















