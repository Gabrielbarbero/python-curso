notas = []
def alunoNota(): # coloca a nota em uma lista
    while True:
        try:
            nota = float(input("Qual a nota do aluno: ")) #entrada
            if 0 <= nota <= 10:
                notas.append(nota) #lista
                return True
            else:
                print("fatalError: Coloque um valor valido (0 a 10)")
        except ValueError:
            print("fatalError: Coloque um valor valido (0 a 10)")
def repetir(): #pergunta se quer perguntar outra nota
    while True:
            repetir1 = input("Quer adicionar outra nota(sim/não): ").lower()
            if repetir1 == "sim":
                return False
            elif repetir1 in ["não","nao"]:
                return True
            else:
                print("fatalError: coloque um valor Valido (sim/não)")
def alunosMedia(): #calcula a media da sala
    print(f"A media dos alunos é {sum(notas) / len(notas):.2f}")