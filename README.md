# Software Engineering

# Sternies of Tandon

## Overal Description

  - A platform that combines the users financial platforms. This will make it easier for the user to understand and track their finances. Specically in the crypto currency realm many of the new platforms do not have easy to read graphical and table visuals to track your investments. Our product will combine investment profolios into one account with graphical insight, an optional trading bot for the user to use, news sources and user choice for media coverage, security of login, possible copy trading, and much more. 

  - For instance if a user has 30% of their porfolio in Fidelity, 20% in Robinhood, 20% in Coinbase Pro, and 30% in TD Amitrade, this website would allow the user to only need to sign into this account to get an analysis of all of their finances at the same time. 

## SetUp 

  Make Prod
  - makes the "make tests" unit tests in the SoftEng repository
  - commits and pushes all modifications

  make dev_env
  - Running this will install all of the requirements from the requirements-dev.txt file, requirements.txt and the heroku requirements file. 

  make tests 
  - makes unit tests in the SoftEng repository 

  make deploy
  - runs ./venv/app/app.py which will run MySQL database and Heroku (if logged in)

  Run Heroku 
  - Its located in the venv/ folder (make sure to be logged in)
  - pip install -r requirements.txt  (make sure to have correct installations)
  - heroku login 
  - heroku local web (http://127.0.0.1:5000/)

  Update Heroku 
  - git push heroku main (update from the main branch)

  Database Setup
  - Prerequisites: PyMySQL, MAMP, PhpMyAdmin, MySQL
  - Start Servers on MAMP
  - Have commands run in Create.sql
  - Have app.py run (either on CLI or via tests)
  - Located on Port 5000 (or your own defined port)


## Run App 
  - clone repo
  - Go through SetUp 
    - make dev_env
  - heroku login 
  - WAMP login for access to database and local host
  - make deploy (or navigate to ./venv and heroku local web)

## Actionable Requirements
  - Create User (automate signing into all of their chosen finanical accounts using key pairs through MySQL database with SHA hashing) 
  - Edit User (account, finanical accounts, saved lists of tickers) 
  - Delete User
  - Aggregate stock data across user profile (select accounts, tickers, ratios, and other algorithmic statistics)
  - Visualize stocks portfolio (graphical)
  - Save Stock (save to a wishlist or another list for their convenience)


## GOALS

   - Implement bots
   - Visualize different ranges of history (6mo, 1 yr, etc.)
   - Have a bot watch market shorts (?)
   - Focus on stocks alone vs focus on crypto
   - Combining stocks with crypto is a specialty that there is not a great solution for so far → great niche audience and market
   - No centralized visual feedback on crypto stocks
   - Could use inspiration from Robinhood API
   - Implement crypto stock recommendations
   - Based on stocks invested
   - News spotlight focus based on analyst personalizations
