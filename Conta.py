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