#desafio 26
'''
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
'''

#desafio 27
'''
n = 0
def fat(n):
    if n == 1:
        return 1
    else:
        return n * fat(n- 1)
        
n = int(input("escolha o numero do fatorial: "))
fat(n)
print(fat(n))
'''

#desafio 28
'''
def db(num):
    return num * 2
def qd(num):
    return dobro** 2
numu = float(input("Qual o numero"))
db(numu)
dobro = db(numu)
quad = qd(numu)
qd(numu)
print(numu,dobro,quad )
'''

#desafio 29
'''
numero = float(input("de um numero:"))
cubo = lambda numero : numero ** 3
print(cubo(numero))
'''

#desafio 30
'''
n1 = float(input("de um numero:"))
n2 = float(input("de outro numero:"))
multi = lambda n1 , n2 : n1 * n2
print(multi(n1,n2))
'''