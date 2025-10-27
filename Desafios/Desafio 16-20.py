#desafio 16
'''
numero = 1
print("para finalizar digite 0")
while numero != 0:
    numero = float(input("coloque um numero:"))
    if numero > 10:
        print("esse numero é maior que 10")
    elif numero == 10:
        print("esse numero é igual a 10")
    else:
        print("esse numero é menor que 10")
'''
#desafio 17
'''
idade = int(input("qual sua idade: "))
if idade > 19:
    print("você é adulto")
elif 19>= idade >= 13:
    print("você é adolescente")
else:
    print("você é criança")
'''
#desafio 18
'''
carros = ["uno","onix","tracker"]
escolha = input("você tem algum carro em mente:").lower()
for i in range(3):
    if escolha == carros[i]:
        print("Temos o carro")
        break
    else:
        pass
if escolha == carros[i]:
    pass
else:
    print("nao temos esse modelo")
'''
#desafio 19
'''
print("tente adivinhar a fruta")
fruta = "abacate"
while True:
    frutaEscolha = input("qual a fruta: ").lower()
    if frutaEscolha == fruta:
        print("parabens voce acertou")
        break
    else:
        print("tente novamente")
'''
#desafio 20
'''
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    if numero%2 == 0:
        print(f"o numero {numero} é par")
    else:
        print(f"o numero {numero} é impar")
'''
