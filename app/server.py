from flask import Flask, render_template, request
import json
from flask_cors import CORS
import numpy as np
from math import floor

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot.html')
def plot():
    return render_template('')

if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True)
