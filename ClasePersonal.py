class Personal:
    __cuil=''
    __apellido=''
    __nombre=''
    __sueldoB=0
    __antiguedad=0.0


    def __init__(self,cuil,apellido,nombre,sueldoB,antiguedad,investigacion='',tipoI='',carrera='',cargo='',catedra=''):
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__sueldoB=sueldoB
        self.__antiguedad=antiguedad

    def getCuil(self):
        return self.__cuil
   
    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getSueldo(self):
        sueldo=self.__sueldoB+(self.__antiguedad/100)*self.__sueldoB
        return sueldo

    def getAntiguedad(self):
        return self.__antiguedad
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.__cuil,
                apellido=self.__apellido,
                nombre=self.__nombre,
                sueldoB=self.__sueldoB,
                antiguedad=self.__antiguedad
            )
        )
        return d
