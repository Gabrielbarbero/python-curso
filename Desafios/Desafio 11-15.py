#desafio 11
'''
for i in range (1,11):
    print(i)
'''
#desafio 12
'''
estados = ["amazonas","amapa","acre","sergipe"]
cidades = ["manaus","macapa","rio branco","aracaju"]
for i in range(0,4):
    print(f"CEP{i+1}")
    for v in range (0,4):
        print(f"{estados[i]} {cidades[v]}")
'''
#desafio 13
'''
i = 1
while (i<=10):
    print(i)
    i += 1    
'''
#desafio 14
'''
i = 1
while i <= 10:
    print(i)
    i += 1
    if i == 5:
        break
print("\n")
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1
'''
#desafio 15
'''
contador = 0
carros = ["Civic","Fiesta","Civic","S10","Civic","Kwid"]
for carro in carros:
    if carro == "Civic":
        contador += 1
print(contador)
'''
