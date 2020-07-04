from flask import Flask, render_template, request, redirect, url_for
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome home"

@app.route('tasks/create')







# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)