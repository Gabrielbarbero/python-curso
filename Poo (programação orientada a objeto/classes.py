'''
class carro:
    def __init__(self,cor,modelo):
        self.cor = cor
        self.modelo = modelo
    def corCarro (self):
        print(f"a cor do carro é {self.cor}")
    def modeloCarro (self):
        print(f"o modelo do carro é {self.modelo}")

carro1 = input("qual a cor: ")
carro1m =input("qual o modelo do carro: ")
caracteristicasCarro1 = carro(carro1,carro1m)
caracteristicasCarro1.corCarro()
caracteristicasCarro1.modeloCarro()


print("Vamos escolher do carro do seu primo")
carro2 = input("qual a cor: ")
carro2m =input("qual o modelo do carro: ")

caracteristicasCarro2 = carro(carro2,carro2m)
caracteristicasCarro2.corCarro()
caracteristicasCarro2.modeloCarro()
'''

class formas:
    def __init__(self,nome,vertices,arestas,):
        self.nome = nome
        self.vertices = vertices
        self.arestas = arestas

    def valorNome(self):
        if self.nome == "circulo":
            self.vertices = 0
            self.arestas = 1
        elif self.nome == "triangulo":
            self.vertices = 3
            self.arestas = 3
        elif self.nome == "quadrado":
            self.vertices = 4
            self.arestas = 4
        elif self.nome == "pentagono":
            self.vertices = 5
            self.arestas = 5
        elif self.nome == "hexagono":
            self.vertices = 6
            self.arestas = 6
        elif self.nome == "heptagono":
            self.vertices = 7
            self.arestas = 7
        elif self.nome == "octogono":
            self.vertices = 8
            self.arestas = 8
        else:
            print("forma desconhecida")
        if self.arestas < 1:
            self.vertices = int(input("coloque o numero de vertices dessa forma: "))
            self.arestas = int(input("coloque o numero de arestas dessa forma: "))
            print("obrigado por sua contribuição")
        else:
            print(f"sua forma é {self.nome} ela possui {self.vertices} vertices e {self.arestas} arestas")
nome1 = input("qual o nome da forma geometrica: ").lower()
infoForma = formas(nome1,0,0)
infoForma.valorNome()