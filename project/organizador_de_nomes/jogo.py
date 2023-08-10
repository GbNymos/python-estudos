import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da janela
largura = 800
altura = 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Mini Jogo com Pygame")

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Variáveis do jogador
jogador_largura = 50
jogador_altura = 50
jogador_x = largura // 2 - jogador_largura // 2
jogador_y = altura - jogador_altura - 10
jogador_velocidade = 5

# Variáveis das bolas
bola_raio = 20
bola_x = random.randint(bola_raio, largura - bola_raio)
bola_y = -bola_raio
bola_velocidade = 3

# Loop principal do jogo
jogo_ativo = True
while jogo_ativo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_ativo = False

    # Movimentação do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador_x > 0:
        jogador_x -= jogador_velocidade
    if teclas[pygame.K_RIGHT] and jogador_x < largura - jogador_largura:
        jogador_x += jogador_velocidade

    # Movimentação da bola
    bola_y += bola_velocidade
    if bola_y > altura + bola_raio:
        bola_x = random.randint(bola_raio, largura - bola_raio)
        bola_y = -bola_raio

    # Verificação de colisão
    if jogador_x < bola_x + bola_raio and jogador_x + jogador_largura > bola_x - bola_raio and jogador_y < bola_y + bola_raio and jogador_y + jogador_altura > bola_y - bola_raio:
        jogo_ativo = False

    #
