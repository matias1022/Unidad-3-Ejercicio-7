from ClasePersonal import Personal
from ClaseApoyo import Apoyo
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClaseDocenteInvestigador import DocenteInvestigador
from zope.interface import implementer
from ClaseInterfaz import interface
from ClaseNodo import Nodo

@implementer(interface)
class Lista:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0
    
    def __init__(self):
        self.__comienzo=None
        self.__actual=None

    def cargarPers(self):
        cuil=input("\nIngrese su CUIL: ")
        apellido=input("\nIngrese su apellido: ")
        nombre=input("\nIngrese su nombre: ")
        sueldoB=float(input("\nIngrese su sueldo: "))
        antiguedad=int(input("\nIngrese su antiguedad: "))

        tipo=input("\nIngrese su Tipo de cargo: (D= Docentes, I= investigadores, DI= docente investigador, A=personal de apoyo)").lower()

        if tipo == "d":
            carrera=input("\nIngrese la carrera: ")
            cargo=input("\nIngrese el cargo que ocupa: ")
            catedra=input("\nIngrese la catedra: ")
            P=Docente(cuil,apellido,nombre,sueldoB,antiguedad,carrera,cargo,catedra)
        
        elif tipo == "i":
            investigacion=input("\nIngrese el area de investigacion: ")
            tipoI=input("\nIngrese el tipo de investigacion: ")
            P=Investigador(cuil,apellido,nombre,sueldoB,antiguedad,investigacion,tipoI)

        elif tipo == "di":
            carrera=input("\nIngrese la carrera: ")
            cargo=input("\nIngrese el cargo que ocupa: ")
            catedra=input("\nIngrese la catedra: ")
            investigacion=input("\nIngrese el area de investigacion: ")
            tipoI=input("\nIngrese el tipo de investigacion: ")
            categ=input("\nIngrese la categoria: ")
            extra=int(input("\nIngrese el importe extra: "))
            P=DocenteInvestigador(cuil,apellido,nombre,sueldoB,antiguedad,carrera,cargo,catedra,categ,extra,investigacion,tipoI)

        elif tipo == "a":
            categ=input("\nIngrese la categoria: ")
            P=Apoyo(cuil,apellido,nombre,sueldoB,antiguedad,categ)

        return P
    def insertarPers(self,personal,pos):
        aux=self.__comienzo
        i=0
        nodo=Nodo(personal)
        while i < pos and aux != None:
            aux=aux.getSiguiente()
            i+=1

        if aux == None:
            print("\nERROR no se encuentra nada en dicha posicion")
            

        else:
            nodo.setSiguiente(aux.getSiguiente())
            aux.setSiguiente(nodo)
            self.__tope +=1
            print("\nPersonal insertado con exito!")

    def agregaPersonal(self,unPersonal):
        assert isinstance(unPersonal,Personal)

        nodo=Nodo(unPersonal)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1
    def mostrarSegunPosicion(self,posicion):
        assert isinstance(posicion,int)

        aux=self.__comienzo
        encontro=False
        i=0
        ant=aux

        if 0<posicion<=self.__tope:
            if i==posicion-1:
                if self.__comienzo==None:
                    print('No hay vehículos cargados.')
                else:
                    print(f'La clase que se encuentra en la posicion: {posicion} es: {aux.getTipo()}')
            else:
                ant=aux
                while aux!=None and encontro==False:
                    if i==posicion-1:
                        encontro=True
                    else:
                        i+=1
                        ant=aux
                        aux=aux.getSiguiente()

                if i==posicion-1:
                    print(f'La clase que se encuentra en la posicion: {posicion} es: {aux.getTipo()}')
        else:
            raise Exception('Posición ingresada es incorrecta.\n')
    def getListado(self):
        p=self.__comienzo  
        s = None  
        print(self.__comienzo  ) 
        while(p != None):  
            s = p.getSiguiente()
            while(s != None):
                if p.getDato().getApellido().lower() > s.getDato().getApellido().lower():
                    aux = p
                    p = s
                    s = aux
                s = s.getSiguiente()
            p = p.getSiguiente()

        for s in self:
            tipo=''
            if type(s) == Docente:
                tipo='Docente'
            elif type(s)==Apoyo:
                tipo='Personal de Apoyo'
            elif type(s)==Investigador:
                tipo='Investigador'
            else:
                tipo='Docente Investigador'

            print(f'\nNombre: {s.getNombre()}\nApellido: {s.getApellido()}\nTipo de agente: {tipo}\nSueldo: {s.calculaSueldo():.2f}')
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            personales=[personal.toJSON() for personal in self]
        )
        return d      
    def listadoCarrera(self,carrera):
        aux=self.__comienzo
        i=0
        listaAux=Lista()

        if self.__comienzo==None:
            print('No hay personal cargado.')
        else:
            while aux!=None and i<self.__tope:
                if aux.getDato().getCarrera().lower() == carrera and aux.getTipo()=='Docente Investigador':
                    listaAux.agregaPersonal(aux.getDato())
                aux=aux.getSiguiente()
                i+=1

        p = listaAux.getComienzo()
        s = None

        while(p != None):  
            s = p.getSiguiente()
            while(s != None):
                if p.getDato().getNombre().lower() > s.getDato().getNombre().lower():
                    aux = p
                    p = s
                    s = aux
                s = s.getSiguiente()
            p = p.getSiguiente()

        for s in listaAux:
            if type(s)==DocenteInvestigador:
                if s.getCarrera().lower()==carrera:
                    print (s)

    def getComienzo(self):
        return self.__comienzo
    def porArea(self,area):
        aux = self.__comienzo
        i = 0
        contInves = 0
        contInvesDoc = 0
        if self.__comienzo == None:
            print('Vacio')
        else:
            while aux!=None and i<self.__tope:
                if aux.getTipo() == 'Docente Investigador' or aux.getTipo()=='Investigador':
                    if aux.getDato().geTarea().lower() == area:
                        if aux.getTipo() == 'Docente Investigador':
                            contInvesDoc += 1
                        elif aux.getTipo() == 'Investigador':
                            contInves += 1
                aux = aux.getSiguiente()
                i+=1
            if contInves!=0:
                print(f'Cantidad de Investigadores: {contInves}.') 
            else:
                print('No hay investigadores en dicha área.')
            if contInvesDoc!=0:
                print(f'Cantidad de Docentes Investigadores: {contInvesDoc}.')
            else:
                print('No hay docentes investigadores en dicha área.')
    def porCategoria(self,categ):
        aux = self.__comienzo
        i = 0
        total = 0
        if self.__comienzo == None:
            print('Vacio')
        else:
            while aux!=None and i<self.__tope:
                if aux.getTipo() == 'Docente Investigador':
                    if aux.getDato().getCategoria().lower() == categ:
                        print(f'Apellido: {aux.getDato().getApellido()}\nNombre: {aux.getDato().getNombre()}\nImporte Extra: {aux.getDato().getExstra()}')
                        total+=aux.getDato().getExstra()
                aux = aux.getSiguiente()
                i+=1 
            if total!=0:
                print(f'Total de dinero que debe solicitar la secretaria de investigacion: {total}')
            else:
                print('No hay docentes investigadores en dicha categoría.')

    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            if self.__actual==None:
                raise IndexError
            self.__indice+=1
            dato=self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
        