from main.Banco import *
import os
if __name__ == "__main__":
    lista_carteiras = []
    def menu():
        os.system('cls')
        print('1 - Cadastrar uma nova carteira')
        print('2 - Listar as contas de uma carteira existente')
        print('3 - Sair do programa')
        seletor(int(input('Informe a opção desejada: ')))
    def cadastro_carteira():
        os.system('cls')
        lista_carteiras.append(carteira(input('Informe o tipo de investimento: ')))
        cadastro_conta(int(input('Deseja cadastrar uma conta?\n1 - Sim\n2 - Não\n = ')),lista_carteiras[-1])
    def cadastro_conta(option, carteira):
        os.system('cls')
        if option == 1 and len(carteira.lista_contas) < 3:
            option = input('Qual o tipo da conta?\nN - Normal\nC - Corrente\nP - Poupança\n = ')
            if option == 'N' or option == 'n':
                carteira.add_conta(conta(int(input('Informe um número para conta: ')),input('Informe um titular para a conta: '),float(input('Informe o valor de saldo inicial: '))))
            elif option == 'C' or option == 'c':
                carteira.add_conta(conta_corrente(int(input('Informe um número para conta: ')),input('Informe um titular para a conta: '),float(input('Informe o valor de saldo inicial: '))))
            elif option == 'P' or option == 'p':
                carteira.add_conta(conta_poupanca(int(input('Informe um número para conta: ')),input('Informe um titular para a conta: '),float(input('Informe o valor de saldo inicial: ')),float(input('Informe o rendimento mensal: '))))
            cadastro_conta(int(input('Deseja cadastrar outra conta?\n1 - Sim\n2 - Não\n = ')), carteira)
        elif option == 1 and len(carteira.lista_contas) == 3:
            print('A carteira já possui 3 contas, o limite máximo atual')
            print('Pressione "Enter" para retornar ao menu: ')
            input()
            menu()
        elif option == 2:
            menu()
    def listar_carteiras():
        qual_carteira = ''
        for carteira in lista_carteiras:
            print(f'Investimento: {carteira.investimento}')
        option = input('Informe o investimento, do qual você deseja listar as contas: ')
        verifica = False
        for carteira in lista_carteiras:
            if option == carteira.investimento:
                verifica = True
                qual_carteira = carteira
                break
        if verifica == False:
            print('Carteira não encontrada, informe um envestimento válido')
            print('Pressione "Enter" para retornar a lista de carteiras: ')
            input()
            listar_carteiras()
        elif verifica == True and len(qual_carteira.lista_contas) == 0 :
            print('A carteira selecionada não possui contas cadastradas')
            print('Pressione "Enter" para retornar a lista de carteiras: ')
            input()
            listar_carteiras()
        else:
            for conta in qual_carteira.lista_contas:
                print(conta.retorna_dados())
        option = input('Deseja retornar ao menu ou encerrar o programa ?\n1 - Sim\n2 - Não\n = ')
        if option == 1:
            menu()
        else: 
            exit()
    def seletor(option):
        if option == 1:
            cadastro_carteira()
        elif option == 2:
            listar_carteiras()
    menu()
















    '''
    lista_carteiras.append(carteira('a'))
    lista_carteiras[0].add_conta(conta(1001, "batata", 100.00))
    lista_carteiras[0].add_conta(conta_corrente(1002, "banana", 100.00))
    lista_carteiras[0].add_conta(conta_poupanca(1003, "beterraba", 100.00))
    lista_carteiras.append(carteira('b'))
    lista_carteiras[1].add_conta(conta(1004, "mandioca", 100.00))
    lista_carteiras[1].add_conta(conta_corrente(1005, "cara", 100.00))
    lista_carteiras.append(carteira('c'))
    lista_carteiras[2].add_conta(conta_poupanca(1007, "inhame", 100.00))
    lista_carteiras.append(carteira('d'))
    '''



'''
    def a(carteira):
        for contas in carteira.lista_contas:
            print(contas.retorna_dados())
            print('\n')
        titular = input('Informe qual o titular da conta: ')
        for conta in carteira.lista_contas:
            if titular == conta.titular:
                c(conta)
    def b():        
        for carteiras in lista_carteiras:
            print(carteiras.investimento)
        investimento = input('Informe o investimento da carteira: ')
        for carteira in lista_carteiras:
            if carteira.investimento == investimento:
                a(carteira)
    def c(conta):
        print('1 - sacar')
        print('2 - depositar')
        print('3 - informar o saldo')
        print('4 - informar o saldo total')
        print('5 - informar o limite')
        print('6 - sair')
        d(int(input('Selecione uma opção: ')),conta)
    def d(opt, conta):
        if opt == 1:
            conta.sacar(float(input('Valor para saque: ')))
            c(conta)
        elif opt == 2:
            conta.depositar(float(input('Valor para depósito: ')))
            c(conta)
        elif opt == 3:
            print(f'Saldo: {conta.saldo}')
            c(conta)
        elif opt == 4:
            print(f'Saldo Total: {conta.saldo_total()}')
            c(conta)
        elif opt == 5:
            print(f'Limite: {conta.limite}')
            c(conta)
        elif opt == 6:
            exit()
    b() 
'''