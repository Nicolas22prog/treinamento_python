def sacar( valor : float) -> None : #inicio do bloco de metodo
    saldo = 1000

    if saldo >= valor :            #inicio do bloco if
    
        saldo -= valor
        print("valor sacado")

    
    #fim do bloco if

#fim do bloco de metodo

def depositar(valor):
    saldo = 1000
    saldo += valor


sacar(500)
depositar(50)