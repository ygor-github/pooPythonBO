class Main:
    pass

print('Testing Project')

from Cliente import Cliente

from Conta import Conta

c1 = Cliente('Joao', '114444-2222')
conta = Conta(c1.nome,6565,0)

print(c1)
print(c1.nome,' e ',c1.telefone)

print(conta.titular,' Número: ',conta.numero,' Seu saldo: ',conta.saldo)