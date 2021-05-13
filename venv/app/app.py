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
import robin_stocks as robin

# Define route for login
@app.route('/robin_login')
def robin_login():
    return render_template('robin_login.html')

#TODO 
@app.route('/robin_login_auth', methods=['GET', 'POST'])
def robin_login_auth():
#    USERNAME = input("Enter Robinhood Username: ")
#    PASS = getpass("Enter Robinhood Password: ")
    username = request.form['username']
    password = request.form['password']
    print("USERNAME *(*********",username)
    try:
        robin.login(username, password, store_session=False)
        #TODO TEMP to render to index
        return render_template('index.html', error=error)
        # return redirect(url_for('home'))
    except Exception:
        # print("Invalid login attempt to Robinhood.")
        # print("Attempts left: {}".format((3 - attempt - 1)))
        error = 'Invalid username or password'
        return render_template('robin_login.html', error=error)

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
		return redirect(url_for('home')) #i can make a homepage
	else:
		#returns an error message to the html page
		error = 'Invalid login or email'
		return render_template('generic_login.html', error=error)

# @app.route('/generic_register', methods=['GET', 'POST'])
# def cus_register():
# 	return render_template('generic_register.html')

# @app.route('/generic_register_auth', methods=['GET', 'POST'])
# def generic_register_auth():
#     email = request.form['email']
#     cursor = conn.cursor()
#     query = 'SELECT * FROM users WHERE email = %s'
#     cursor.execute(query, (email))
#     data = cursor.fetchone()
#     error = None
#     if(data):
#         #If the previous query returns data, then user exists
#         error = "This user already exists! Login instead."
#         return render_template('generic_register.html', error = error)
#     else:
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']
#         ins = '''INSERT INTO user (name,email,password) VALUES (%s,%s,MD5(%s))'''
#         cursor.execute(ins, (name,email,password))
#         conn.commit()
#         cursor.close()
#         return redirect('/generic_login')


# @app.route('/home', methods=['GET', 'POST'])
# def homepage():
#     #Jasmine's code here: 
#     email = session['username']
#     return render_template('home.html')


if __name__ == "__main__":
	app.run('127.0.0.1', 5000, debug = True)