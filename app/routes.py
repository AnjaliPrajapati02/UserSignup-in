# routes.py
from app import app
import os
from flask import Flask, render_template, request,session, redirect, url_for, flash
from models import Credentials,db
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


# def initialize_routes(app):
#     from routes import hello
#     app.add_url_rule('/', 'hello', hello)
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        new_user = Credentials(username=username,email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()  

        flash('User signed up successfully!')
        # return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        # print(username)
        password = request.form.get("password")
        # print(password)


        # Check if both username and password are provided
        if not (username and password):
            flash("Please provide both username and password.")
            return render_template('login.html')

        # Query the database for the user
        user = Credentials.query.filter_by(username=username).first()
        # print(user)

        if user:
            # Check if the provided password matches the stored password
            if user.check_password(password):
                # Store user information in session
                session['id'] = user.id
                session['username'] = user.username
                # You can store additional user information in session if needed

                flash("Login successful!")
                return render_template("profile.html",user=user)
            else:
                flash("Invalid password. Please try again.")
        else:
            flash("Invalid username. Please try again.")

    return render_template('login.html')



@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template("profile.html")


@app.route("/edit/<int:id>", methods=['GET','POST'])
def edit(id):
    user = Credentials.query.filter_by(id=id).first()
    return render_template("update.html",user=user)

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    # user = Credentials.query.filter_by(id=id).first()
    user = Credentials.query.get(id)

    if request.method == "POST" and user:
        username = request.form.get("username")
        email = request.form.get("email")


        user.update_profile(username, email)
        return render_template("profile.html", user=user)
    return render_template("login.html", user=user)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('home'))

