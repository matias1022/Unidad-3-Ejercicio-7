from ClasePersonal import Personal

class Investigador(Personal):
    __investigacion=None
    __tipoI=None
 

    def __init__(self, cuil, apellido, nombre, sueldoB, antiguedad,investigacion,tipoI,carrera='',cargo='',catedra=''):
        super().__init__(cuil, apellido, nombre, sueldoB, antiguedad,investigacion,tipoI,carrera,cargo,catedra)
        self.__investigacion=investigacion
        self.__tipoI=tipoI


    def geTarea(self):
        return self.__investigacion

    def getTipo(self):
        return self.__tipoI
    def calculaSueldo(self):
        sueldo=0.0
        sueldo+=self.getSueldo()+self.getAntiguedad()*self.getSueldo()/100
        return sueldo






    def __lt__(self,O):
        menor=False
        if self.getNombre()<O.getNombre():
            menor=True
        
        return menor




    def mostrar(self):
        cadena="\nCUIL: "+self.getCuil()+"\nNombre: "+self.getNombre()+"\nApellido: "+self.getApellido()+"Sueldo: "+str(self.getsueldo())
        cadena+="\nAntiguedad: "+str(self.getAntiguedad())+"\nArea Investigacion: "+self.__investigacion+"\nTipo investigacion: "+self.__tipoI
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
                            areainvestigacion=self.__investigacion,
                            tipoinvestigacion=self.__tipoI,
                           
                            )
            )
        return d