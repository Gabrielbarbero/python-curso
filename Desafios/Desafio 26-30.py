#desafio 26

def potencial():
    numero = float(input("de o valor do numero: "))
    potencia = input("de o valor do expoente: ")
    if potencia == "":
        potencia = 2
        print(numero ** potencia)
    else:
        potencia = int(potencia)
        print(numero ** potencia)

potencial()