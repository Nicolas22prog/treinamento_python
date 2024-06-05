texto = input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print()


#range(star, stop, (step))

for numero in range(0, 51, 5):
   print(numero, end=" ")    
