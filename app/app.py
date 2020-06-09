import numpy as np
import pandas as pd
import csv

from flask import Flask, jsonify, render_template, request
from sqlalchemy import func

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/comparisons')
def comparisons():

    return render_template('comparisons.html')

@app.route('/visualization1')
def visualization1():

    return render_template('visualization1.html')

@app.route('/visualization2')
def visualization2():

    return render_template('visualization2.html')

@app.route('/visualization3')
def visualization3():

    return render_template('visualization3.html')

@app.route('/visualization4')
def visualization4():

    return render_template('visualization4.html')

@app.route('/visualization5')
def visualization5():

    return render_template('visualization5.html')

@app.route('/visualization6')
def visualization6():

    return render_template('visualization6.html')

# @app.route('/visualization7')
# def visualization7():

#     return render_template('visualization7.html')

if __name__ == '__main__':
    app.run(debug=True)
