from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'pythondb'

mysql= MySQL(app)


@app.route("/")
def home():
    return "Hello User!!!"

@app.route("/register",methods =['POST','GET'])
def register():
    if request.method== 'GET':
       cursor= mysql.connection.cursor()
       cursor.execute('''SELECT * FROM user''')
       res= cursor.fetchall()
       cursor.close()
       return render_template("register.html",data=res)
    
    if request.method== 'POST':
       name = request.form['name']
       email = request.form['email']
       phone = request.form['phone']
       college = request.form['college']
       cursor = mysql.connection.cursor()
       cursor.execute('''INSERT INTO user(name,email,phone,college) VALUES(%s,%s,%s,%s)''',(name,email,phone,college))
       mysql.connection.commit()
       cursor.close()
       return "Data inserted successfully"

    

if __name__ == "__main__":
  app.run(host= 'localhost')