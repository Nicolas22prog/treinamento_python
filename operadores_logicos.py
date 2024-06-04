#operador "and" (todas devem retornar True para ser true)
saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque<=limite

#operador "or" (apenas uma deve retornar true para ser true, para ser false, todas devem ser false)
saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque<=limite

#operador de negação "not" (inverte o dado booleano)
not 1000 > 1500 #retorna true

contatos_emergencia = [] # lista vazia retorna false

not contatos_emergencia # retorna true
 #string preenchida retorna true
not "saque 1500" #retorna false
 #string vazia retoirna false
not "" #retorna true 

#parenteses
 
saldo = 1000
saque = 250
limite = 200
conta_especial = True
exp = saldo >= saque and saque<=limite or conta_especial and saldo >=saque #retorna true
print(exp)

exp_2 = (saldo >= saque and saque<=limite ) or (conta_especial and saldo >=saque) #retorna true
print(exp_2)
 
exp_3 = saldo>= saque and saque<=limite #retorna false
print(exp_3)
