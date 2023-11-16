"""
** While / Else
** Contadores
** Acumuladores
"""
contador = 0
acumulador = 1

while contador <= 10 :
    print(contador)
    acumulador += contador
    if contador > 5: #  Quebrar antes não executa o else
        break

    print(acumulador)
    contador +=1
else:
    print("cabo")
print("esse executa")
