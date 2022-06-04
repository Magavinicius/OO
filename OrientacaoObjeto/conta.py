class Conta:
    
    def __init__(self,numero,titular,saldo,limite):
        print("Conta construida")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def titular(self):
        return self.__titular.title()

    def extrato(self):
        print("Saldo de R${} do titular {}".format(self.__saldo,self.__titular))

    def deposita(self, valor):
        self.__saldo += valor
        print("O valor depositado foi de R${}".format(valor))
        print("SALDO TOTAL DE R${} do titular {}".format(self.__saldo,self.__titular))

    def pode_sacar(self,valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def saca(self, valor):
        if(self.pode_sacar(valor)):
            self.__saldo -= valor
            print("O valor sacado foi de R${}".format(valor))
            print("SALDO TOTAL DE R${} do titular {}".format(self.__saldo,self.__titular))
        else:
            print("O valor {} ultrapassou o limite de {}".format(self.__saldo,self.__limite))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_conta(self):
        return self.__numero
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        print("Limite alterado")

    def info_conta(self,):
        print("Conta  :   {}".format(self.__numero))
        print("Titular:   {}".format(self.__titular))
        print("Saldo  : R${}".format(self.__saldo))
        print("Limite : R${}".format(self.__limite))