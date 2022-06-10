from flask import render_template, redirect, request, url_for, flash, session
import cloudinary
import cloudinary.uploader
from datetime import datetime
from werkzeug.utils import secure_filename
from bson.objectid import ObjectId
from sqlalchemy import func
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
    return render_template("pages/home.html", projects=projects, home_active=True)


# login
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Handles user login and renders the login form
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = bool(User.query.filter_by(
            username=func.lower(request.form.get('username'))).first())
        check_user = User.query.filter_by(username=func.lower(
            request.form.get('username'))).first()

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(check_user.password,
                                   request.form.get('password')):
                session["user"] = request.form.get("username").lower()
                flash(f"Welcome, {str(check_user).capitalize()}")
                return redirect(url_for("home_page", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash('Incorrect username/password. Please try again.')
            return redirect(url_for("login"))
    return render_template("pages/auth.html", register=False, login_active=True)


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
        password = request.form.get('password')
        confirm_password = request.form.get('confirmpassword')
        # check if the username already exists
        if bool(User.query.filter_by(
                username=func.lower(request.form.get('username'))).first()):
            flash('That username is already taken - please try again.')
        # check if both passwords are the same
        elif not password == confirm_password:
            flash('Please make sure that both passwords are identical')
        else:
            user = User(first_name=request.form.get('firstname'),
                        last_name=request.form.get('lastname'),
                        username=request.form.get('username').lower(),
                        password=generate_password_hash(
                            request.form.get('password')))
            db.session.add(user)
            db.session.commit()

    return render_template("pages/auth.html", register=True)


# add a project page
@app.route("/new-project", methods=["GET", "POST"])
def add_project():
    """
    Handles adding a new project and renders the add project form
    """
    if request.method == "POST":
        image = request.files['projectimage']
        upload_result = cloudinary.uploader.upload(image)
        current_date = datetime.now()
        date = current_date.strftime("%x")
        project = {
            "project_name": request.form.get('projectname'),
            "project_description": request.form.get('projectdescription'),
            "project_image": upload_result["secure_url"],
            "project_image_name": request.form.get('filename'),
            "created_by": session['user'],
            "date_posted": date,
            "live_link": request.form.get('livelink'),
            "repo_link": request.form.get('repolink'),
            "project_tags": request.form.getlist('checked')
        }
        mongo.db.projects.insert_one(project)
        project_name = request.form.get('projectname')
        flash(f'{project_name} successfully added')
            
    return render_template("pages/add-or-edit-project.html",
                            add_project=True,
                            project_active=True)


# edit project page
@app.route("/edit-project/<project_id>", methods=["GET", "POST"])
def edit_project(project_id):
    """
    Handles editing a project and renders the edit project form
    """
    if request.method == "POST":
        image = request.files['projectimage']
        upload_result = cloudinary.uploader.upload(image)
        submit = {
            "project_name": request.form.get('projectname'),
            "project_description": request.form.get('projectdescription'),
            "project_image": upload_result["secure_url"],
            "project_image_name": request.form.get('filename'),
            "created_by": session['user'],
            "live_link": request.form.get('livelink'),
            "repo_link": request.form.get('repolink'),
            "project_tags": request.form.getlist('checked')
        }
        mongo.db.projects.update_one({"_id": ObjectId(project_id)}, {"$set": submit})
        flash(f'Your project has been successfully updated')

    project = mongo.db.projects.find_one({"_id": ObjectId(project_id)})
    return render_template("pages/add-or-edit-project.html", edit_project=True, project_active=True, project=project)


# project deletion warning
@app.route("/warning/<project_id>")
def warning(project_id):

    project=mongo.db.projects.find_one({"_id": ObjectId(project_id)})
    projects = list(mongo.db.projects.find())
    return render_template("pages/home.html", project=project, projects=projects, modal=True)


# delete project
@app.route("/delete-project/<project_id>")
def delete_project(project_id):
    mongo.db.projects.delete_one({"_id": ObjectId(project_id)})
    flash('Project deleted')
    return redirect(url_for("home_page"))


# individual project page
@app.route("/project")
def go_to_project():
    """
    Renders individual projects
    """
    return render_template("pages/project.html")


# profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def go_to_profile(username, active_page):
    """
    Renders profile pages
    """
    # grab the session user's username from the database
    username = User.query.filter_by(username=username).first()
    user = mongo.db.users.find_one({"account_name": str(username)})
    projects = list(mongo.db.projects.find({"created_by": str(username)}))
    active_page = active_page
    return render_template("pages/profile.html", projects=projects, username=username, user=user, active_page=True)


# edit profile page
@app.route("/edit-profile/<user>", methods=["GET", "POST"])
def edit_profile(user):
    """
    Handles editing session user's profile and renders the edit profile form
    """
    if request.method == "POST":
        image = request.files['projectimage']
        upload_result = cloudinary.uploader.upload(image)
        submit = {
            "name": request.form.get('name'),
            "user_bio": request.form.get('userbio'),
            "user_image": upload_result["secure_url"],
            "user_image_name": request.form.get('filename'),
        }
        mongo.db.users.update_one({"account_name": str(user)}, {"$set": submit})
        flash(f'Your profile has been successfully updated')

    user = mongo.db.users.find_one({"account_name": str(user)})
    return render_template("pages/edit-profile.html", user=user, profile_active=True)


# contact page
@app.route("/contact")
def contact():
    """
    Renders the contact us form
    """
    return render_template("pages/contact.html", contact_active=True)
