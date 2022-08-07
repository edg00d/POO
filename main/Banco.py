class carteira:
    def __init__ (self, investimento):
        self.__investimento = investimento
        self.__lista_contas = []
    @property
    def investimento(self):
        return self.__investimento
    @investimento.setter
    def investimento(self, investimento):
        self.__investimento = investimento
    @property
    def lista_contas(self):
        return self.__lista_contas
    def add_conta(self, conta):
        if len(self.__lista_contas) < 3:
            self.__lista_contas.append(conta)
            print('Conta cadastrada')
        else:
            print('Máximo de contas já atingido (3)')
    def contas_negativas(self):
        contas_negativas = []
        for conta in self.__lista_contas:
            if conta.saldo < 0:
                contas_negativas.append(conta)
        return contas_negativas
class conta:
    def __init__(self, numero, titular, saldo):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    def sacar(self, valor):
        if valor > self.__saldo:
            print('Não há saldo o suficiente')
        else:
            self.__saldo -= valor
            print('Operação concluída')
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print('Operação concluída')
        else:
            print('Valor para saque inválido')
    def retorna_dados(self):
        return f'\nNumero: {self.numero}\nTitular: {self.titular}\nSaldo: {self.saldo}'
class conta_corrente(conta):
    def __init__(self, numero, titular, saldo):
        super().__init__(numero, titular, saldo)
        self.__limite = 2000
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    def saldo_total(self):
        return self.saldo + self.__limite
    def sacar(self, valor):
        if valor > self.saldo_total():
            print("Não há saldo, nem limite, o sufuciente")
        elif valor > self.saldo:
            valor -= self.saldo
            self.saldo = 0
            self.limite -= valor
            print('Operação concluída')
        else:
            self.saldo -= valor
            print('Operação concluída')
    def retorna_dados(self):
        return super().retorna_dados() + f'\nLimite: {self.__limite}'
class conta_poupanca(conta):
    def __init__(self, numero, titular, saldo, rendimento):
        super().__init__(numero, titular, saldo)
        self.__rendimento = rendimento
    @property
    def rendimento(self):
        return self.__rendimento
    @rendimento.setter
    def rendimento(self, rendimento):
        self.__rendimento = rendimento
    def acao_rendimento(self):
        self.saldo = self.saldo * self.__rendimento
    def retorna_dados(self):
        return super().retorna_dados() + f'\nRendimento: {self.__rendimento}'