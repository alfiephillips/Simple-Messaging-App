from flask import Blueprint
from flask import Flask, render_template, url_for, redirect, request, session, jsonify, flash, Blueprint
from .database import DataBase
from .api import get_history

view = Blueprint("views", __name__)


# GLOBAL CONSTANTS
NAME_KEY = 'name'

# VIEWS

@view.route("/login", methods=["GET", "POST"])
def login():
    """
    Displays the main login page and handles
    saving the user's name in session
    :exception POST:
    :return: None
    """

    if request.method == "POST":
        name = request.form["inputName"]
        if len(name) >= 4:
            session[NAME_KEY] = name
            flash(f"You have been successfully logged in {name}!")
            return redirect(url_for("views.home"))

        else:
            flash("1Name must be longer than 3 characters!")

    return render_template("login.html", **{"session": session})

@view.route("/logout")
def logout():
    """
    Logs out the user by popping name from the session
    :return: views.login
    """

    session.pop(NAME_KEY, None)
    flash("0You were logged out.")
    return redirect(url_for("views.login"))

@view.route("/")
def home():
    """
    Displays the homepage if user is logged in
    :return: None
    """

    if NAME_KEY not in session:
        flash("0You must be logged in to view this page!")
        return redirect(url_for("views.login"))

    return render_template("index.html", **{"session": session})

@view.route("/history")
def history():
    """
    View message history to the user
    :return: None
    """
    if NAME_KEY not in session:
        flash("0Please login before viewing message history")
        return redirect(url_for("views.login"))

    messages = get_history(session[NAME_KEY])
    return render_template("history.html", **{"history": messages})

