from conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, id_conta: int, saldo: float, taxa_rendimento: float):
        super().__init__(id_conta, saldo)
        self.__taxa_rendimento = taxa_rendimento

    @property
    def taxa_rendimento(self):
        return self.__taxa_rendimento

    @taxa_rendimento.setter
    def taxa_rendimento(self, valor: float):
        if valor < 0:
            raise ValueError("A taxa de rendimento não pode ser negativa.")
        self.__taxa_rendimento = valor

    def sacar(self, valor: float):
        try:
            if valor <= 0:
                raise ValueError("O valor a ser sacado deve ser positivo.")
            if self.saldo < valor:
                raise ValueError("Saldo insuficiente para saque.")
            self.saldo -= valor
        except ValueError as erro:
            print(f"Erro ao sacar valor: {erro}")

    def verificar_rendimento_ao_ano(self, tempo: float):
        try:
            if tempo < 0:
                raise ValueError("O tempo não pode ser negativo.")
            return self.saldo * ((1 + self.taxa_rendimento) ** tempo - 1)
        except ValueError as erro:
            print(f"Erro ao verificar rendimento: {erro}")