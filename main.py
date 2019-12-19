import json
from flask import Flask, request, Response
from http import HTTPStatus
from models.student import Student
from typing import List

students : List[Student] = []

app = Flask(__name__)

@app.route("/")
def hello():
    response = Response(
        "Los endpoints dispnibles son: <br/> GET /students<br/> GET /students/:rut <br/> POST /students"
    )
    return response

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
    else:
        form = request.json
        #variables que contienen el rut, nombre y notas respectivamente
        rut = form['rut']
        name = form ['nombre']
        grades = form['notas']
        #validación de la forma de ingreso de datos
        if 'rut' in form and 'nombre' in form and 'notas' in form:
            for stud in students:
                #Verifica que no exista el rut que se está ingresando
                if rut == stud.rut:
                    response = Response(
                    json.dumps({"msg": "Este Alumno ya fue ingresado"}),
                    status=HTTPStatus.NOT_ACCEPTABLE,
                    mimetype="application/json"
                    )
                    return response
            #Luego de verificar que no exista, procede a agregarlo
            student = Student (rut, name,grades)
            students.append(student)
            response = Response(
                json.dumps({"msg": "Alumno ingresado exitosamente"}),
                status=HTTPStatus.CREATED,
                mimetype="application/json"
                )
        #Entrega este mensaje en caso de no ingresar la totalidad de los datos        
        else:
            response = Response(
                json.dumps({"msg": "No se ingresaron los datos de manera correcta"}), 
                status=HTTPStatus.BAD_REQUEST,
                mimetype="application/json"
                )
            return response   
    return response

@app.route("/students/<rut>", methods=["GET"])
def get_student(rut : str):
    #Validación de que se este ingresando un rut y no otros caracteres
    if rut.isdigit() != True:
        response = Response(
            json.dumps({"msg" : "Rut inválido"}), 
            status=HTTPStatus.BAD_REQUEST, 
            mimetype="application/json"
        )
    else:
        rut = int(rut)
        #Busca al estudiante según su rut
        for stud in students:
            if rut == stud.rut:
                response = Response(
                    json.dumps(
                        stud, 
                        default = lambda s: s.toDict()
                    ), 
                    status=HTTPStatus.OK,
                    mimetype="application/json"
                )
                return response               
        #Mensaje en caso de que no encontrarse el rut
        response = Response(
            json.dumps(
                {"msg": "No existe alumno ingresado con ese rut"}
            ), 
            status=HTTPStatus.NOT_FOUND,
            mimetype="application/json"
        )               
        return response
    return response
    
if __name__ == "__main__":
    app.run()