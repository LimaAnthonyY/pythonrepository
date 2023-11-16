"""
Operador ternário em python
"""
loggedUser = False
nomeUser = "Anthony"

# if loggedUser:
#     msg = 'Hello {}'.format(nomeUser)
# else:
#     msg = 'Usuario não logado.'

msg = '\33[32mHello {}'.format(nomeUser) if loggedUser else '\33[31mUsuario não logado.'
print(msg)

idade = input("Digite a idade: ")
# if idade >= 18 :
#     print("KOé")
# else:
#     print("Taxado")

if not idade.isnumeric():
    print('Digite apenas numero.')
else:
    idade = int(idade)
    emaior = (idade>=18)
    msg = 'KOé' if emaior else 'Taxado'
    print(msg)
