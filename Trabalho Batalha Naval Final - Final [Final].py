# Universidade do Vale do Itajaí - Campus Kobrasol
# Escola Politécnica
# Disciplina - Introdução a Python
# Professor: Evandro
# Trabalho para M2, Batalha Naval
# Entrega em 29/10/2024
# Autores:
#           Mateus Pereira Benvenutti
#           Guilherme Silveira de Melo

import random
import time

# Inicializa o tabuleiro do jogador e do computador
tabuleiro_player = [
    ["~" for _ in range(10)] for _ in range(10)
]
tabuleiro_pc_vw = [
    ["~" for _ in range(10)] for _ in range(10)
]  # Tabuleiro visível do computador
tabuleiro_pc_hf = [
    ["~" for _ in range(10)] for _ in range(10)
]  # Tabuleiro de referência do computador

# Dicionário para monitorar os navios do player 

navios_player = {
    "PA": {'nome': 'porta-aviões', "tamanho": 5, "coordenadas": [], "simbolo": "P"},
    "NT1": {'nome': 'navio tanque',"tamanho": 4, "coordenadas": [], "simbolo": "N"},
    "NT2": {'nome': 'navio tanque', "tamanho": 4, "coordenadas": [], "simbolo": "N"},
    "CT1": {'nome': 'contratopedeiro', "tamanho": 3, "coordenadas": [], "simbolo": "C"},
    "CT2": {'nome': 'contratopedeiro', "tamanho": 3, "coordenadas": [], "simbolo": "C"},
    "CP3": {'nome': 'contratopedeiro', "tamanho": 3, "coordenadas": [], "simbolo": "C"},
    "S1": {'nome': 'submarino', "tamanho": 2, "coordenadas": [], "simbolo": "S"},
    "S2": {'nome': 'submarino', "tamanho": 2, "coordenadas": [], "simbolo": "S"},
    "S3": {'nome': 'submarino', "tamanho": 2, "coordenadas": [], "simbolo": "S"},
    "S4": {'nome': 'submarino', "tamanho": 2, "coordenadas": [], "simbolo": "S"}
}

# Dicionário para monitorar os navios do computador

navios_pc = {
    "PA": {'nome': 'porta-aviões', "tamanho": 5, "coordenadas": [], "simbolo": "P"},
    "NT1": {'nome': 'navio tanque',"tamanho": 4, "coordenadas": [], "simbolo": "N"},
    "NT2": {'nome': 'navio tanque', "tamanho": 4, "coordenadas": [], "simbolo": "N"},
    "CT1": {'nome': 'contratopedeiro', "tamanho": 3, "coordenadas": [], "simbolo": "C"},
    "CT2": {'nome': 'contratopedeiro', "tamanho": 3, "coordenadas": [], "simbolo": "C"},
    "CP3": {'nome': 'contratopedeiro', "tamanho": 3, "coordenadas": [], "simbolo": "C"},
    "S1": {'nome': 'submarino', "tamanho": 2, "coordenadas": [], "simbolo": "S"},
    "S2": {'nome': 'submarino', "tamanho": 2, "coordenadas": [], "simbolo": "S"},
    "S3": {'nome': 'submarino', "tamanho": 2, "coordenadas": [], "simbolo": "S"},
    "S4": {'nome': 'submarino', "tamanho": 2, "coordenadas": [], "simbolo": "S"}
}


# Dicionário para alterar as letras do input do usuário para números
posicoes = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
}

# E o inverso para montar a listas de posições dos navios
posicoes_inverso = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J'
}

# Funções do jogo:

def exibir_tabuleiro(tabuleiro, nome_tabuleiro):
    '''Exibe o tabuleiro selecionado.
        Args: 
            tabuleiro(list[list[str]]): Tabuleiro do jogador ou computador.
            nome_tabuleiro[str]: Nome do tabuleiro'''
    print(f"\n{nome_tabuleiro}")
    # Exibe os números das colunas no topo
    numeros_colunas = "   " + " ".join([str(i) for i in range(10)])
    print(numeros_colunas)
    # Exibe as linhas com as letras e o tabuleiro
    for letra_linha, linha in zip(posicoes.keys(), tabuleiro):
        print(f"{letra_linha}  " + " ".join(linha))


def exibir_tabuleiros():
    '''Exibe os dois tabuleiros visíveis.'''
    exibir_tabuleiro(tabuleiro_player, "Seu Tabuleiro:")
    exibir_tabuleiro(tabuleiro_pc_vw, "Tabuleiro do Computador:")


def posicionar_navios():
    '''Pede para o player posicionar os navios dele.
    Posiciona os navios no tabuleiro.
    Prenche a lista de posições de cada navio no dicionário.
    '''
    print('Posicione seus navios. ')
    for sigla, navios in navios_player.items(): # Ìtera sobre cada navio individual do dicionário
        exibir_tabuleiro(tabuleiro_player, 'Seu Tabuleiro:') # Vai mostrando o tabuleiro conforme é preenchido
        if navios['tamanho'] == 5: # Como só tem um porta-aviões, esse if é para mostrar o texto apropriado
            print('Posicione seu porta-aviões (5 espaços): ')
        else: # sigla [-1:] pega o último digito da sigla de cada navio para mostrar qual deles é
            print(f'Posicione seu {sigla[-1:]}º {navios['nome']} ({navios['tamanho']} espaços): ')
        while True:
            orientacao = input('Orientação vertical ou horizonta? V/H ').strip().upper()
            if orientacao == 'V':
                print(f'O {navios['nome']} será posicionado de cima para baixo.')
                break
            elif orientacao == 'H':
                print(f'O {navios['nome']} será posicionado da direita para a esquerda.')
                break
            else:
                continue
        while True:
            posicao_inicial = input(f'Digite a posição inicial do {navios['nome']} (Ex.: A1, D7): ').upper().strip()
            try:
                # Prepara as coordenadas
                x, y = posicao_inicial[0], posicao_inicial[1]
                y = int(y)
                x = posicoes[x]
                if orientacao == 'H':
                    # Verifica se os espaços adjacentes estão vazios e se todo comprimento do navio
                    # vai caber no tabuleiro. Identico para a orientação vertical.
                    posicao_valida = all(
                        all(
                            tabuleiro_player[m][n] == '~'
                            for m in range(x-1, x+2)
                            for n in range(b-1, b+2)
                            if 0 <= m < 10 and 0 <= n < 10   
                        ) and 0 <= b < 10 and 0 <= x < 10
                    for b in range(y, y+navios['tamanho'])
                    )
                    if posicao_valida:
                        for b in range(y, y + navios['tamanho']):
                            tabuleiro_player[x][b] = navios['simbolo'] # Desenha no tabuleiro
                            coord = f'{posicao_inicial[0]}{b}'
                            navios['coordenadas'].append(coord) # Salva as coordenadas no dicionário. 
                    else:
                        print("Posição inválida. Seu navio está encostando em outro ou está indo para fora do tabuleiro.")
                        continue                    
                elif orientacao == 'V':
                    posicao_valida = all(
                        all(
                            tabuleiro_player[m][n] == '~'
                            for m in range(a-1, a+2)
                            for n in range(y-1, y+2)
                            if 0 <= m < 10 and 0 <= n < 10   
                        ) and 0 <= y < 10 and 0 <= a < 10
                    for a in range(x, x+navios['tamanho'])
                    )
                    if posicao_valida:
                        for a in range(x, x + navios['tamanho']):
                            tabuleiro_player[a][y] = navios['simbolo']
                            coord = f'{posicoes_inverso[a]}{y}'
                            navios['coordenadas'].append(coord)
                    else:
                        print("Posição inválida. Seu navio está encostando em outro ou está inido fora do tabuleiro.")
                        continue
            except Exception:
                print('Posição inválida.')
                continue
            break

def gerar_posicoes_pc(): # Praticamente identico a posicionar_navios(), mas utilizando random e sem mensagens.
    '''Gera aleatoriamente as posição dos navios do computador.
    Marca no tabuleiro de referência do computador.
    Preenche a lista de posições no dicionário.'''
    for navios in navios_pc.values():
        orientacao = random.randint(0, 1)
        while True:
            try:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                if orientacao == 0:
                    posicao_valida = all(
                        all(
                            tabuleiro_pc_hf[m][n] == '~'
                            for m in range(x-1, x+2)
                            for n in range(b-1, b+2)
                            if 0 <= m < 10 and 0 <= n < 10   
                        ) and 0 <= b < 10 and 0 <= x < 10
                    for b in range(y, y+navios['tamanho'])
                    )
                    if posicao_valida:
                        for b in range(y, y + navios['tamanho']):
                            tabuleiro_pc_hf[x][b] = navios['simbolo']
                            coord = f'{posicoes_inverso[x]}{b}'
                            navios['coordenadas'].append(coord)
                    else:
                        continue                    
                elif orientacao == 1:
                    posicao_valida = all(
                        all(
                            tabuleiro_pc_hf[m][n] == '~'
                            for m in range(a-1, a+2)
                            for n in range(y-1, y+2)
                            if 0 <= m < 10 and 0 <= n < 10   
                        ) and 0 <= y < 10 and 0 <= a < 10
                    for a in range(x, x+navios['tamanho'])
                    )
                    if posicao_valida:
                        for a in range(x, x + navios['tamanho']):
                            tabuleiro_pc_hf[a][y] = navios['simbolo']
                            coord = f'{posicoes_inverso[a]}{y}'
                            navios['coordenadas'].append(coord)
                    else:
                        continue
            except Exception:
                continue
            break


def atingiu_player(coordenada: int):
    '''Verifica se o jogador atingiu e se afundou algum navio do computador.
        Funções separadas por causa da mensagem a ser exibida apenas.
        Args:
            navios_pc(dict): Dicionário dos navios do compudador.
            coordenada(str): Coordenada da jogada do jogador.'''
    for navio in navios_pc.values():
        if coordenada in navio["coordenadas"]:
            print(f'Você atingiu um {navio['nome']}!')
            time.sleep(2)
            navio["coordenadas"].remove(coordenada)  # Remove a coordenada atingida
            if not navio["coordenadas"]:  # Se todas as coordenadas foram atingidas
                print(f"O {navio['nome']} foi afundado!")
                time.sleep(2)

def atingiu_pc(coordenada: int):
    '''Verifica se o computador atingiu e se afundou algum navio do jogador.
        Funções separadas por causa da mensagem a ser exibida apenas.
        Args:
            navios_player(dict): Dicionário dos navios do jogador.
            coordenada(str): Coordenada da jogada do jogador.'''
    for navio in navios_player.values():
        if coordenada in navio["coordenadas"]:
            print(f'O computador atingiu um {navio['nome']}!')
            time.sleep(2)
            navio["coordenadas"].remove(coordenada)  # Remove a coordenada atingida
            if not navio["coordenadas"]:  # Se todas as coordenadas foram atingidas
                print(f"O seu {navio['nome']} foi afundado!")
                time.sleep(2)

def verificar_vitoria(navios:dict) -> bool:
    '''Verifica se todas a listas de coordenadas no dicionário estão vazias.
    Args:
        navios(dict): Informações dos navios do jogador ou PC.
    Return: 
        bool: Se venceu.'''
    return all(not navio["coordenadas"] for navio in navios.values())


def jogada_humano():
    while True:
        try:
            coordenada = input("Digite a posição (Ex: A1, B4): ").upper().strip()
            x, y = coordenada[0], coordenada[1]  # Separa a letra e o número
            y = int(y)
            x = posicoes[x]  # Converte a letra para o índice correspondente
            if tabuleiro_pc_vw[x][y] == "~":  # Verificando se o usuário escolheu um ponto vazio
                if tabuleiro_pc_hf[x][y] == "~":  # Verificando se errou
                    print("Você errou!")
                    tabuleiro_pc_vw[x][y] = "O"  # Marca o erro
                    time.sleep(2)
                    break
                if tabuleiro_pc_hf[x][y] != "~":  # Verifica se acertou
                    tabuleiro_pc_vw[x][y] = 'X'
                    atingiu_player(coordenada)
                    if verificar_vitoria(navios_pc):
                        break
                    exibir_tabuleiros()
                    print("Jogue novamente.")
                    continue
            else:
                print("Jogada inválida. Tente novamente.")
        except Exception:
            print("Jogada inválida. Tente novamente.")


def jogada_pc():
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        coordenada = f'{posicoes_inverso[x]}{y}'
        if tabuleiro_player[x][y] == "O" or tabuleiro_player[x][y] == "X": #Evitando que o computador escolha um ponto ocupado
            continue
        else:
            print(f'O computador escolheu {coordenada}.')
            time.sleep(2)
            if tabuleiro_player[x][y] == "~":
                print("O computador errou!")
                tabuleiro_player[x][y] = "O"
                time.sleep(2)
                break
            else:
                tabuleiro_player[x][y] = "X"
                atingiu_pc(coordenada)
                if verificar_vitoria(navios_player):
                    break
                exibir_tabuleiros()
                print("Ele vai jogar novamente...")
                time.sleep(2)
                continue


if __name__ == '__main__':
    while True:
        gerar_posicoes_pc()
        posicionar_navios()
        # Jogo principal
        while True:
            exibir_tabuleiros()  # Exibe os tabuleiros após cada jogada
            jogada_humano()  # Jogada do jogador
            if verificar_vitoria(navios_pc):
                print('Parabéns! Você venceu!')
                input()
                break
            exibir_tabuleiros()  # Exibe os tabuleiros novamente
            jogada_pc()  # Jogada do computador
            if verificar_vitoria(navios_player):
                print('Que pena! O computador venceu.')
                input()
                break
