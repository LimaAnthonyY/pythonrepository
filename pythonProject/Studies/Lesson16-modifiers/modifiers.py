"""
Formatando valores com modificadores

** :s - Texto (str)
** nome = 'Anthony Lima'
** print("{:s}".format(nome))
**
** :d - Inteiros (int)
** num = '10'
** print("{:d}".format(num))
**
** :f - Números flutuantes (float)  # formatando tipo float
** num = '100'
** print("{:f}".format(num))
**
** :.(NÚMERO)F - quantidade de casas decímais (float)
** num1 = 10
** num2 = 3
** divisao = num1 / num2
** print("{:.2f}".format(divisao))
**
** :(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)
** num1 = 1
** print("{:0>10}".format(num1))
** num2 = 1150
** print("{:0<10}".format(num2))
**
** num2 = 1150
** print("{:0>10.2f}".format(num2))
**
** > - Esquerda
** < - Direita
** ^ - Centro
"""

nome = 'tOIn'
sobrenome = 'Fallen'
nomeForm = "{:#^8}".format(nome)
sobrenomeForm = "{:$^8}".format(sobrenome)
print(nomeForm)
print(sobrenomeForm)

print(nome.lower())
print(nome.upper())
print(nome.title())


