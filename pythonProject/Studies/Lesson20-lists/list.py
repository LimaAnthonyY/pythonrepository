"""
** fatiamento
** append, insert, pop, del, clear, extend, +
** min, max
** range
"""
# #         1   2   3   4   5
# lista = ['A','B','C','D','E']
# #         5   4   3   2   1
#
#
# lista2 = ['1','0','2','3','4']
# lista2[4] = 'ANTES DE VOLTAR AVANCE PARA TRÁS'
# string = 'ABCDE'
#
# print(lista[1])
# print(lista2[1])
# print(lista2[4])
# print(lista[0:4]) #  Vai do indice 0 até o 3, pois o 4 não e incluido
# print(lista[2:]) #  Vai do indice 2 até o final
# print(lista[::2]) #  Vai do indice 0 até o final, e pula 2
# print(lista[::-1]) #  Vai do indice 4 até o começo, de forma invertida
# lista3 = lista + lista2
# print(lista3)
#
# lista.extend(lista2) #  faz igual o + adiciona uma extensão a lista
# print(lista)
#
# print(lista2)
# lista2.append("COM PELÉ") #  adiciona um caracter ao final da lista
# print(lista2)
#
# lista2.insert(0,"PELÉ NO INICIO") #  adiciona um caracter no local q vc quiser da lista
# print(lista2)
#
# lista2.pop()
# print(lista2) #  deleta o ultimo caracter
#
# l2 = [1,2,3,4,5,6,7,8,9]
# print(l2)
# del(l2[3:5]) #  exclui um trecho
# print(l2)
#
# print(max(l2)) #  imprimir o numero maximo ou utiliza-lo
# print(min(l2)) #  imprimir o numero minimo ou utiliza-lo
#
# l2 = range(1,10)
# print(l2)
# l2 = [1,2,3,4,5,6,7,8,9]
# l2 = list(range(0,100,8))
# print(l2)
#
# # iterando
# soma=0
# for valor in l2:
#     soma+=valor
#     print(valor)
# print(soma)
#
# l2 = ['String', True, 10, -20.5]
#
# for elem in l2 :
#     print("\033[32mo tipo de é {} e seu valor é {} ".format(type(elem),elem))

## Jogo da Forca
secreto = "botijao"
digitados = []
chances = 3

while True :
    if chances <= 0:
        print('\33[31mVocê perde mané!')
        break
    letra = input("\33[33mDigite uma letra: ")
    digitados.append(letra) #  capturando as letra digitadas
        
    if len(letra) > 1:
        print("\33[31mPode não amigao.\nSó uma letra")
        chances -= 1
        print("\33[32mVocê ainda tem {} chances".format(chances))
        continue

    if letra in secreto:
        print("\33[33mBOA CUZÃO, TEM A LETRA AQUI CACHORRO")
    else :
        print("\33[31mAcertou não cuzão.\nTenta de novo")
        print("\33[32mVocê ainda tem {} chances".format(chances))
        chances -= 1
        digitados.pop()

    secretoTemp = ''
    for letraSec in secreto:
        if letraSec in digitados:
            secretoTemp += letraSec
        else:
            secretoTemp += "*"

    if secretoTemp == secreto:
        print("\33[32mVOCÊ GANHOU CUZAO TU É PIKA A PALAVRA É : {}".format(secretoTemp))
        break
    else:
        print("\33[31mVoce perdeu padrim newba")
    print("\33[32mVocê ainda tem {} chances".format(chances))

