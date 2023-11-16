"""
Leia a documentação cuzão
"""
"""
num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

print(int(num1)+int(num2))
"""
# isnumeric isdigt isdecimal
# números e positivos (12345)
"""
num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1+num2)
else:
    print('Deu certo não')

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

try:
    num1 = float(num1)
    num2 = float(num2)

    print("{:.2f}".format(num1 + num2))
except:
    print('Deu certo não')
"""
valor = True

if valor:
    #Explicando oq vai rola aqui
    pass  # ignora ou guarda lugar
else:
    print('Tchal')

if valor:
    #Explicando oq vai rola aqui
    ...  # ignora ou guarda lugar
else:
    print('Tchal')
