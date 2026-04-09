# Importando a biblioteca
from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.collision import *

# Janela
janela = Window(1200, 600)
janela.set_title("Exercício 4")

controle = janela.get_keyboard()

# Pads
pad1 = Sprite("traço.png")
pad1.x = 0
pad1.y = janela.height/2 - pad1.height/2

pad2 = Sprite("traço.png")
pad2.x = janela.width - pad2.width
pad2.y = janela.height/2 - pad2.height/2

# Bola
boly = Sprite("boly.png")
boly.set_position(janela.width/2 - boly.width/2,
                  janela.height/2 - boly.height/2)

# Velocidades
velx = 0
vely = 0
velp = 320
velIA = 380

# Pontuação
esquerda = 0
direita = 0

# Controle de pausa (quando faz ponto)
Colidiu = True

while True:

    # Só move a bola se NÃO estiver pausado
    boly.x += velx * janela.delta_time()
    boly.y += vely * janela.delta_time()

    # IA simples
    if (boly.x >= janela.width/2 and boly.y >= janela.height/2 and vely > 0):
        pad2.y += velIA * janela.delta_time()
    if (boly.x >= janela.width/2 and boly.y <= janela.height/2 and vely < 0):
        pad2.y -= velIA * janela.delta_time()

    # Controles
    if (controle.key_pressed("w")):
        pad1.y -= velp * janela.delta_time()
    elif (controle.key_pressed("s")):
        pad1.y += velp * janela.delta_time()

    if (controle.key_pressed("up")):
        pad2.y -= velp * janela.delta_time()
    elif (controle.key_pressed("down")):
        pad2.y += velp * janela.delta_time()

    # Limites dos pads
    if (pad1.y <= 0):
        pad1.y = 0
    if (pad1.y + pad1.height >= janela.height):
        pad1.y = janela.height - pad1.height

    if (pad2.y <= 0):
        pad2.y = 0
    if (pad2.y + pad2.height >= janela.height):
        pad2.y = janela.height - pad2.height

    # Colisão com topo/baixo
    if (boly.y <= 0):
        boly.y = 0
        vely *= -1
    if (boly.y + boly.height >= janela.height):
        boly.y = janela.height - boly.height
        vely *= -1

    # PONTUAÇÃO
    if (boly.x + boly.width >= janela.width):
        esquerda += 1

        boly.set_position(janela.width/2 - boly.width/2,
                          janela.height/2 - boly.height/2)

        velx = 0
        vely = 0
        Colidiu = True

    if (boly.x <= 0):
        direita += 1

        boly.set_position(janela.width/2 - boly.width/2,
                          janela.height/2 - boly.height/2)

        velx = 0
        vely = 0
        Colidiu = True

    
    if Colidiu and controle.key_pressed("space"):
        velx = -300   # pode trocar depois
        vely = 200
        Colidiu = False

    # Colisão com pads
    if (pad1.collided(boly)):
        velx *= -1
        boly.x = pad1.x + pad1.width

    if (pad2.collided(boly)):
        velx *= -1
        boly.x = pad2.x - boly.width

    # Desenho
    janela.set_background_color([0, 255, 255])

    janela.draw_text(f"{esquerda}  x  {direita}",
                     janela.width/2 - 60, 30,
                     30, (0, 0, 0), "Arial", True, False)

    pad1.draw()
    pad2.draw()
    boly.draw()

    janela.update()