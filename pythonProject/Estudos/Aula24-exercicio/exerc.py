"""
Criar 2 contadores
1 subindo
1 descendo
"""
cont = 0
cont2 = 10
x = 0
num = 10
for x in range(1,num+1):
    print(cont, cont2)
    cont += 1
    cont2 -= 1

for p, r in enumerate(range(10,1,-1)):
    print(p, r)