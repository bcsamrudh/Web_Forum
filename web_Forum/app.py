from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SECRET_KEY"]="5tuUD978NHJ@"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"


db=SQLAlchemy(app)
migrate=Migrate(app,db)

import web_forum