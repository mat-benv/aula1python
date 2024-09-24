notas = {}

print('Sistema de registro e cáculo de médias. ')

while True:
    aluno = input('Digite o nome do aluno (ou "ok" para avançar): ').title().strip()
    if aluno == "Ok":
        break
    if aluno in notas:
        print(f'{aluno} já foi cadastrado.')
        continue
    if aluno == '':
        continue
    notas[aluno] = {}

disciplina = {}

for aluno, disciplina in notas.items():
    while True:
        materia = input('Digite o nome da disciplina (ou "ok" para avançar): ').title().strip()
        if materia == "Ok":
            break
        if materia in disciplina:
            print(f'{materia} já foi cadastrada. ')
            continue
        if materia == '':
            continue
        disciplina[materia] = []
for aluno, disciplina in notas.items():
    nprovas = int(input("Quantas provas para cada disciplina? "))
    i = 0
    while i < nprovas:
        for materia, nota in disciplina.items():
            g = float(input(f"Qual a {i+1}ª nota de {aluno} em {materia}? "))
            nota.append(g)

            i += 1
print(notas)