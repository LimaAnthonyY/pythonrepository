#       Índices // valor que tem indices são iteraveis
#       0123456789................33
frase = 'o rato roeu a roupa do rei de roma'
tamanhoFrase = len(frase)
contador = 0
novaStr = ''

inp = input("Qual letra deseja colocar maiúscula? ")

 #  Iteração <- Iterar
while contador < tamanhoFrase:
    # print(frase[contador], contador)
    letra = frase[contador]
    if letra == inp:
        novaStr += inp.upper()
    else:
        novaStr+=letra
    contador +=1

print(novaStr)