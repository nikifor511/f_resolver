from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

fl_app = Flask(__name__)

fl_app.config['SECRET_KEY'] = 'you-will-never-guess'
fl_app.config.from_object(Config)
db = SQLAlchemy(fl_app)
migrate = Migrate(fl_app, db)

from routes import *
from models import *


if __name__ == '__main__':
    print("init...")
    fl_app.run()