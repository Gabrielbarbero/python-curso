#idade=int(input(f"qual a sua idade: "))
#carteira= True
#verificador=idade>=18 and carteira
#print(verificador)

#user=input("Digite o seu nome: ")
#senha=input("Digite a sua senha: ")



#verificar=user=="gabriel" and senha=="2025"
#print(verificar)

#Ver se pode dirigir

#idade=int(input("Qual a sua idade: ")) #idade do usuario

#carteira=input("Você tem carteira (sim/não): ") #carteira do usuario

#if idade>=18 and carteira=="sim": #se for maior de idade e tiver carteira vai dar certo
    
    #print("você pode dirigir")

#elif idade<18 or carteira == "não" : #se for menor ou nao tiver carteira

    #print("Você não pode dirigir")

#else: #resposta inconclusiva
    #print("tente denovo")

#nota1=float(input("Qual foi sua primeira nota: "))
#nota2=float(input("Qual foi sua segunda nota: "))

#media=(nota1+nota2)/2

#if media>=7:
    #print(f"Você passou com {media:.2f}")
#elif media>=4:
    #print(f"Você está de recuperação com {media:.2f}")
#else:
    #print(f"Você reprovou com {media:.2f}")

idade=int(input(f"qual sua idade: "))

if idade >= 18:
    print ("Acesso Permitido")

elif idade >=16:
    autorizacao = input("Seus pais altorizam (sim/não): ")
    if autorizacao== "sim:" :
        print("Acesso Permitido com autorização")
else:
    print("Acesso negado")
