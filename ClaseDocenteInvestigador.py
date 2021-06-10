from ClaseDocente import Docente
from ClaseInvestigador import Investigador

class DocenteInvestigador(Docente, Investigador):
    __categ = ""
    __extra = 0

    def __init__(self,cuil,apellido,nombre,sueldoB,antiguedad,carrera,cargo,catedra,categ,extra,investigacion,tipoI):
        super().__init__(cuil,apellido,nombre,sueldoB,antiguedad,carrera,cargo,catedra,investigacion,tipoI)
        self.__categ = categ
        self.__extra = extra


    def getCategoria(self):
        return self.__categ

    def getExstra(self):
        return self.__extra


    def calcularSueldo(self):
        sueldo=Docente.calculaSueldo(self)+self.__extra
        return sueldo #11550 + 50 =11600

    def getSueldo(self):
        return super().getSueldo()

    def __str__(self):
        return f'''Cuil: {self.getCuil()}.
Apellido: {self.getApellido()}.
Nombre: {self.getNombre()}.
Sueldo Básico: ${self.getSueldo():.2f}.
Antiguedad: {self.getAntiguedad()}.
Carrera: {self.getCarrera()}.
Cargo: {self.getCargo()}.
Cátedra: {self.getCatedra()}.
Área de Investigación: {self.geTarea()}.
Tipo de Investigación: {self.getTipo()}.
Categoría: {self.__categ}.
Importe Extra: ${self.__extra:.2f}.
'''


    def toJSON(self):
        d=dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            cuil=self.getCuil(),
                            apellido=self.getApellido(),
                            nombre=self.getNombre(),
                            sueldoB=self.getSueldo(), 
                            antiguedad=self.getAntiguedad(),
                            carrera=self.getCarrera(),
                            cargo=self.getCargo(),
                            catedra=self.getCatedra(),
                            categ=self.__categ,
                            importeextra=self.__extra,
                            investigacion=self.geTarea(),
                            tipoI=self.getTipo()
                            )
            )
        return d
