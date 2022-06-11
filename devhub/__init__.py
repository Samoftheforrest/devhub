import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
import cloudinary
import cloudinary.uploader
from werkzeug.utils import secure_filename
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')
if os.environ.get("DEVELOPMENT") == "True":
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    
app.config['UPLOAD_FOLDER'] = "static/uploads/"

db = SQLAlchemy(app)
mongo = PyMongo(app)
ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]

cloudinary.config(
    cloud_name="samforrest",
    api_key="483791879975147",
    api_secret=os.environ.get("API_SECRET")
)

from devhub import routes