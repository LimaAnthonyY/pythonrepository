"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
"""
hora = input("Que horas são?\nEntre 00 ah 23! \n")

try:
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print("Bom dia flor do dia!")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde flor que arde!")
    elif hora >= 18 and hora <= 23:
        print("Boa noite apenas!")
    else :
        print("Horário deve estar entre 00 e 23.")
except:
    print("Horário deve estar entre 00 e 23.")
"""
hora = input("Que horas são?\nEntre 00 ah 23! \n")

if hora.isdigit():
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print("Bom dia flor do dia!")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde flor que arde!")
    elif hora >= 18 and hora <= 23:
        print("Boa noite apenas!")
    else :
        print("Horário deve estar entre 00 e 23.")
else:
    print("Você não digitou um horário.")
