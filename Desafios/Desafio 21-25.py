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
    print("tem nao, vaza")