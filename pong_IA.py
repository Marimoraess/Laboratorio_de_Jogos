# Importando bibliotecas
from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *

# Criando a tela
tela = Window(1200, 600)
tela.set_title("Exercício 4 - Pong")

# Controle
controle = tela.get_keyboard()

# Pads
pad1 = Sprite("traço.png")
pad1.x = pad1.width * 2
pad1.y = tela.height/2 - pad1.height/2

pad2 = Sprite("traço.png")
pad2.x = tela.width - (pad2.width * 3)
pad2.y = tela.height/2 - pad2.height/2

# Bola
bola = Sprite("boly.png")
bola.x = tela.width/2 - bola.width/2
bola.y = tela.height/2 - bola.height/2

# Velocidades
velx = -300
vely = 400
velp = 320
velIA = 380

# Pontuação
esquerda = 0
direita = 0

# Loop principal
while True:

    # Movimento da bola
    bola.x += velx * tela.delta_time()
    bola.y += vely * tela.delta_time()

    # IA simples (segue a bola)
    if bola.y > pad2.y:
        pad2.y += velIA * tela.delta_time()
    elif bola.y < pad2.y:
        pad2.y -= velIA * tela.delta_time()

    # Controles jogador 1
    if controle.key_pressed("w"):
        pad1.y -= velp * tela.delta_time()
    if controle.key_pressed("s"):
        pad1.y += velp * tela.delta_time()

    # Controles jogador 2 (opcional)
    if controle.key_pressed("up"):
        pad2.y -= velp * tela.delta_time()
    if controle.key_pressed("down"):
        pad2.y += velp * tela.delta_time()

    # Limite dos pads
    if pad1.y < 0:
        pad1.y = 0
    if pad1.y + pad1.height > tela.height:
        pad1.y = tela.height - pad1.height

    if pad2.y < 0:
        pad2.y = 0
    if pad2.y + pad2.height > tela.height:
        pad2.y = tela.height - pad2.height

    # Colisão com topo/baixo
    if bola.y <= 0:
        bola.y = 0
        vely *= -1

    if bola.y + bola.height >= tela.height:
        bola.y = tela.height - bola.height
        vely *= -1

    # Pontuação
    if bola.x + bola.width >= tela.width:
        esquerda += 1
        velx *= -1
        bola.x = tela.width/2 - bola.width/2
        bola.y = tela.height/2 - bola.height/2

    if bola.x <= 0:
        direita += 1
        velx *= -1
        bola.x = tela.width/2 - bola.width/2
        bola.y = tela.height/2 - bola.height/2

    # Colisão com pads
    if pad1.collided(bola):
        velx *= -1
        bola.x = pad1.x + pad1.width

    if pad2.collided(bola):
        velx *= -1
        bola.x = pad2.x - bola.width

    # Desenho
    tela.set_background_color((255, 255, 255))

    tela.draw_text(
        "{} x {}".format(esquerda, direita),
        tela.width/2 - 50,
        30,
        30,
        (0, 0, 0),
        "Arial",
        True,
        False
    )

    pad1.draw()
    pad2.draw()
    bola.draw()

    tela.update()