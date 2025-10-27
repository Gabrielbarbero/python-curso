#Imprima os números de 1 a 10 usando um laço for.
'''
for v in range(1,11):
    print(v)
'''
'''
soma = 0

while True:
    numero=int(input("Qual o numero: "))
    if numero == 0:
        break
    else:
        soma += numero
print(soma)
'''
'''
multi = int(input("Coloque um numero:"))
for v in range(1, 11):
    total = v*multi
    print(total)
'''

'''
i = 1
v = int(input("Qual o número: "))
while i <= v:
    if i % 2 == 0:
        print(i)
    i += 1
'''
'''
i = 0
v = int(input("Informe o numero: "))
while i <= v:
    if i == 0:
        print(f"{i} não existe")
    elif i % 2 == 0:
        print (f"{i} é par")
    else:
        print(f"{i} é impar")
    i += 1
'''
'''
soma = 0
for f in range(1,101):
    if f % 2 == 0:
        print(f"{f} é pár")
        soma += 1
    else:
        print("--------------------------")
print(f"foram {soma} numeros pares")
'''

import random

numeroSecreto = random.randint(1,5555555)
tentativa = 0
while True:
    numero = int(input("fale o numero: "))
    if numero == numeroSecreto:
        tentativa += 1
        print(f"você acertou em {tentativa} tentativas")
        break
    elif numero < numeroSecreto:
        tentativa += 1
        print(f"é maior ({tentativa})")

    elif numero > numeroSecreto:
        tentativa += 1
        print(f"é menor ({tentativa})")

'''
vezes = 0
while True:

    numero =int(input("Numero: "))

    if numero<= 1:

        print("Error:Escreva um numero Válido")
    else:

        break
        

for i in range(1 , numero +1):

    if numero% i == 0:

        vezes += 1

if vezes == 2:

    print("é primo")

else:
    
    print("não é primo")


soma = 0

while True:
    perfeito = int(input("de o valor de um numero para checar se ele é perfeito: "))
    if perfeito>1:
        break
    else:
        print("Fatal_Error:Coloque um numero valido")
    
for i in range(1, perfeito):
    if perfeito % i == 0:
        soma += i

if soma == perfeito:
    print("ele é perfeito")
else:
    print("ele não é perfeito")
'''
