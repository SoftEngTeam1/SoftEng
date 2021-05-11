# from flask import Flask
from flask import Flask, render_template, request, session, url_for, redirect, flash, abort
import robin_stocks as robin

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


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