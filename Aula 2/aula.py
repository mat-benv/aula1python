chamada = []
nome = ' '
while nome.lower() != "pare":
    nome = input("Digite o nome: ")
    nome = nome.title()
    chamada.append(nome)
chamada.sort()
chamada.pop()
print(list(chamada))
