presenca_alunos = {}

print('Sistema de registro de presença.')

while True:
    aluno = input('Digite o nome do aluno (ou "ok" para avançar): ').title()
    if aluno == "Ok":
        break
    presenca_alunos[aluno] = []
#print(presenca_alunos)

dias = int(input('Quantos dias de aula? '))

i = 0
while i < dias:
    for nome, presenca in presenca_alunos.items():
        g = input(f"{nome} está na aula {i+1}?(P/A) ").upper()
        if g == 'P':
            presenca.append(1)
        elif g == 'A':
            presenca.append(0)
        else:
            print('Input inválida, digite P ou A para presença ou ausência. ')
            continue
    i += 1

for nome, presenca in presenca_alunos.items():
    print(f'{nome} teve {(sum(presenca) / dias) * 100:.1f}% de presença.')