saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    saldo -= saque
    print("realizando saque!")
else:
    print("Saldo insuficiente")     
