
from ClaseDocente import Docente
from ClaseLista import Lista
from menu import Menu

def test():
    lista=Lista()
    unDocente=Docente('20-43641926-1','Gonzalez','Matias',720000.0,4,'LSI','Profesor','POO'','',')
    lista.agregaPersonal(unDocente)     


if __name__ == '__main__':
    test()

    menu=Menu()
    menu.Ejecutar()