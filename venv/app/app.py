# from flask import Flask
from flask import Flask, render_template, request, session, url_for, redirect, flash, abort
import robin_stocks as robin

app= Flask(__name__)

@app.route('/')
def index():
    # return "<h1>Welcome to the group Sternies of Tandon</h1>"
    return render_template('index.html')


# @app.route('/loginAuth', methods=['GET', 'POST'])
# def loginAuth():
    # # grabs information from the forms
    # username = request.form['username']
    # password = request.form['password'] + SALT
    # hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    # query = 'SELECT username, password FROM person WHERE username = %s and password = %s'
    # data = run_sql_one(query, (username, hashed_password))
    # error = None
    # if (data):
    #     # creates a session for the the user
    #     # session is a built in
    #     session['username'] = data['username']
    #     return redirect(url_for('home'))
    # else:
    #     # returns an error message to the html page
    #     error = 'Invalid username or password'
    #     return render_template('login.html', error=error)

@app.route('/robin_login', methods=['GET', 'POST'])
def robin_login():
    USERNAME = input("Enter Robinhood Username: ")
    PASS = getpass("Enter Robinhood Password: ")
    try:
        robin.login(USERNAME, PASS, store_session=False)
        return redirect(url_for('home'))
    except Exception:
        # print("Invalid login attempt to Robinhood.")
        # print("Attempts left: {}".format((3 - attempt - 1)))
        error = 'Invalid username or password'
        return render_template('login.html', error=error)



# Define route for login
@app.route('/login')
def login():
    return render_template('login.html')