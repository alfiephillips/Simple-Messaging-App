from flask import Blueprint
from flask import Flask, render_template, url_for, redirect, request, session, jsonify, flash, Blueprint
# from .database import DataBase

view = Blueprint("views", __name__)


# GLOBAL CONSTANTS
NAME_KEY = 'name'
MSG_LIMIT = 20

# VIEWS

@view.route("/", methods=["GET"])
def home():
    if request.method != "GET":
        return jsonify({
            "Error": "You can only perform get requests to this page."
        })

    return jsonify({
        "Message": "Welcome to the API!"
    })