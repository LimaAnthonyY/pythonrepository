"""
* Operadores logicos
* and  Verifica e só aceita se as duas empressões ou mais, são verdadeiras
* or  Verifica e aceita se qualquer uma das empressões, é verdadeiras
* not  Inverte a expressão ou pergunta se a variavel possui algum valor -- retorna valor booleano
a = ''
if not a:
print('Por favor, preencha o valor de A.')
a = 2
b = 3
if not b > a:
    print('b > a')
else:
    print('a > b')
* in Verifica se n existe em uma variavel
nome = 'Anthony'
if 'y' in nome :
    print("Existe a letra 'a' no seu nome.")
* not in
* and ou |    if int(idade) >= idadeMin and int(idade) <= idadeMax:
* or ou &    if int(idade) >= idadeMin or int(idade) <= idadeMax:
"""

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Anthony'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Conseguiu logar pae.')
else:
    print('Errou alguma coisa pae.')