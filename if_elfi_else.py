import sys


opcao = int(input("Informe uma opção: [1] sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção invalida")