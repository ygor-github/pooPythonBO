class Main:
    pass

print('Testing Project')

from Cliente import Cliente

from Conta import Conta

c1 = Cliente('Joao', '114444-2222')
conta = Conta(c1.get_nome(),6565,200)

#print(c1)
#print(c1.get_nome(),' e ',c1._telefone)

#print(conta._titular,' Número: ',conta._numero,' Seu saldo: ',conta._saldo)

conta.desposita(100)
conta.extrato()
conta.saque(150)
conta.extrato()