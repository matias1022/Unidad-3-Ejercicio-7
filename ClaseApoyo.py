from ClasePersonal import Personal

class Apoyo(Personal):
    __categ=''


    def __init__(self, cuil, apellido, nombre, sueldoB, antiguedad,categ):
        super().__init__(cuil, apellido, nombre, sueldoB, antiguedad)
        self.__categ=categ


    def getCategoria(self):
        return self.__categoria


    def calcularSueldo(self):

        sueldo=self.getsueldo()
        if self.__categoria >=1 and self.__categoria <=10:
            sueldo+=(10/100)*sueldo

        elif self.__categoria>=21 and self.__categoria<=22:
            sueldo+=(20/100)*sueldo

        elif self.__categoria>=11 and self.__categoria<=20:
            sueldo+=(30/100)*sueldo


    def __lt__(self,O):
        menor=False
        if self.getnombre()<O.getnombre():
            menor=True
        
        return menor

    def mostrar(self):
        cadena="\nCUIL: "+self.getCuil()+"\nNombre: "+self.getNombre()+"\nApellido: "+self.getApellido()+"Sueldo: "+str(self.calcularSueldo())
        cadena+="\nAntiguedad: "+str(self.getAntiguedad())+"\nCategoria: "+self.__categ
        return cadena


    def toJSON(self):
        d=dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            cuil=self.getCuil(),
                            apellido=self.getApellido(),
                            nombre=self.getNombre(),
                            sueldobasico=self.getSueldo(), 
                            antiguedad=self.getAntiguedad(),
                            categoria=self.__categ,
                            )
            )
        return d