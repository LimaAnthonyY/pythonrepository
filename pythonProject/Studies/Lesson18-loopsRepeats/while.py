"""
** While em python
** Utilizado para realizar ações enquanto
** uma condição for verdadeira
"""
x = 0
#  while x < 10: #  Loop infinito
#     if x == 3:
#         x += 1
#         continue
#
#     print("{}".format(x))
#     x+=1
# print("Cabo")

# while x < 10: #  Loop infinito
#     if x == 3:
#         break
#
#     print("{}".format(x))
#     x+=1 #  = x + 1
# print("Cabo")

# x = 0
# y = 0
#
# while x < 10:
#     y = 0
#     while y < 5:
#         print("X vale {} e Y vale {}".format(x+1,y+1))
#         y+=1
#     x += 1
#
# print("cabo!")

while True:
    print(    )
    num1 = input("Digite um numero: ")
    num2 = input("Digite outro numero: ")
    if not num1.isnumeric() or not num2.isnumeric():
        print("Você precisa digitar um número.\nPara sair digite 'sair' ou enter para continuar")
        sair = input("")
        if sair == "sair" or sair == "Sair":
            break
        continue
    operador = input("Digite um operador:\nExemplos:\n+\n-\n*\n/\n")

    num1=float(num1)
    num2=float(num2)
    # + - / *
    if operador == "+":
        print("{:.2f}".format(num1+num2))
    elif operador == "/":
        print("{:.2f}".format(num1/num2))
    elif operador == "*":
        print("{:.2f}".format(num1*num2))
    elif operador == "-":
        print("{:.2f}".format(num1-num2))
    else : #  if operador != "-" and operador != "/" and operador != "*" and operador != "+":
        print("Operador inválido")

    print("Deseja continuar?\nPara sair digite 'Sair' ou enter para continuar")
    sair = input("")
    if sair == "sair" or sair == "Sair":
        break