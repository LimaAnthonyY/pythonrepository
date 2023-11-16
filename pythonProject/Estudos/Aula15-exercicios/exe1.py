"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um numero
inteiro, informe que não é um número inteiro.
"""

"""
numero = input ("Digite um número inteiro: ")
try :
    numero = int(numero)
    if numero%2 == 0:
        print("{} é um número par".format(numero))
    else:
        print("{} é um número ímpar.".format(numero))
except:
    print("Não é um número inteiro.")

"""
numero = input ("Digite um número inteiro: ")
if numero.isdigit():
    numero = int(numero)
    if numero%2 == 0:
        print("{} é um número par".format(numero))
    else:
        print("{} é um número ímpar.".format(numero))
else:
    print("Não é um número inteiro.")