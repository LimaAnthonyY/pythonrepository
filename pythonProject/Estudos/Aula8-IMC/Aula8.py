"""
* Criar variáveis para nome (str), idade (int), //check
* altura (float) e peso (float) de uma pessoa //check
* Criar variável com o ano atual (int) //check
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual) //check
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa) //check
* Exibir um texto com todos os valores na tela usando F-Strings(com as chaves) //check
"""
nome = "Luiz"
idade = 35
altura = 1.80
peso = 80.5
imc = peso / altura ** 2
anoAtual = 2022
anoNasc = anoAtual - idade

print(f"{nome} tem {idade} anos, {altura:.2f} de altura e pesa {peso}Kg.")
print("O IMC de {} é {:.2f}".format(nome,imc))
print("{} nasceu em {}".format(nome,anoNasc))