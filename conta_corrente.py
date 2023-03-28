from conta import Conta


class ContaCorrente(Conta):
    def __init__(self, id_conta: int, saldo: float, limite: float):
        super().__init__(id_conta, saldo)
        self.limite = limite

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor: float):
        try:
            if valor < 0:
                raise ValueError("O limite não pode ser negativo.")
            self.__limite = valor
        except ValueError as error:
            print(error)

    def sacar(self, valor: float):
        try:
            if valor <= 0:
                raise ValueError("O valor a ser sacado deve ser positivo.")
            if self.saldo + self.limite < valor:
                raise ValueError("Saldo insuficiente para saque.")
            self.saldo -= valor
        except ValueError as error:
            print(error)