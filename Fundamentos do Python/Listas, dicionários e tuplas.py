"""
nomes = ["Gabriel","Matheus","João","Carlos"]
i = 0
for i in range (1,5):
    print(nomes[i]) #baseado em index inicia no 0
    i += 1


nomes = ["Gabriel","Matheus","João","Carlos","Lucas","Felipe"]
print (nomes)
nomes.append ("Maria")
print(nomes)
nomes.remove ("Carlos")
print(nomes)

objetivos = []
while True:
    objetivos.append(input("Fale um objetivo: "))
    continuar =input("Você tem mais objetivos? se sim digite sim: ").lower()
    if continuar == "sim":
        print()
    else:
        break

objetivoEsp = input("Você tem algum objetivo especifico para ser mostrado: ").lower()
if objetivoEsp == "sim":
    i = int(input("Qual o objetivo: "))
    i -=1
    print(objetivos[i])
else:
    print(objetivos)
    """
