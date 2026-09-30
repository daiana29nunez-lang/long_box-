from datetime import date
class comic:
    def __init__(self ,titulo, numero_edicion , editorial, universo, anio, paginas):
        self.__titulo = titulo
        self.__numero_edicion = numero_edicion
        self.__editorial = editorial
        self.__universo = universo
        self.__anio = anio
        self.__paginas = paginas


        self.__leido = False
        self.__puntaje = None
        self.__fecha_lectura = None

        if anio < 0:
            raise ValueError("el año no puede ser negativo")
        if paginas < 0:
            raise ValueError("la cantidad de paginas no puede ser negativo")

        #-------getters------

    def get_titulo(self):
            return self.__titulo

    def get_numero_edicion(self):
            return self.__numero_edicion

    def get_editorial(self):
            return self.__editorial

    def get_universo(self):
            return self.__universo

    def get_anio(self):
            return self.__anio

    def get_paginas(self):
            return self.__paginas

    def get_leido(self):
            return self.__leido

    def get_puntaje(self):
            return self.__puntaje

    def get_fecha_lectura(self):
            return self.__fecha_lectura


        #---------metodos---------

    def marcar_como_leido(self,puntaje):
            if puntaje < 1 or puntaje > 5 :
                raise ValueError("el puntaje debe estar entre el 1 y 5")
            
            self.__leido = True
            self.__puntaje = puntaje
            self.__fecha_lectura = date.today()


    def marcar_como_no_leido(self):
            self.__leido = False
            self.__puntaje = None
            self.__fecha_lectura = None  

    def mostrar_informacion(self):
            print("titulo:",self.__titulo)
            print("numero de edicion:",self.__numero_edicion)
            print("editorial:",self.__editorial)
            print("universo:",self.__universo)
            print("año:",self.__anio)
            print("paginas:",self.__paginas)
            print("leido:",self.__leido)
            print("puntaje:",self.__puntaje)
            print("fecha de lectura:",self.__fecha_lectura)

    
        