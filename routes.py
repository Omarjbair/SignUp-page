from flask import render_template, request, flash, redirect, url_for

from app import app
from models import Signup, db


@app.route("/")
@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        if not name:
            flash("Please enter name")
            return redirect(url_for('signup'))
        if not email:
            flash("Please enter email")
            return redirect(url_for('signup'))
        if not password:
            flash("Please enter password")
            return redirect(url_for('signup'))
        else:
            if db.session.query(db.exists().where(Signup.email == email)).scalar():
                flash("This email is used before")
                return redirect(url_for('signup'))
            else:
                if "@" in email and len(password) >= 8:
                    signup_data = Signup(name=name, email=email, password=password)
                    db.session.add(signup_data)
                    db.session.commit()
                    return redirect(url_for('welcome'))
                else:
                    if len(password) < 8:
                        flash("Your password less than 8 characters")
                        return redirect(url_for('signup'))
    return render_template('index.html')


@app.route('/welcome', methods=["GET", "POST"])
def welcome():
    signup_info = Signup.query.all()
    return render_template('welcome.html', signup=signup_info[-1].name)
