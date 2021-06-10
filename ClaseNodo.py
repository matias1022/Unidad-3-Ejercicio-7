from ClasePersonal import Personal

from ClaseDocente import Docente

from ClaseApoyo import Apoyo

from ClaseInvestigador import Investigador

from ClaseDocenteInvestigador import DocenteInvestigador


class Nodo:
    __personal=None
    __siguiente=None

    def __init__(self,personal):
        self.__personal=personal
        self.__siguiente=None

    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__personal

    def getTipo(self):
        tipo=None
        if type(self.__personal)==Docente:
            tipo='Docente'
        elif type(self.__personal)==Apoyo:
            tipo='Personal Apoyo'
        elif type(self.__personal)==Investigador:
            tipo='Investigador'
        else:
            tipo='Docente Investigador'
        return tipo

    def __str__(self):
        return f'''{self.__personal}'''
