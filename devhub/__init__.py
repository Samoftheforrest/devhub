import os
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
import cloudinary
import cloudinary.uploader
from werkzeug.utils import secure_filename
if os.path.exists("env.py"):
    import env

# flask
app = Flask(__name__)

# mongodb
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')
mongo = PyMongo(app)

# cloudinary
app.config['UPLOAD_FOLDER'] = os.environ.get("UPLOAD_FOLDER")
ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]

cloudinary.config(
    cloud_name=os.environ.get("CLOUD_NAME"),
    api_key=os.environ.get("API_KEY"),
    api_secret=os.environ.get("API_SECRET")
)

# postgresql
if os.environ.get("DEVELOPMENT") == "True":
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://")
    app.config['SQLALCHEMY_DATABASE_URI'] = uri

db = SQLAlchemy(app)

from devhub import routes