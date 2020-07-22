
import datetime

from flask import Flask,render_template,request
# import mysql
import mysql.connector
import mysql.connector
from datetime import datetime
# from mysql.connector import errorcode

app = Flask(__name__)

connection = mysql.connector.connect(host='localhost',
                                    database='dev',
                                    user='root',
                                    password='')
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
    	phone = request.form.get('phone_num')
    	msg = request.form.get('msg')
    	cursor.execute(f"insert into contact(name, phone_num, email, msg,date) values('{name}', '{phone}', '{email}', '{msg}','{datetime.now()}')")
    	connection.commit()
    	cursor.close()
		# connection.close()
    	# return 'success'
    return render_template('contact.html')

app.run(debug=True)

