saldo = 350
saque = float(input("valor do saque: "))

status = "sucesso" if saldo >= saque else "falha"
print(f"{status} ao realizar o saque")