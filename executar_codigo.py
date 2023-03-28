from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

# Criando uma conta corrente
Conta_Corrente = ContaCorrente(id_conta=5, saldo=10500, limite=5000)

# Realizando operações na conta corrente
Conta_Corrente.depositar(valor=12500)
Conta_Corrente.sacar(valor=5500)
print(f"Saldo da conta corrente: R$ {Conta_Corrente.saldo:.2f}")

# Criando uma conta poupança
Conta_Poupanca = ContaPoupanca(id_conta=9, saldo=13500, taxa_rendimento=0.08)

# Realizando operações na conta poupança
Conta_Poupanca.depositar(valor=6500)
Conta_Poupanca.sacar(valor=3500)
rendimento_1_ano = Conta_Poupanca.verificar_rendimento_ao_ano(tempo=1)
print(f"Saldo da conta poupança: R$ {Conta_Poupanca.saldo:.2f}")
print(f"Rendimento em 1 ano: R$ {rendimento_1_ano:.2f}")