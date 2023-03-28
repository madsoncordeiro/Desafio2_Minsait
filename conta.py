class Conta:
    def __init__(self, id_conta: int, saldo: float):
        self.__id_conta = id_conta
        self.__saldo = saldo

    @property
    def id_conta(self):
        return self.__id_conta

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor: float):
        if valor < 0:
            raise ValueError("O valor de saldo não pode ser negativo.")
        self.__saldo = valor

    def depositar(self, valor: float):
        try:
            if valor <= 0:
                raise ValueError("O valor a ser depositado deve ser positivo.")
            self.__saldo += valor
        except ValueError as err:
            print(f"Erro ao depositar: {err}")

    def sacar(self, valor: float):
        try:
            if valor <= 0:
                raise ValueError("O valor a ser sacado deve ser positivo.")
            if self.__saldo < valor:
                raise ValueError("Saldo insuficiente para saque.")
            self.__saldo -= valor
        except ValueError as err:
            print(f"Erro ao sacar: {err}")