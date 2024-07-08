import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
