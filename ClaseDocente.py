from ClasePersonal import Personal

class Docente(Personal):
    __carrera=''
    __cargo=''
    __catedra=''

    def __init__(self, cuil, apellido, nombre, sueldoB, antiguedad,carrera,cargo,catedra,investigacion='',tipoI=''):
        super().__init__(cuil, apellido, nombre, sueldoB, antiguedad,investigacion,tipoI,carrera,cargo,catedra)
        self.__carrera=carrera
        self.__cargo=cargo
        self.__catedra=catedra


    def getCarrera(self):
        return self.__carrera

    def getCargo(self):
        return self.__cargo

    def getCatedra(self):
        return self.__catedra

    def calculaSueldo(self):
        sueldo=int(self.getSueldo())
        if self.__cargo=='simple':
            sueldo+=(10/100)*sueldo

        elif self.__cargo =="semiexclusivo":
            sueldo+=(20/100)*sueldo

        elif self.__cargo =="exclusivo":
            sueldo+=(50/100)*sueldo

        return sueldo


    def __lt__(self,O):
        menor=False
        if self.getnombre()<O.getnombre():
            menor=True
        
        return menor








    def toJSON(self):
        d=dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            cuil=self.getCuil(),
                            apellido=self.getApellido(),
                            nombre=self.getNombre(),
                            sueldobasico=self.getSueldo(), 
                            antiguedad=self.getAntiguedad(),
                            carrera=self.__carrera,
                            cargo=self.__cargo,
                            catedra=self.__catedra,
                            
                            )
            )
        return d
    def mostrar(self):
        cadena="\nCUIL: "+self.getCuil()+"\nNombre: "+self.getNombre()+"\nApellido: "+self.getApellido()+"Sueldo: "+str(self.calculaSueldo())
        cadena+="\nAntiguedad: "+str(self.getAntiguedad())+"\nCarrera: "+self.__carrera+"\nCargo: "+self.__cargo+"\nCatedra: "+self.__catedra
        return cadena