"""
** Enumerate - Enumerar elementos da lista # list
"""

lista = [
    #  0      1      2
    ['edu', 'joao',"luiz"], #  0
    #   0       1       2
    ['eddd', 'é',"luiza"], #  1
    #    0         1        2
    ['cuuu', 'joaona',"luizzzzz"] #  2
] #  cada virgula separa 1 valor da lista

enumerada = enumerate(lista)
print(enumerada)

print(lista[0][2])
print(lista[1][1])
print(lista[2][0])

for v1 in enumerate(lista, 99): #  mostra quando ele inicia, enumerar a partir do 99
    valorEnumerado, minhaLista = v1
    print(minhaLista)
