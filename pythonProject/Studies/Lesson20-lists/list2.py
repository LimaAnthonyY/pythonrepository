"""
Split, Join, Enumerate em python
** Split - Dividir uma str
** Join - Juntar uma lista
** Enumerate - Enumerar elementos Iteráveis
"""
# str = "O Brasil é o o o país do futebol, o Brasil é penta"
# lista = str.split(' ')
# lista2 = str.split(',')
# print(lista)
# print(lista2)
#
# palavra =''
# contagem = 0
# #
# # for valor in lista:
# #     print("\033[32ma '{}' palavra {}x apareceu".format(valor,lista.count(valor)))
#
# for valor in lista:
#     qtdVx = lista.count(valor)
#
#     if qtdVx > contagem:
#         contagem = qtdVx
#         palavra = valor
#
# print("\33[32mA palavra que apareceu mais vezes é '{}'  {}x".format(palavra,contagem))
#
# for valor in lista2:
#     print(valor.strip().capitalize())
#
# str = 'O Brasil é penta.'
# lista = str.split(' ')
# string = ','.join(lista)
#
# print(str)
# print(lista)
# print(string)

str = 'O Brasil é penta.'
lista = str.split(' ')

for indice, valor in enumerate(lista):
    print(indice,valor, lista[indice])

lista2 = ["Mari","Jojo","Av"]

for indice, nome in enumerate(lista2):
    print(indice, nome)

n1, n2, n3 = lista2
print(n2)
