from random import randint
nsec = randint(1, 20)
guess = 0
while True:
    guess = int(input('Adivinhe o número entre 1 e 20!: '))
    if guess > nsec:
        print(f'{guess} é maior que o número secreto.')
    elif guess < nsec:
        print(f'{guess} é menor que o número secreto.')
    elif guess == nsec:
        print(f'Parabéns! Você acertou! O número era {nsec}!')
        break
    sair = input('Quer desistir?: ')
    if sair == 'sim' or sair == 'SIM' or sair == 'Sim':
        print("Tchau!")
        break
    else:
        continue
print('Fim de jogo.')
