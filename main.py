import json
from flask import Flask, request, Response
from http import HTTPStatus
from models.student import Student
from typing import List

students : List[Student] = []

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!", 200

@app.route("/students/", methods=["GET", "POST"])
def get_students():
    if request.method == "GET":
        response = Response(
            json.dumps(
                students, 
                default = lambda s: s.toDict()
            ), 
            status=HTTPStatus.OK,
            mimetype="application/json"
        )
    elif request.method == "POST":
        form = request.json
        print(form)
        return "POST", 200
    else:
        response = Response(
            json.dumps({"msg" : "Método inválido"}), 
            status=HTTPStatus.METHOD_NOT_ALLOWED, 
            mimetype="application/json"
        )
    return response

@app.route("/students/<rut>", methods=["GET"])
def get_student(rut : str):
    if rut.isdigit() != True:
        response = Response(
            json.dumps({"msg" : "Rut inválido"}), 
            status=HTTPStatus.BAD_REQUEST, 
            mimetype="application/json"
        )
    else:
        rut = int(rut)
        print(rut)
        return "GET", 200
    return response

if __name__ == "__main__":
    app.run()