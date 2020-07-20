from flask import Flask,render_template,request

import mysql.connector
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

connection = mysql.connector.connect(host='localhost',
                                         database='dev',
                                         user='root',
                                         password='root')
cursor = connection.cursor()

#mysql = MySQL(app)	# Init

@app.route('/')
def home():
    return render_template('index.html')
# app.run() 
@app.route('/about')
def about():
    return render_template('about.html')
# app.run() 
@app.route('/contact',methods=['GET','POST'])
def contact():
    if (request.method=='POST'):
    	name = request.form.get('name')
    	email = request.form.get('email')
    	phone = request.form.get('phone')
    	msg = request.form.get('message')
    	cursor.execute(f"insert into contacts(name, phone, email, message) values('{name}', '{phone}', '{email}', '{msg}')")
    	connection.commit()
    	cursor.close()
    	return 'success'
    return render_template('contact.html')

app.run(debug=True)
