nome = input('Qual seu nome? ')

print(nome or "Não foi digitado nada.")

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Anthony'

variavel = a or b or c or d or e or f or g #  checa todas e para na verdadeira no caso o valor 22
print(variavel)