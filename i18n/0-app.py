#!/usr/bin/env python3
"""Setup a basic Flask app"""
from flask import Flask, render_template


app = Flask(__name__)
babel = Babel(app)


@app.route("/")
def index():
    """create a simple route that simply outputs"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
