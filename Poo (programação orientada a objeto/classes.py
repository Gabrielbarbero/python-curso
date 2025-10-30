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