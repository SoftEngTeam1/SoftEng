# from flask import Flask
from flask import Flask, render_template, request, session, url_for, redirect, flash, abort
import pymysql.cursors
app = Flask(__name__)

#UNCOMMENT WHEN SET UP
#Configure MySQL
#conn = pymysql.connect(host='localhost',
#                       port=8889, #may need to change dependant on if youre using XAMPP, MAMP, WAMP, etc.
#					   user='root',
#					   password='root',
#					   db='users',
#					   charset='utf8mb4',
#					   cursorclass=pymysql.cursors.DictCursor)


@app.route('/')
def index():
    return render_template('index.html')

#ROBINHOOD CODE#
#import robin_stocks as robin

#@app.route('/robin_login', methods=['GET', 'POST'])
#def robin_login():
#    USERNAME = input("Enter Robinhood Username: ")
#    PASS = getpass("Enter Robinhood Password: ")
#    try:
#        robin.login(USERNAME, PASS, store_session=False)
#        return redirect(url_for('home'))
#    except Exception:
#        # print("Invalid login attempt to Robinhood.")
#        # print("Attempts left: {}".format((3 - attempt - 1)))
#        error = 'Invalid username or password'
#        return render_template('login.html', error=error)

#GENERIC USER CODE#

# Define route for login
@app.route('/generic_login')
def generic_login():
    return render_template('generic_login.html')


#authenticates and checks to see if user exits
@app.route('/generic_login_auth', methods=['GET', 'POST'])
def cus_login_auth():
	email = request.form['email']
	password = request.form['password']
	cursor = conn.cursor()
    #may need to change password encrpytion
	query = 'SELECT * FROM customer WHERE email = %s and password = MD5(%s)' #this is for password encryption, we dont necessarily need to do this
	cursor.execute(query, (email, password))
	data = cursor.fetchone()
	cursor.close()
	error = None
	if(data):
		#creates a session for the the user
		#session is a built in
		session['username'] = email
		return redirect(url_for('index')) #i can make a homepage
	else:
		#returns an error message to the html page
		error = 'Invalid login or email'
		return render_template('generic_login.html', error=error)

if __name__ == "__main__":

	app.run('127.0.0.1', 5000, debug = True)
 
