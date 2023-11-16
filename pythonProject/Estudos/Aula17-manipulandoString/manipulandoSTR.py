"""
** String indices
** Fatiamento de Strings [inicio:fim:passo]
** Funções built-in len, abs, type, print, etc...
** Essas funções podem ser usadas diretamente em cada tipo.
** Dúvida consultar documentação
"""
#  positivos [012345678] [Python s2]
texto = 'Python s2'
#  negativos -[987654321] [Python s2]
print(texto[0])
print(texto[-9])
url = 'https://www.google.com.br/'
print(url[:-1])

novaStr = texto [2:6] #  [inicioDOcorte:fimDOcorte]
print(novaStr)
novaStr2 = texto [:6] #  Ele não inclui o ultimo caracter
print(novaStr2)
novaStr3 = texto [7:] #  Ele não inclui o ultimo caracter
print(novaStr3)
novaStr4 = texto [:-3] #  Ele não inclui o ultimo caracter
print(novaStr4)

texto2 = texto [0::2] #  [inicioDOcorte:fimDOcorte:pula]
print(texto2)

print(len(texto))