from ClaseLista import Lista
from ClaseObjectEncoder import ObjectEncoder
import os


class Menu:
      __op = 0
      def __init__(self,opcion=0):
        self.__op = opcion
      def Ejecutar(self):
          os.system('cls')
          salir = False
          lista=Lista()
          jsonF=ObjectEncoder()   
          d=lista.toJSON()
        #  jsonF.guardarJSONArchivo(d,'personal.json')
          diccionario=jsonF.leerJSONArchivo('personal.json') #se lee el archivo JSON
          lista=jsonF.decodificarDiccionario(diccionario)
          
          while salir == False:
              print('1-\tInsertar a agentes a la colección.')
              print('2-\tAgregar agentes a la colección.')
              print('3-\tDada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.')
              print('4-\tIngresar por teclado una carrear y listar todos los nombres de los docentes investigadores')
              print('5-\tDada un area de investigacion, contar docente investigador y cantidad de investigadores que trabajan')
              print('6-\tGenerar listado de todos los agentes')
              print('7-\tListar docentes investigadores de una categoria')
              print('8-\tAlmacenar datos en archivo Json')
              print('0-\tSalir')
              self.__op = int(input('Ingrese la opcion: '))
              if self.__op == 1: 
                  posicion=int(input("Ingresar posicion"))
                  unPersonal=lista.cargarPers()
                  lista.insertarPers(unPersonal,posicion-1)
              elif self.__op == 2: 
                  unPersonal=lista.cargarPers()
                  lista.agregaPersonal(unPersonal)
                  
              elif self.__op == 3 : 
                   posicion=int(input("\nIngrese la posicion: "))
                   lista.mostrarSegunPosicion(posicion)
              elif self.__op == 4: 
                    carrera=input('Ingrese la carrera: ')
                    carrera=carrera.lower()
                    lista.listadoCarrera(carrera)
              elif self.__op == 5: 
                    areaI=input('Ingrese un área de ingestigación: ')
                    areaI=areaI.lower()
                    lista.porArea(areaI)
              elif self.__op == 6: 
                   print('Mostrar agentes ordenados.')
                   lista.getListado()
              elif self.__op == 7: 
                   categoria=input("\nIngrese una categoria: (I, II, III, IV o V)")
                   categoria=categoria.lower()
                   lista.porCategoria(categoria)

              elif self.__op == 8: 
                    print('             Almacenar personal en archivo JSon.')
                    jsonF=ObjectEncoder()        #genera el Archivo JSON
                    d=lista.toJSON()
                    jsonF.guardarJSONArchivo(d,'personal.json')
                    print('El Almacenamiento fue un exito en el archivo"personal.json".')
      
 
              elif self.__op == 0: #Salir
                  salir = True
              else:
                 print('Opcion ingresada incorrecta')
                 input('Presiona ENTER para continuar...')


          print('Cerrando Menú..')   