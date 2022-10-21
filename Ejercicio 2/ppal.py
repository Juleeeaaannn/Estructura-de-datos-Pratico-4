# Implemente el TAD Tabla Hash teniendo en cuenta la política de manejo de colisiones direccionamiento abierto, utilizando como función de transformación de claves el método de la división, procesando las claves sinónimas a través de la secuencia de Prueba Pseudo Random y considerando trabajar con 1000 claves numéricas que serán generadas pseudoaleatoriamente a través de la función rand.

# Se pide calcular la Longitud de la Secuencia de Prueba al Buscar una clave teniendo en cuenta:

# 1.    El tamaño de la tabla Hash no es un número primo.

# 2.    El tamaño de la tabla Hash sí es un número primo.
from math import trunc
import random
import numpy as np
class Hash:
    __tabla=[]
    __dimension=0
    __random=0
    def __init__(self,claves):
        aux=trunc(claves/0.7)
        self.__random=random.randint(0,2)
        print(self.__random)
        self.__dimension=self.primo(aux)
        self.__tabla=np.full(int(self.__dimension),None)

    def es_primo(self,num):
        for n in range(2, num):
            if num % n == 0:
                return False
        return True

    def primo(self,num):
        band=True

        while band:
            if( self.es_primo(num) ):
                band=False
            else:
                num+=1
        return num


    def Insertar(self,elemento):
        aux=elemento%self.__dimension #METODO DE DIVISION
        if self.__tabla[aux]==None:#pregunto si la cabeza de la lista esta vacia
            self.__tabla[aux]=elemento
        else:
            
            aux1=aux
            while self.__tabla[aux]!=None and aux<self.__dimension:#PREGUNTO SI LA POSICION ES MENOR AL MAXIMO
                aux=aux+self.__random
            if self.__tabla[aux]!=None and aux<self.__dimension:
                self.__tabla[aux]=elemento
                print("insertado")
            else:#SI NO SE ENCONTRO POSICION MENOR AL MAXIMO SE VUELVE AL PRINCIPIO DE LA TABLA
                aux=0
                while self.__tabla[aux]!=None and aux<aux1:
                    aux=aux+self.__random
                if self.__tabla[aux]!=None and aux<aux1:
                    self.__tabla[aux]=elemento
                    print("insertado")
                else:
                    print("posicion no encontrada para insertar!")


    def Buscar(self,elemento):
        aux=elemento%self.__dimension
        if self.__tabla[aux]==elemento:
            retorna=self.__tabla[aux]
        else:
            aux1=aux
            while self.__tabla[aux]!=None and aux<self.__dimension:#PREGUNTO SI LA POSICION ES MENOR AL MAXIMO
                aux=aux+self.__random
            if self.__tabla[aux]!=None and aux<self.__dimension:
                retorna=self.__tabla[aux]
            else:#SI NO SE ENCONTRO POSICION MENOR AL MAXIMO SE VUELVE AL PRINCIPIO DE LA TABLA
                aux=0
                while self.__tabla[aux]!=None and aux<aux1:
                    aux=aux+self.__random
                if self.__tabla[aux]!=None and aux<aux1:
                    retorna=self.__tabla[aux]
                else:
                    print("elemento no encontrado!")
        return retorna

    def Mostrar(self):
        for i in range(self.__dimension):
            print(i, self.__tabla[i])

if __name__ == '__main__':
    tabla=Hash(10)
    for i in range(10):
        aux=random.randrange(10)
        print(f"numero={aux}")
        tabla.Insertar(aux)
    tabla.Mostrar()