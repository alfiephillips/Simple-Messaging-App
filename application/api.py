from flask import Blueprint
from flask import Flask, render_template, url_for, redirect, request, session, jsonify, flash, Blueprint
from .database import DataBase

api = Blueprint("api", __name__)

# GLOBAL CONSTANTS

NAME_KEY = 'name'
MSG_LIMIT = 20