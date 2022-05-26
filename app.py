import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists('env.py'):
    import env


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABSE_URI'] = 'postgres://wzlawbygbnkcfw:31237ca27f9c2fadb006e5c13c531feecf4525d6f845fcb8dfdfaba5dc9b2ff4@ec2-63-35-156-160.eu-west-1.compute.amazonaws.com:5432/d81u0d8dnje45o'
db = SQLAlchemy(app)

class User(db.Model):
    """ User model """

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)


app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

# pages
# homepage
@app.route("/")
def home_page():
    """
    Renders the homepage
    """
    projects = list(mongo.db.projects.find())
    return render_template("pages/home.html", projects=projects)


# login
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Handles user login and renders the login form
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("home_page", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("pages/auth.html", register=False)


@app.route("/logout")
def logout():
    """
    Handles log out functionality by removing the user from the session
    """
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# register
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Handles registration and renders the registration form
    """
    if request.method == "POST":
        first_name = request.form.get('firstname')
        last_name = request.form.get('lastname')
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user:
            flash('Username already exists')
            return redirect(url_for(register))

        new_user = User(first_name=first_name, 
                        last_name=last_name, 
                        username=username, password=generate_password_hash(password))

        db.session.add(new_user)
        db.session.commit()


    return render_template("pages/auth.html", register=True)


# add a project page
@app.route("/new-project")
def add_project():
    """
    Handles adding a new project and renders the add project form
    """
    return render_template("add-project.html")


# edit project page
@app.route("/edit-project")
def edit_project():
    """
    Handles editing a project and renders the edit project form
    """
    return render_template("edit-project.html")


# individual project page
@app.route("/project") # add project name to end of URL
def go_to_project():
    """
    Renders individual projects
    """
    return render_template("project.html")


# profile page
@app.route("/profile") # add username to end of URL
def go_to_profile():
    """
    Renders profile pages
    """
    return render_template("profile.html")


# edit profile page
@app.route("/edit-profile")
def edit_profile():
    """
    Handles editing session user's profile and renders the edit profile form
    """
    return render_template("edit-profile.html")


# contact page
@app.route("/contact")
def contact():
    """
    Renders the contact us form
    """
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)