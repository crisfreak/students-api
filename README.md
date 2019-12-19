# Detalles de las rutas

|Metodo|Ruta|Función|Ejemplo|
|--|--|--|--|
|GET|/students|Muestra a todos los alumnos ingresados|/students|
|GET|/students/:rut|Muestra un alumno según su rut <br>(el rut debe ingresarse sin dígito verificador)|/students/19751590|
|POST|/students|Ingresa un alumno por body con los siguientes datos: <br> rut sin digito verificador (variable de tipo entero) <br> nombre (variable de tipo string) <br> notas (lista de floats)|/students<br>Formulario(json)<br>{<br>&nbsp;&nbsp;&nbsp;"rut":19751590,<br>&nbsp;&nbsp;&nbsp;"nombre":"Nombre del alumno",<br>&nbsp;&nbsp;&nbsp;"notas": [3.3,5.4,7]<br>}|
