"""
** for / else em python
"""

variavel = ['Ca', 'Ra','lho','por', 'tra']
comecaJ = False

for valor in variavel:
    if valor.lower().startswith('R'):
        comecaJ = True
    else :
        print("IE IE")

if comecaJ:
    print("EI EI")
else:
    print("Não monkey")