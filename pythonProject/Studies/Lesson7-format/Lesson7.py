"""
Iniciar com letra, pode conter números, separar _,letrar minúsculas
"""
nome = 'Anthony'  # Atribuição variavel, salvando um valor na memória
idade = 20  # int
altura = 1.75  # float
e_maior = idade > 18  # bool
data_1 = True  # bool
data_atual = 2022  # int
peso = 64
imc = peso/(altura ** 2)

print (nome, 'tem', idade, 'anos de idade e seu IMC é:', imc)
print (f'{nome} tem {idade} anos de idade e seu IMC é: {imc:.2f}')  # função format
print ('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome,idade,imc))  # função format
print ('{n} tem {i} anos de idade e seu imc é {im:.2f}'.format(n=nome,i=idade,im=imc))  # função format
