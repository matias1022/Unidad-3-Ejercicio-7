from pathlib import Path

import json

from ClaseLista import Lista

from ClasePersonal import Personal

from ClaseDocente import Docente

from ClaseApoyo import Apoyo

from ClaseInvestigador import Investigador

from ClaseDocenteInvestigador import DocenteInvestigador

class ObjectEncoder(object):
    def decodificarDiccionario(self,d):
        if '__class__'not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Lista':
                personales=d['personales']
                dPersonal=personales[0]
                lista=class_()
                for i in range(len(personales)):
                    dPersonal=personales[i]
                    class_name=dPersonal.pop('__class__')
                    class_=eval(class_name)
                    atributos=dPersonal['__atributos__']
                    unPersonal=class_(**atributos)
                    lista.agregaPersonal(unPersonal)
            return lista
    
    def guardarJSONArchivo(self,diccionario,archivo):
        with Path(archivo).open('w',encoding='UTF-8') as destino:
            json.dump(diccionario,destino,indent=4)
            destino.close()

    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding='UTF-8') as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario