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
import random
from nodo import Nodo
import numpy as np
class Hash:
    __tabla=[]
    __dimension=0
    def __init__(self,dimension=257):
        self.__dimension=dimension
        self.__tabla=np.full(dimension,None)
    # def Insertar(self,elemento):
    #     aux=elemento%self.__dimension #METODO DE DIVISION
    #     if self.__tabla[aux]==None:#pregunto si la cabeza de la lista esta vacia
    #         self.__tabla[aux]=Nodo(elemento)
    #         self.__tabla[aux].setElemento(elemento)
    #     else:#si la cabeza no esta vacia entra por aca
    #         aux1=self.__tabla[aux]
    #         while(aux1.getSiguiente()!=None):
    #             aux1=aux1.getSiguiente()
    #         aux1.setSiguiente(Nodo(elemento))
    def Insertar(self,elemento):
        aux=elemento%self.__dimension #METODO DE DIVISION
        if self.__tabla[aux]==None:#pregunto si la cabeza de la lista esta vacia
            self.__tabla[aux]=elemento
            
        else:
            while(self.__tabla[aux]!=None):
                if aux<self.__dimension and aux>0:
                    aux-=1
                else:
                    aux=self.__dimension-1
            if self.__tabla[aux]==None:
                self.__tabla[aux]=elemento
            else:
                print("posicion no econtrada, para insertar el elemento!")
            

    def Borrar(self):
        pass
    # def Buscar(self,elemento):
    #     aux=elemento%self.__dimension
    #     if self.__tabla[aux].getElemento()==elemento:
    #         retorna=self.__tabla[aux]
    #     else:
    #         aux1=self.__tabla[aux]
    #         while(aux1.getElemento()!=elemento):
    #             aux1=aux1.getSiguiente()
    #         if aux1.getElemento()==elemento:
    #             retorna=aux1
    #         else:
    #             retorna=None
    #             print("elemento no encontrado")
    #     return retorna

    def Buscar(self,elemento):
        aux=elemento%self.__dimension
        if self.__tabla[aux]==elemento:
            retorna=self.__tabla[aux]
        else:
            while(self.__tabla[aux]!=elemento):
                if aux<self.__dimension and aux>0:
                    aux-=1
                else:
                    aux=self.__dimension-1
            if self.__tabla[aux]==elemento:
                retorna=self.__tabla[aux]
                print("posicion",aux)
            else:
                retorna=None
                print("elemento no encontrado")
        return retorna

    def Mostrar(self):
        for i in range(self.__dimension):
            print(i, self.__tabla[i])
if __name__ == '__main__':
    tabla=Hash()
    for i in range(200):
        aux=random.randrange(1000)
        tabla.Insertar(aux)
    tabla.Mostrar()
