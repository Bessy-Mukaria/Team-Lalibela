from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template ("index.html")

@app.route("/analysis")
def index():
    return render_template ("analysis.html")

@app.route("/Start Predictions")
def index():
    return render_template ("Start Predictions.html")

