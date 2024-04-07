# Sistema de Caixa Eletrônico Geek-Bank

Bem-vindo ao sistema de caixa eletrônico Geek-Bank! Este programa permite que você gerencie contas bancárias e realize transações como saques, depósitos e transferências.

## Funcionalidades

1. **Criar Conta**
   - Crie uma nova conta bancária para um cliente com suas informações pessoais.

2. **Sacar Fundos**
   - Realize saques de uma conta bancária específica.

3. **Depositar Fundos**
   - Deposite dinheiro em uma conta bancária específica.

4. **Transferir Fundos**
   - Transfira dinheiro entre duas contas bancárias.

5. **Listar Contas**
   - Visualize uma lista de todas as contas bancárias existentes.

6. **Sair do Sistema**
   - Encerre o sistema de caixa eletrônico.

## Instruções

1. **Executando o Programa**
   - Certifique-se de ter o Python instalado em seu computador.
   - Execute o programa `atm_system.py`.

2. **Opções do Menu**
   - `1`: Criar uma nova conta
   - `2`: Sacar fundos
   - `3`: Depositar fundos
   - `4`: Transferir fundos
   - `5`: Listar todas as contas
   - `6`: Sair do sistema

3. **Criando uma Conta**
   - Insira os detalhes do cliente, como nome, e-mail, CPF e data de nascimento.
   - Uma nova conta bancária será criada e adicionada ao sistema.

4. **Realizando Transações**
   - Para saques e depósitos, forneça o número da conta e o valor desejado.
   - Para transferências, especifique o número da conta de origem, o número da conta de destino e o valor a ser transferido.

5. **Listando Contas**
   - Visualize um resumo de todas as contas bancárias existentes, incluindo detalhes do cliente e saldo da conta.

## Requisitos

- Python

## Estrutura do Código

- `atm_system.py`: Contém a lógica principal do sistema de caixa eletrônico.
- `models/cliente.py`: Define a classe `Cliente` para informações do cliente.
- `models/conta.py`: Define a classe `Conta` para contas bancárias.
- `utils/`: Diretório contendo funções utilitárias e métodos auxiliares.

## Executando o Programa

```bash
python atm_system.py
