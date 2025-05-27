# PROVA – Introdução à Programação (BIA)
#**Nome completo:** Ivanildo Hyvo Silva Santos
#**Matrícula:** 2022129520039
#**E-mail institucional:** ivanildohyvo@discente.ufg.br

## QUESTÃO 4
import pygame
import random
import sys

# --- Configurações Básicas do Jogo ---
ALTURA_TABULEIRO = 20
LARGURA_TABULEIRO = 10
TAMANHO_BLOCO = 30 # Tamanho de cada "bloco" da peça em pixels

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (100, 100, 100)
CORES_PECA = [
    (0, 255, 255), # I (ciano)
    (255, 255, 0), # O (amarelo)
    (128, 0, 128), # T (roxo)
    (0, 0, 255),   # J (azul)
    (255, 165, 0), # L (laranja)
    (0, 255, 0),   # S (verde)
    (255, 0, 0)    # Z (vermelho)
]

# Margens do tabuleiro na tela
MARGEM_ESQUERDA = 50
MARGEM_SUPERIOR = 50

# Tamanho da janela do Pygame
LARGURA_JANELA = LARGURA_TABULEIRO * TAMANHO_BLOCO + MARGEM_ESQUERDA * 2
ALTURA_JANELA = ALTURA_TABULEIRO * TAMANHO_BLOCO + MARGEM_SUPERIOR * 2

# Representação dos estados das células
VAZIO = 0       # Espaço vazio no tabuleiro
# Em Pygame, usaremos um índice para a cor da peça que preencheu a célula,
# não apenas 1. O índice 0 será para vazio, 1 para a primeira cor, etc.

# --- Definição das Peças (Tetrominós) ---
# Cada peça é uma lista de listas (rotações).
# As peças agora terão um índice na lista TODAS_AS_PECAS para associar a uma cor.
PECA_I = [
    [[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]],
    [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]
]

PECA_O = [
    [[1, 1], [1, 1]]
]

PECA_T = [
    [[0, 1, 0], [1, 1, 1], [0, 0, 0]],
    [[0, 1, 0], [0, 1, 1], [0, 1, 0]],
    [[0, 0, 0], [1, 1, 1], [0, 1, 0]],
    [[0, 1, 0], [1, 1, 0], [0, 1, 0]]
]

PECA_J = [
    [[1, 0, 0], [1, 1, 1], [0, 0, 0]],
    [[0, 1, 1], [0, 1, 0], [0, 1, 0]],
    [[0, 0, 0], [1, 1, 1], [0, 0, 1]],
    [[0, 1, 0], [0, 1, 0], [1, 1, 0]]
]

PECA_L = [
    [[0, 0, 1], [1, 1, 1], [0, 0, 0]],
    [[0, 1, 0], [0, 1, 0], [0, 1, 1]],
    [[0, 0, 0], [1, 1, 1], [1, 0, 0]],
    [[1, 1, 0], [0, 1, 0], [0, 1, 0]]
]

PECA_S = [
    [[0, 1, 1], [1, 1, 0], [0, 0, 0]],
    [[0, 1, 0], [0, 1, 1], [0, 0, 1]]
]

PECA_Z = [
    [[1, 1, 0], [0, 1, 1], [0, 0, 0]],
    [[0, 0, 1], [0, 1, 1], [0, 1, 0]]
]

# Lista de todas as peças disponíveis (associadas ao índice de cor)
TODAS_AS_PECAS = [PECA_I, PECA_O, PECA_T, PECA_J, PECA_L, PECA_S, PECA_Z]

# --- Variáveis de Estado do Jogo (Globais) ---
tabuleiro = [[VAZIO for _ in range(LARGURA_TABULEIRO)] for _ in range(ALTURA_TABULEIRO)]

peca_atual = None             # A peça que está caindo atualmente (índice da peça em TODAS_AS_PECAS)
rotacao_peca_atual = 0        # O índice da rotação atual da peça
posicao_peca_atual_y = 0      # Posição Y (linha) do canto superior esquerdo da peça no tabuleiro
posicao_peca_atual_x = 0      # Posição X (coluna) do canto superior esquerdo da peça no tabuleiro
cor_peca_atual_idx = 0        # Índice da cor da peça atual na lista CORES_PECA

pontuacao = 0                 # Pontuação do jogador
game_over = False             # Sinaliza se o jogo acabou

# --- Funções de Lógica de Jogo (Reaproveitadas e adaptadas) ---

def criar_nova_peca():
    """
    Cria uma nova peça aleatória, a posiciona no topo e define sua cor.
    Verifica se a nova peça já colide, indicando Game Over.
    """
    global peca_atual, rotacao_peca_atual, posicao_peca_atual_y, posicao_peca_atual_x, cor_peca_atual_idx, game_over

    cor_peca_atual_idx = random.randrange(len(TODAS_AS_PECAS))
    peca_atual = TODAS_AS_PECAS[cor_peca_atual_idx] # A peça é a lista de rotações
    
    rotacao_peca_atual = 0
    posicao_peca_atual_y = 0
    largura_peca = len(peca_atual[rotacao_peca_atual][0])
    posicao_peca_atual_x = (LARGURA_TABULEIRO - largura_peca) // 2

    if not pode_mover(peca_atual[rotacao_peca_atual], posicao_peca_atual_y, posicao_peca_atual_x):
        game_over = True
        print("\n!!! GAME OVER !!!")


def pode_mover(peca_matriz, nova_y, nova_x):
    """
    Verifica se uma dada matriz de peça pode ser posicionada nas coordenadas (nova_y, nova_x)
    sem colidir com as bordas do tabuleiro ou com peças já fixadas.

    Args:
        peca_matriz (list): A matriz da peça na sua rotação atual (ex: PECA_I[0]).
        nova_y (int): A nova linha de destino no tabuleiro.
        nova_x (int): A nova coluna de destino no tabuleiro.

    Returns:
        bool: True se a peça pode ser movida, False caso contrário.
    """
    for y_peca, linha_peca in enumerate(peca_matriz):
        for x_peca, valor_celula in enumerate(linha_peca):
            if valor_celula == 1: # Se a célula da peça está preenchida
                tabuleiro_y = nova_y + y_peca
                tabuleiro_x = nova_x + x_peca

                # Colisão com as bordas
                if (tabuleiro_x < 0 or tabuleiro_x >= LARGURA_TABULEIRO or
                        tabuleiro_y >= ALTURA_TABULEIRO):
                    return False
                
                # Colisão com peças já fixadas (apenas se a posição estiver dentro do tabuleiro)
                # O tabuleiro_y < 0 é para ignorar células da peça que estão "acima" do tabuleiro
                # no momento da criação, mas que não colidem.
                if tabuleiro_y >= 0 and tabuleiro[tabuleiro_y][tabuleiro_x] != VAZIO:
                    return False
    return True


def mover_peca_para_baixo():
    """
    Tenta mover a peça atual uma linha para baixo.
    Se não puder, fixa a peça e verifica/remove linhas completas.
    """
    global posicao_peca_atual_y

    if pode_mover(peca_atual[rotacao_peca_atual], posicao_peca_atual_y + 1, posicao_peca_atual_x):
        posicao_peca_atual_y += 1
    else:
        fixar_peca()
        verificar_linhas_completas() # Esta função já cuida da pontuação e da remoção
        if not game_over:
            criar_nova_peca()


def mover_peca_horizontal(delta_x):
    """
    Tenta mover a peça atual horizontalmente.
    """
    global posicao_peca_atual_x
    if pode_mover(peca_atual[rotacao_peca_atual], posicao_peca_atual_y, posicao_peca_atual_x + delta_x):
        posicao_peca_atual_x += delta_x


def girar_peca():
    """
    Tenta girar a peça atual para a próxima rotação.
    """
    global rotacao_peca_atual
    proxima_rotacao = (rotacao_peca_atual + 1) % len(peca_atual)
    if pode_mover(peca_atual[proxima_rotacao], posicao_peca_atual_y, posicao_peca_atual_x):
        rotacao_peca_atual = proxima_rotacao
    # Lógica de "wall kick" mais avançada seria implementada aqui para lidar com rotações próximas às paredes


def fixar_peca():
    """
    Fixa a peça atual no tabuleiro, marcando suas células com o índice da cor da peça.
    """
    for y_peca, linha_peca in enumerate(peca_atual[rotacao_peca_atual]):
        for x_peca, valor_celula in enumerate(linha_peca):
            if valor_celula == 1:
                tabuleiro_y = posicao_peca_atual_y + y_peca
                tabuleiro_x = posicao_peca_atual_x + x_peca
                
                # Garante que não está tentando preencher fora dos limites superiores
                if 0 <= tabuleiro_y < ALTURA_TABULEIRO and 0 <= tabuleiro_x < LARGURA_TABULEIRO:
                    # Fixa a peça usando o índice da cor para identificar no tabuleiro
                    tabuleiro[tabuleiro_y][tabuleiro_x] = cor_peca_atual_idx + 1 # +1 porque VAZIO é 0


def verificar_linhas_completas():
    """
    Verifica e remove linhas completas, atualizando a pontuação e movendo as linhas.
    """
    global tabuleiro, pontuacao
    linhas_removidas = 0
    linhas_a_manter = []

    for y in range(ALTURA_TABULEIRO -1, -1, -1): # Percorre de baixo para cima
        if VAZIO not in tabuleiro[y]: # Se a linha não contém VAZIO, está completa
            linhas_removidas += 1
        else:
            linhas_a_manter.append(tabuleiro[y])
    
    # Preenche o topo do tabuleiro com novas linhas vazias
    novas_linhas_vazias = [[VAZIO for _ in range(LARGURA_TABULEIRO)] for _ in range(linhas_removidas)]
    # Inverte a ordem das linhas a manter para que fiquem no topo
    linhas_a_manter.reverse() 
    tabuleiro = novas_linhas_vazias + linhas_a_manter

    # Lógica de pontuação
    if linhas_removidas == 1:
        pontuacao += 100
    elif linhas_removidas == 2:
        pontuacao += 300
    elif linhas_removidas == 3:
        pontuacao += 500
    elif linhas_removidas >= 4:
        pontuacao += 800


# --- Funções de Desenho com Pygame ---

def desenhar_bloco(superficie, x, y, cor):
    """Desenha um bloco individual na tela."""
    pygame.draw.rect(superficie, cor, (x, y, TAMANHO_BLOCO, TAMANHO_BLOCO), 0)
    pygame.draw.rect(superficie, CINZA, (x, y, TAMANHO_BLOCO, TAMANHO_BLOCO), 1) # Borda do bloco

def desenhar_tabuleiro(superficie):
    """Desenha o tabuleiro fixado na tela."""
    for y in range(ALTURA_TABULEIRO):
        for x in range(LARGURA_TABULEIRO):
            if tabuleiro[y][x] != VAZIO:
                # O valor em tabuleiro[y][x] é o índice da cor + 1
                cor = CORES_PECA[tabuleiro[y][x] - 1]
                desenhar_bloco(superficie,
                               MARGEM_ESQUERDA + x * TAMANHO_BLOCO,
                               MARGEM_SUPERIOR + y * TAMANHO_BLOCO,
                               cor)

def desenhar_peca_atual(superficie):
    """Desenha a peça que está caindo na tela."""
    if peca_atual is not None:
        cor = CORES_PECA[cor_peca_atual_idx]
        for y_peca, linha_peca in enumerate(peca_atual[rotacao_peca_atual]):
            for x_peca, valor_celula in enumerate(linha_peca):
                if valor_celula == 1:
                    desenhar_bloco(superficie,
                                   MARGEM_ESQUERDA + (posicao_peca_atual_x + x_peca) * TAMANHO_BLOCO,
                                   MARGEM_SUPERIOR + (posicao_peca_atual_y + y_peca) * TAMANHO_BLOCO,
                                   cor)

def desenhar_score(superficie):
    """Desenha a pontuação na tela."""
    font = pygame.font.Font(None, 36) # Fonte padrão do Pygame, tamanho 36
    texto = font.render(f"Pontuação: {pontuacao}", True, BRANCO)
    superficie.blit(texto, (MARGEM_ESQUERDA, 10)) # Posição do texto

def desenhar_game_over(superficie):
    """Desenha a mensagem de Game Over na tela."""
    font = pygame.font.Font(None, 72)
    texto = font.render("GAME OVER!", True, (255, 0, 0)) # Vermelho
    # Centraliza o texto
    texto_rect = texto.get_rect(center=(LARGURA_JANELA // 2, ALTURA_JANELA // 2))
    superficie.blit(texto, texto_rect)

# --- Loop Principal do Jogo com Pygame ---

def iniciar_jogo():
    """
    Inicializa o Pygame e executa o loop principal do jogo.
    """
    global game_over, pontuacao, tabuleiro

    pygame.init() # Inicializa todos os módulos do Pygame
    tela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA)) # Cria a janela do jogo
    pygame.display.set_caption("Meu Tetris Simplificado") # Título da janela

    relogio = pygame.time.Clock() # Cria um objeto Clock para controlar o FPS

    # Resetar o estado do jogo para um novo início
    tabuleiro = [[VAZIO for _ in range(LARGURA_TABULEIRO)] for _ in range(ALTURA_TABULEIRO)]
    pontuacao = 0
    game_over = False

    criar_nova_peca()

    tempo_queda = pygame.time.get_ticks() # Tempo em milissegundos desde o início do Pygame
    intervalo_queda = 500 # Peça cai a cada 500ms (0.5 segundos)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Se o usuário clicar no 'X' da janela
                running = False
            
            if event.type == pygame.KEYDOWN and not game_over: # Se uma tecla foi pressionada
                if event.key == pygame.K_LEFT:
                    mover_peca_horizontal(-1)
                elif event.key == pygame.K_RIGHT:
                    mover_peca_horizontal(1)
                elif event.key == pygame.K_UP: # Tecla para girar
                    girar_peca()
                elif event.key == pygame.K_DOWN: # Tecla para queda suave
                    mover_peca_para_baixo()
                    tempo_queda = pygame.time.get_ticks() # Reseta o timer de queda
                # Hard Drop (queda instantânea até o fim)
                elif event.key == pygame.K_SPACE: 
                    while pode_mover(peca_atual[rotacao_peca_atual], posicao_peca_atual_y + 1, posicao_peca_atual_x):
                        posicao_peca_atual_y += 1
                    mover_peca_para_baixo() # Fixa a peça e cria uma nova

        if not game_over:
            # Lógica de queda automática baseada no tempo
            agora = pygame.time.get_ticks()
            if agora - tempo_queda >= intervalo_queda:
                mover_peca_para_baixo()
                tempo_queda = agora

        # --- Desenho na tela ---
        tela.fill(PRETO) # Preenche a tela com preto a cada frame

        # Desenha as bordas do tabuleiro
        pygame.draw.rect(tela, CINZA, (MARGEM_ESQUERDA - 2, MARGEM_SUPERIOR - 2, 
                                       LARGURA_TABULEIRO * TAMANHO_BLOCO + 4, 
                                       ALTURA_TABULEIRO * TAMANHO_BLOCO + 4), 2)

        desenhar_tabuleiro(tela)
        desenhar_peca_atual(tela)
        desenhar_score(tela)

        if game_over:
            desenhar_game_over(tela)

        pygame.display.flip() # Atualiza toda a tela para mostrar o que foi desenhado
        relogio.tick(60) # Limita o jogo a 60 quadros por segundo (FPS)

    pygame.quit() # Desinicializa o Pygame
    sys.exit() # Sai do programa

# --- Execução do Jogo ---
if __name__ == "__main__":
    iniciar_jogo()