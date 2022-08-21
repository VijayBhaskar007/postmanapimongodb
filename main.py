from flask import Flask ,request,jsonify
import  mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect("Use your ongodb cluster connection like - "host = "localhost" , user = 'root' , passwd = "Jaijai1@11""
cursor = mydb.cursor()
cursor.execute("create database if not exists taskdb")
cursor.execute("create table if not exists taskdb.tasktable (name varchar(30) , number int)")

@app.route('/insert',methods = ['POST'])
def insert():
    if request.method=='POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into taskdb.tasktable  values(%s , %s)",(name ,number))
        mydb.commit()
        return jsonify(str('Succesfully Inserted'))

@app.route("/update" , methods= ['POST'])
def update():
    if request.method=='POST':
         get_name = request.json['get_name']
         cursor.execute("update taskdb.tasktable set number = number + 500 where name = %s ",(get_name,))
         mydb.commit()
         return jsonify(str("Udated Sccessfully"))

@app.route("/delete" , methods= ['POST'])
def delete():
    if request.method == 'POST':
        name_del = request.json['name_del']
        cursor.execute("delete from taskdb.tasktable where name = %s",(name_del,))
        mydb.commit()
        return jsonify(str("Dleted Sccessfully"))

@app.route("/fetch",methods = ['POST','GET'])
def fetch_data():
    cursor.execute("select * from taskdb.tasktable")
    l = []
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))
    
if __name__ == '__main__':
    app.run()  
  
 
 """
 on postman API tool need to provide data-
Using URL like: 127.0.0.1: 5000/insert
Need to select; body-raw-json and click on 'Send' button
Also go to MONGODB and use select statement to see the changes
    
    {
    "name" : "nizam",
    "number":6867
}

"""
