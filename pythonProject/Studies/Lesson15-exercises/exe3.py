"""
Faça um programa que peça o primeiro nome ao usuário. Se o nome tiver 4 letras ou
menos escreve "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

# any Return True if any element of the iterable is true. If the iterable is empty, return False
# chr Return the string representing a character whose Unicode code point is the integer i
# portanto any(chr.isdigit() for chr in nome) ira retorna True se alguma coisa digitada na string for um numero
# e falso caso so tenha sido digitado letras

nome = input("Digite seu primeiro nome: ")


if any(chr.isdigit() for chr in nome) == False:
    qtdCarac = str(len(nome))
    qtdCarac = int(qtdCarac)
    if qtdCarac <= 4 :
        print("Seu nome é curto.")
    elif qtdCarac == 5 or qtdCarac == 6 :
        print("Seu nome é normal.")
    elif qtdCarac > 6 :
        print("Seu nome é muito grande.")
else:
    print("Seu nome possui um número.")
