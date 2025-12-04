from flask import Flask # Importing the Flask class 
from config import Config # Importing the Config class from config.py - to manage app settings e.g. secret key
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__) # Creating an instance of the Flask class

app.config.from_object(Config) # Loading configuration settings from the Config class
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'


import routes 

