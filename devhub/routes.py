from flask import render_template, redirect, request, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from devhub import app, db, mongo
from devhub.models import User

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
        existing_user = bool(User.query.filter_by(username=request.form.get('username')).first())

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash():
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
        if bool(User.query.filter_by(username=request.form.get('username')).first()):
            flash('That username is already taken - please try again.')
        else:
            user = User(first_name=request.form.get('firstname'),
            last_name=request.form.get('lastname'), 
            username=request.form.get('username').lower(), 
            password=generate_password_hash(request.form.get('password')))
            db.session.add(user)
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