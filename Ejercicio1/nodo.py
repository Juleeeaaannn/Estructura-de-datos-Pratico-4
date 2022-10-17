class Nodo:
    __elemento=None
    __sig=None
    def __init__(self,elemento=None):
        self.__elemento=elemento
        self.__sig=None
    def getElemento(self):
        return self.__elemento
    def getSiguiente(self):
        return self.__sig
    def setElemento(self,elemento):
        self.__elemento=elemento
    def setSiguiente(self,elemento):
        self.__sig=elemento