class Conta:
    
    def __init__(self,numero,titular,saldo,limite):
        print("Conta construida")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo de R${} do titular {}".format(self.saldo,self.titular))


    def depositar(self, valor):
        self.saldo += valor
        print("O valor depositado foi de R${}".format(valor))
        print("SALDO TOTAL DE R${} do titular {}".format(self.saldo,self.titular))

    def saca(self, valor):
        self.saldo -= valor
        print("O valor sacado foi de R${}".format(valor))
        print("SALDO TOTAL DE R${} do titular {}".format(self.saldo,self.titular))