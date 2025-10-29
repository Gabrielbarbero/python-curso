#desafio 21
'''
cidades = ("Potirendaba","Ibira","Uchoa")
decisao = input("Coloque uma cidade").capitalize()
for cidade in cidades:
    if cidade == decisao:
        print("essa cidade esta na lista.")
        break
    else:
        pass
if cidade != decisao:
    print("essa cidade não esta na lista")
'''
#desafio 22
'''
paises = ["Brasil","Estados unidos","França","Japão","Italia"]
capitais = ["Brasilia","Washington","Paris","Tokyo","Roma"]
i = 0
escolha = input("escolha um pais: ").capitalize()
for pais in paises:
    if pais == escolha:
        break
    else:
        i += 1
        pass
if pais == escolha:
    print(f"a(o) {pais}, a capital chama {capitais[i]}")
else:
    print("nao tenho informações sobre a capital desse pais")
'''
#desafio 22.1

'''
=======

>>>>>>> 16d65b316f2ad4c33badc5cb60cc2ca8a9d00c5f
paisCapitais = {
    "brasil": "brasilia",
    "estados unidos": "whasington",
    "frança": "paris",
    "japão": "tokyo",
    "italia": "roma"
}
escolha = input("Escolha um pais para saber a capital").lower()

if escolha in paisCapitais:
    print(f"{escolha}, {paisCapitais[escolha]}")
else:
<<<<<<< HEAD
    print("tem nao, vaza")
'''

#desafio 23
'''
amigos1 =["lucas","guilherme","davi","rafael","gustavo"]
amigos2 = ["guilherme","rafael","felipe","andré","afonso"]

for nome in amigos1:
    if nome in amigos2:
        print(nome)
'''

#desafio 24
'''
def elevado():
    number = float(input("digite um numero:"))
    potencia = number **2 
    print(potencia)
elevado()
'''

#desafio 25
'''
def soma():
    n1 = float(input("de o valor 1 "))
    n2 = float(input("de o valor 2 "))
    print(n1 + n2)

soma()
'''