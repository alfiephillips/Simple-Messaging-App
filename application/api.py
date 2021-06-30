from application.utilities import remove_seconds_from_messages
from flask import Blueprint
from flask import Flask, render_template, url_for, redirect, request, session, jsonify, flash, Blueprint
from .database import DataBase

api = Blueprint("api", __name__)

# GLOBAL CONSTANTS

NAME_KEY = 'name'
MSG_LIMIT = 20

# API

@api.route("/get-name", methods=["GET"])
def get_name():
    """
    Gets the current user name
    :return: JSON: name<object>
    """

    if request.method == "GET":
        data = {"name": ""}
        if NAME_KEY in session:
            data = {"name": session[NAME_KEY]}

        return jsonify(data)

    else:
        return jsonify({
            "Error": "Request not authorized."
        })

@api.route("/get-messages", methods=["GET"])
def get_messages():
    """
    Get all the messages from the database
    :return: JSON: messages<list>
    """

    if request.method == "GET":
        db = DataBase()
        messages = remove_seconds_from_messages(db.get_all_messages(MSG_LIMIT))

        return jsonify(messages)

    else:
        return jsonify({
            "Error": "Request not authorized."
        })

@api.route("/get-history", methods=["GET"])
def get_history(name):
    """
    :param name: str
    :return: messages<list> - :constraint: user
    """

    if request.method == "GET":
        db = DataBase()
        messages = remove_seconds_from_messages(db.get_messages_by_name(name))
        
        return messages

    else:
        return jsonify({
            "Error": "Request not authorized"
        })