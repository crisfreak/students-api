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
        #validación de la forma de ingreso de datos
        if 'rut' in form and 'nombre' in form and 'notas' in form:
            stud = Student (form['rut'], form['nombre'],form['notas'])
            students.append(stud)
            response = Response(
                json.dumps({"msg": "Alumno ingresado exitosamente"}),
                status=HTTPStatus.CREATED,
                mimetype="application/json"
            )
            return response
        
        else:
            response = Response(
                json.dumps({"msg": "No se ingresaron los datos de manera correcta"}), 
                status=HTTPStatus.BAD_REQUEST,
                mimetype="application/json"
                )
            return response   

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
        for i in range(len(students)):
            if int(rut) == students[i].rut:
                response = Response(
                    json.dumps(
                        students[i], 
                        default = lambda s: s.toDict()
                    ), 
                    status=HTTPStatus.OK,
                    mimetype="application/json"
                )               
                return response
    return response

if __name__ == "__main__":
    app.run()