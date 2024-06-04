import sys
conta_normal = True
conta_universitaria = False
saldo = 600
saque =float(input("valor do saque: "))
cheque_especial = 10%saldo
if conta_normal:
    if saldo >= saque:
        print("saque realizado com sucesso:")
    elif saque <= (saldo + cheque_especial):  
        print("saque realizado com uso do cheque especial!")
    else:
        print("Saldo insuficiente!")
        sys.exit        
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
        sys.exit              
else: 
    print("O sistema nao reconheceu o seu tipo de conta, entre em contato com o seu gerente")
    sys.exit