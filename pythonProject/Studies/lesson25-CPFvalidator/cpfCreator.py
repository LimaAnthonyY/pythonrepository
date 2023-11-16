from random import randint

cpf = str(randint(100000000,999999999))

somador = 0
sum = 0
lista=[]
for p, r in enumerate(range(10,1,-1)):
    lista.append (cpf[p])
    sum = int(cpf[p]) * r
    somador += sum
aux = 11 - (somador % 11)
if aux > 9:
    lista.append('0')
else :
    lista.append(str(aux))

sum = 0
somador = 0
cpf += str(lista [-1])
for p, r in enumerate(range(11,1,-1)):
    sum = int(cpf[p]) * r
    somador += sum
aux = 11 - (somador % 11)
if aux > 9:
    lista.append(0)
else :
    lista.append(str(aux))
cpf += str(lista [-1])

print(cpf)
print(lista)
aux = list(map(int, lista))
print('\33[32mO CPF é: {}{}{}.{}{}{}.{}{}{}-{}{}'.format(aux[0],aux[1],aux[2],aux[3],aux[4],aux[5],aux[6],aux[7],aux[8],aux[9],aux[10]))



