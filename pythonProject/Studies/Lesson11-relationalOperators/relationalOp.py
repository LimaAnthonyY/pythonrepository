"""
* Operadores relacionais
* == igualdade
* > maior que
* >= maior ou igual a
* < menor que
* <= menor ou igual a
* != diferente
* and ou |    if int(idade) >= idadeMin and int(idade) <= idadeMax:
* or ou &    if int(idade) >= idadeMin or int(idade) <= idadeMax:
"""

nome = input('Qual o seu nome? ')
idade = input('Qual sua idade? ')

idadeMin = 20
idadeMax = 30

if int(idade) >= idadeMin and int(idade) <= idadeMax:
    print('O senhor(a) {} tem {} anos, por isso já pode pegar um emprestimo.'.format(nome, idade))
else:
    print('O senhor(a) {} tem {} anos, por isso não pode pegar um emprestimo.'.format(nome, idade))
