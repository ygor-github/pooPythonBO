class Conta:
    def __init__(self,titular, numero, saldo):
        self._titular=titular
        self._numero=numero
        self._saldo=0

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if(saldo < 0):
            print('O saldo nao pode ser negativo')
        else:
            self._saldo = saldo

    def saque(self, valor):
        if (self.saldo>=valor):
            self.saldo-=valor
            print('Saque realizado com sucesso')
        else:
            print('Saldo insuficiente')


    def desposita(self, valor):
        self.saldo+=valor

    def extrato(self):
        print('Cliente: ',self._titular, ' Saldo Atual: ',self._saldo)