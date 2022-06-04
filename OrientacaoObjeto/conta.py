class Conta:
    
    def __init__(self,numero,titular,saldo,limite):
        print("Conta construida")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de R${} do titular {}".format(self.__saldo,self.__titular))


    def deposita(self, valor):
        self.__saldo += valor
        print("O valor depositado foi de R${}".format(valor))
        print("SALDO TOTAL DE R${} do titular {}".format(self.__saldo,self.__titular))

    def saca(self, valor):
        self.__saldo -= valor
        print("O valor sacado foi de R${}".format(valor))
        print("SALDO TOTAL DE R${} do titular {}".format(self.__saldo,self.__titular))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def numero_da_conta(self):
        return self.__numero
    
    def retorna_limite(self):
        return self.__limite