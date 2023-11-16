"""
** for in em Python
** Iterando str com for
** Função range(start=0, stop, step=1)
"""
#
# texto = 'Python'
#
# for n, letra in enumerate(texto):
#     print(n,letra)
#
# for n in range (1, 10,1):
#     if n == '1':
#         print(n)

# num = int(input("Digite um número: "))
# tot = 0
# for c in range(1,num+1):
#     if num % c == 0:
#         print('\033[33m', end=" ")
#         tot += 1
#     else:
#         print('\033[31m', end=" ")
#     print("{}".format(c),end=" ")
# print("\n\033[mNúmero {} foi divisível {} vezes".format(num,tot))
# if tot == 2:
#     print("É PRIMO")
# else:
#     print("NÃO É")


# texto = 'Python'
# newStr = ''
#
# for letra in texto:
#     if letra == 't':
#         newStr = newStr + letra.upper()
#     elif letra == 'h':
#         newStr += letra.upper()
#     else:
#         newStr += letra.lower()
# print(newStr) 

num = int(input("Digite um número: "))
primos=[]
for x in range(1,num+1):
    cont = 0
    for y in range (1,x+1):
        if x%y==0:
            cont+=1
    if cont <=2:
        primos.append(x)
print("\033[31m{}".format(primos))
