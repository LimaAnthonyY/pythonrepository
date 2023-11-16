"""
** Desempacotamento de listas
"""

lista = ['edu', 'joao',"luiz"]
n1, n2, *outraLista = lista #  Gerou 2 variaveis 1 para o indice 1 e outro para o indice 2
 #  o *outraLista gerou outra lista com o restante dos valores
# caso você não venha a utilizar o restante utilizar *_

print(n1, n2, outraLista)