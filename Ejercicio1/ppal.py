# implemente el TAD Tabla Hash teniendo en cuenta la política de manejo de colisiones
# direccionamiento abierto, utilizando como función de transformación de claves el método
# de la división, procesando las claves sinónimas a través de la secuencia de Prueba Lineal
# y considerando trabajar con 1000 claves numéricas que serán generadas aleatoriamente a
# través de la función rand.
# Se pide calcular la Longitud de la Secuencia de Prueba al Buscar una clave teniendo en
# cuenta:
# 1. El tamaño de la tabla Hash no es un número primo.
# 2. El tamaño de la tabla Hash sí es un número primo.
# Realice un breve análisis comparativo basado en las dos consideraciones anteriores
from nodo import Nodo
import numpy as np
class Hash:
    __tabla=[]
    __dimension=0
    def __init__(self,dimension=5):
        self.__dimension=dimension
        self.__tabla=np.full(dimension,Nodo)
    def Insertar(self,elemento):
        # if isinstance(elemento,str):
        #     pass
        # else:
        aux=elemento%self.__dimension #METODO DE DIVISION
        if self.__tabla[aux]==None:
            self.__tabla[aux].SetElemento(elemento)
        else:
            aux1=self.__tabla[aux]
            while(aux1.GetSiguiente()!=None):
                aux1=aux1.GetSiguiente()
            aux1.SetSiguiente(elemento)

    def Borrar(self):
        pass
    def Buscar(self,elemento):
        aux=elemento%self.__dimension
        if self.__tabla[aux].getElemento()==elemento:
            pass
    def Mostrar(self):
        for i in range(0,self.__dimension):
            print(i,self.__tabla[i].getElemento())
if __name__ == '__main__':
    tabla=Hash()
    tabla.Insertar(4315)
    tabla.Mostrar()
