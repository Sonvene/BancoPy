from models.cliente import Cliente
from models.conta import Conta

felicity: Cliente = Cliente('felicity', 'felicity@gmail.com', '123.456.789-01', '02/08/1981')
angelina: Cliente = Cliente('Angelina', 'Angelina@gmail.com', '192.499.889-06', '21/12/1974')

# print(felicity)
# print(angelina)

conta1: Conta = Conta(felicity)
conta2: Conta = Conta(angelina)

print(conta1)
print(conta2)





