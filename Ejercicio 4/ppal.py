#       Implemente el TAD Tabla Hash teniendo en cuenta la política de manejo de colisiones usando Buckets,    utilizando como función de transformación de claves el método de extracción, y considerando trabajar con 1000 claves numéricas que serán generadas aleatoriamente a través de la función rand; teniendo en cuenta:

#       Se pide informar:

# 1.    La cantidad de Buckets desbordados; esto es, todas sus componentes ocupadas.

# 2.    La cantidad de Buckets subocupados; esto es, menos de la tercera parte ocupada.

#       Considerando:

# 1.    La cantidad de Buckets del Área Primaria no es un número primo.          

# 2.    La cantidad de Buckets del Área Primaria sí es un número primo.
import random
from math import trunc
import numpy as np
class Registro:
    __indice=0
    __dimension=4
    __registro=[]
    def __init__(self):
        self.__dimension=4
        self.__registro=np.full(self.__dimension,None)
        self.__indice=0
    def getIndice(self):
        return self.__indice
    def getRegistro(self):
        return self.__registro
    def addRegistro(self,elemento):
        self.__registro[self.__indice-1]=elemento
        self.__indice+=1
    def getElemento(self,i):
        return self.__registro[i]
    def lleno(self):
        return self.__indice<=4






class Hash:
    __tabla=[]
    __dimension=0
    __overflow=0
    def __init__(self,claves):
        aux=trunc(claves/4)
        self.__overflow=aux
        aux+=(30*aux/100)
        self.__dimension=self.primo(trunc(aux))
        regi=Registro()
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
        ele1=int(listaele[3]+listaele[4])
        aux=ele1%self.__dimension#METODO DE EXTRACCION
        if self.__tabla[aux].lleno():#pregunto si el registro esta lleno
            self.__tabla[aux].addRegistro(elemento)
        else:#si no esta lleno el registro
            band=True
            while(band and self.__overflow<self.__dimension):
                a=self.__tabla[self.__overflow].getIndice()
                if self.__tabla[self.__overflow].lleno():
                    self.__tabla[self.__overflow].addRegistro(elemento)
                    band=False
                else:
                    self.__overflow+=1
                



    def Buscar(self,elemento):
        listaele=str(elemento)
        ele1=int(listaele[3]+listaele[4])
        aux=ele1%self.__dimension
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
            for j in range(0,4):
                print(i,j,self.__tabla[i].getElemento(j),end="\t ")
                print("")



if __name__ == '__main__':
    tabla=Hash(20)
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