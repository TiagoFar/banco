from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Tiago', 35)
cliente2 = Cliente('Talita', 32)
cliente3 = Cliente('Sujinho', 9)

conta1 = ContaPoupanca(1111, 234567, 0)
conta2 = ContaCorrente(2222, 234568, 0)
conta3 = ContaPoupanca(3333, 234569, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente1)  # Nome e idade
banco.inserir_conta(conta1)  #  agencia, conta e saldo
banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado.')

    print('---------------------------------')

if banco.autenticar(cliente2):
    cliente2.conta.depositar(10)
    cliente2.conta.sacar(90)
else:
    print('Cliente não autenticado.')


