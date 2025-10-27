#nome="papelada";
#idade=2;

#print("Meu Nome:",nome);
#print("Minha Idade:",idade);

#parte inicial da aula








#nome="Gerailton";
#idade=50;

#print("Meu Novo Nome:",nome);
#print("Minha Nova Idade",idade);

#x=25
#z=79

#multiplicacao=x*z
#print("MULTIPLICAÇÃO:",multiplicacao)

#nome=input("qual o Seu nome: ")

#print(nome,"!!")

#print("Nome Bonito")

#idade=input("qual a sua idade?: ")
#print(idade+", Que legal")

#meio da aula








#nome=input("Qual o Seu Nome?: ")
#idade=int(input("Qual a Sua Idade?: "))

#jogo=input("Qual Seu Jogo Favorito MEU Consagrado?:")


#print(f"Legal, Seu Nome é {nome} e Sua Idade é {idade} e Seu Jogo Favorito é {jogo}, Pessima escolha bro") Parte com f_string
#print(f"{nome}, voce tera daqui 5 anos {idade+5} anos")








#valor1=int(input("qual o Primeiro Valor que Você quer?"))

#valor2=int(input("qual o outro valor?"))

#valor_eq=input("Qual Formato de Calculo voce quer?")

#print(f"Você quer {valor1}{valor_eq}{valor2} então o calculo da {valor1-valor2}")







#num1=60
#num2=20

#print(num1+num2)
#print(num1-num2)
#print(num1/num2)
#print(num1//num2)
#print(num1*num2)
#print(num1**num2)
#print(num1%num2)









#Valor_p=int(input("Qual o Valor do produto? "))
#Desconto_v=int(input("Qual o Desconto? "))

#multi_1=Valor_p*Desconto_v
#multi_2=1*100

#total=multi_1/multi_2

#print(f"O desconto será de {total}")








#preco=int(input("Qual o Preço: " ))
#desconto=int(input("Qual o Desconto: "))

#Final=preco-preco*desconto/100

#print(f"O Valor Final do Produto vai Ser R${Final}")









#produto=input("Qual o Produto que voce ira usar: ")
#quantidade=int(input("Qual a quantidade em ml ou g: "))
#uso=int(input("Quanto voce usa por dia: "))

#Q_dias=quantidade/uso

#print(f"Você usara o/a {produto} em {Q_dias:.0f}")








#peso=int(input("qual o seu peso?"))
#altura=float(input("qual a sua altura?"))

#imc=peso/altura**2

#print(f"seu imc é {imc:.2f}")

#calculadora de winrate
partidas=float(input("Quantas partidas? ")) #quantidade de partidas
vitorias=float(input("Quantas vitorias? ")) #quantidade de vitorias

winrate=(vitorias/partidas) * 100 #dividir vitoria por derrota e *100

if winrate >50: 
    print(f"Você está positivado sua taxa de vitoria  é {winrate: .2f}%") #se vencer mais de 50% 
elif winrate == 50:
    print(f"Você está na média sua taxa de vitoria é {winrate}%") #você esta na média
else:
    print(f"Você está negativado sua taxa de vitoria é {winrate: .2f}%") #se vencer menos de 50% 