# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def addition():
    """ Addition for params a and b"""

    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a, b))

@app.route("/sub")
def subtract():
    """ Subtract b param from a param"""

    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(sub(a, b))

@app.route("/mult")
def multiply():
    """Multiply a and b params"""

    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(mult(a, b))

@app.route("/div")
def divide():
    """ Subtract b param from a param"""

    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(div(a, b))


operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """will compute the chosen operator math on the given a and b params"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(operators[oper](a, b))