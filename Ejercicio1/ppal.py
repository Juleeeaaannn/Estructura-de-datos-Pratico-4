# implemente el TAD Tabla Hash teniendo en cuenta la política de manejo de colisiones
# direccionamiento abierto
# utilizando como función de transformación de claves el método
# de la división, procesando las claves sinónimas a través de la secuencia de Prueba Lineal
# y considerando trabajar con 1000 claves numéricas que serán generadas aleatoriamente a
# través de la función rand.
# Se pide calcular la Longitud de la Secuencia de Prueba al Buscar una clave teniendo en
# cuenta:
# 1. El tamaño de la tabla Hash no es un número primo.
# 2. El tamaño de la tabla Hash sí es un número primo.
# Realice un breve análisis comparativo basado en las dos consideraciones anteriores
from math import trunc
import random
import numpy as np
class Hash:
    __tabla=[]
    __dimension=0
    def __init__(self,claves):
        aux=trunc(claves/0.7)
        self.__dimension=self.primo(aux)
        print(self.__dimension)
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
        if self.__tabla[aux]==None:#pregunto si esta vacia la posicion que encontre
            self.__tabla[aux]=elemento
        else:
            aux1=aux+1
            while(self.__tabla[aux1]!=None and aux!=aux1):
                    aux1=(aux1+1)%self.__dimension #SECUENCIA DE PRUEBA LINEAL||| permite utilizar el while para que la proxima posicion en la que caiga este dentro del arreglo numpy
                                                 # si despues de realizados los ciclos vuelve a caer en la posicion aux1 es que no encontro lugar.
            if aux!=aux1 and self.__tabla[aux1]==None:
                self.__tabla[aux1]=elemento
            else:
                print("elemento no econtrada!")

    def Buscar(self,elemento):
        aux=elemento%self.__dimension
        if self.__tabla[aux]==elemento:
            retorna=self.__tabla[aux]
        else:
            aux1=aux+1
            while(self.__tabla[aux]!=None and aux!=aux1):
                    aux=(aux+1)%self.__dimension
            if aux!=aux1:
                retorna=self.__tabla[aux]
            else:
                retorna=None
                print("elemento no encontrado")
        return retorna

    def Mostrar(self):
        for i in range(self.__dimension):
            print(i, self.__tabla[i])

if __name__ == '__main__':
    tabla=Hash(10)
    tabla.Insertar(6)
    tabla.Insertar(57)
    tabla.Mostrar()
