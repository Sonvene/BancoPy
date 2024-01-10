from typing import List
from time import sleep
from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('===============================================')
    print('===================== ATM =====================')
    print('================== Geek-Bank ==================')
    print('===============================================')

    print('\nSelecione uma Opção no menu.\n')
    print('1 - Criar conta.')
    print('2 - Efetuar saque.')
    print('3 - Efetuar deposito.')
    print('4 - Efetuar transferência.')
    print('5 - Listar contas.')
    print('6 - Sair do sistema.')

    opcao: int = int(input('Opção: '))

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre')
        sleep(2)
        exit(0)
    else:
        print('opção invalida')
        sleep(1)
        menu()


def criar_conta() -> None:
    print('Informe os dados do cliente')

    nome: str = input('Nome do cliente: ')
    email: str = input('Imail do cliente: ')
    cpf: str = input('CPF do cliente: ')
    data_nascimento: str = input('Data nascimento: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)
    contas.append(conta)

    print('Conta criado com suscesso.')
    print('Dados da conta:')
    print(f'---------------')
    print(conta)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))
            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta com o numero: {numero}')
    else:
        print('não existem contas para cadastrar')
    sleep(1)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informar o valor do depósito: '))
            conta.depositar(valor)
        else:
            print(f'Não foi encontrada a conta com o número: {numero}')
    else:
        print('Não existem contas cadastradas')
    sleep(1)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('Informa o número da sua conta: '))
        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input('informe o número da conta destino: '))
            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input('Informa o valor da transferência: '))
                conta_o.transferir(conta_d, valor)
            else:
                print(f'a conta destino com o número {numero_d} não foi encontrada.')
        else:
            print(f'A conta com número: {numero_o} não foi encontrada.')
    else:
        print('não existem constas cadastradas')
    sleep(1)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas\n')
        for conta in contas:
            print(conta)
            print('---------------')
            sleep(0.5)
        menu()
    else:
        print('não existem constas cadastradas')
    sleep(1)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None
    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c

if __name__ == "__main__":
    main()
