from typing import List
from statistics import mean
class Student():
    rut:int 
    nombre:str
    notas:List[float]

    def __init__(self, rut:int, nombre:str, notas:List[float] = []):
        self.rut = rut
        self.nombre = nombre
        self.notas = notas

    @property
    def promedio(self) -> float:
        if len(self.notas) == 0:
            return 0.0
        else:
            return round(mean(self.notas), 1)

    @property
    def estado(self) -> str:
        if self.promedio >= 4.0:
            return "Aprobado"
        else:
            return "Reprobado"
    
    def toDict(self) -> dict:
        return {
            "rut": self.rut, 
            "nombre": self.nombre,
            "promedio": self.promedio,
            "notas": self.notas,
            "estado": self.estado
        }

        
