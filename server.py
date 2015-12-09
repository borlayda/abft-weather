#!/usr/bin/env python
from matrix import *
from flask import Flask, request
app = Flask(__name__)

@app.route("/verify", methods=["POST"])
def verify():
    matrices = request.get_json("matrices")
    checksums = request.get_json("checksums")
    summerize = make_summ(matrices)
    iterate_matrix(summerize, checksums[0], checksums[1])
    return summerize

if __name__ == "__main__":
    app.run('0.0.0.0', 8080)
