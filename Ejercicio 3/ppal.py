# Implemente el TAD Tabla Hash teniendo en cuenta la política de manejo de colisiones encadenamiento, utilizando como función de transformación de claves el método de plegado, y considerando trabajar con 1000 claves numéricas que serán generadas aleatoriamente a través de la función rand.

# Se pide informar:

# 1.    La longitud de cada una de las listas de claves sinónimas.

# 2.    La cantidad de esas listas que registran una longitud que varía en hasta 3 unidades, por exceso o por defecto, respecto al promedio de las longitudes de dichas listas.

# Considerando:

# 1.    La cantidad de listas de claves sinónimas no es un número primo.

# 2.    La cantidad de listas de claves sinónimas sí es un número primo.
import random
from math import trunc
from Nodo import Nodo
import numpy as np
class Hash:
    __tabla=[]
    __dimension=0
    def __init__(self,claves):
        aux=trunc(claves/4)
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
        listaele=str(elemento)
        ele1=int(listaele[0]+listaele[1])
        ele2=int(listaele[2]+listaele[3])
        ele3=int(listaele[4])
        aux=(ele1+ele2+ele3)%self.__dimension#METODO DE PLEGADO
        if self.__tabla[aux]==None:#pregunto si la cabeza de la lista esta vacia
            self.__tabla[aux]=Nodo(elemento)
            self.__tabla[aux].setElemento(elemento)
        else:#si la cabeza no esta vacia entra por aca
            aux1=self.__tabla[aux]
            while(aux1.getSiguiente()!=None):
                aux1=aux1.getSiguiente()
            aux1.setSiguiente(Nodo(elemento))



    def Buscar(self,elemento):
        aux=elemento%self.__dimension
        if self.__tabla[aux].getElemento()==elemento:
            retorna=self.__tabla[aux]
        else:
            aux1=self.__tabla[aux]
            while(aux1.getSiguiente()!=None):
                aux1=aux1.getSiguiente()
            retorna=aux.getSiguiente()
        return retorna


    def Mostrar(self):
        for i in range(self.__dimension):
            print(i, self.__tabla[i].getElemento(), end="\t")
            aux=self.__tabla[i].getSiguiente()
            while(aux!=None):
                print(aux.getElemento(),end="\t ")
                aux=aux.getSiguiente()
            print("")

if __name__ == '__main__':
    tabla=Hash(10)
    tabla.Insertar(20811)
    tabla.Insertar(21115)
    tabla.Insertar(20619)
    tabla.Insertar(20318)
    tabla.Insertar(20017)
    tabla.Insertar(20916)
    tabla.Insertar(20815)
    tabla.Insertar(20614)
    tabla.Insertar(20213)
    tabla.Insertar(20412)
    tabla.Mostrar()