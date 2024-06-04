#operadore de identidade é "is"
 
curso = "Curso de python"
nome_curso = curso
saldo = 200
limite = 200

exp_1 = curso is nome_curso #retorna true

exp_2 = curso is not nome_curso #retorna false

exp_3 = saldo is limite #retorna true

print(exp_1)
print(exp_2)
print(exp_3)
