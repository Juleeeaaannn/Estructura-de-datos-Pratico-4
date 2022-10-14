class Nodo:
    __elemento=None
    __sig=None
    def __init__(self,elemento=None):
        self.__elemento=elemento
        self.__sig=None
    def GetElemento(self):
        return self.__elemento
    def GetSiguiente(self):
        return self.__sig
    def SetElemento(self,elemento):
        self.__elemento=elemento
    def SetSiguiente(self,elemento):
        self.__sig=elemento