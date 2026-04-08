
#Importando a biblioteca
from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*

#Passando os parametros de tamanho da tela
tela = Window(800,800)

#Oque será escrito
tela.set_title("Exercício 3")

#Fazer com que fique mais tempo aberto
tela.delay(5000)

#Desenho da bola na tela
bola = Sprite("boly.png")

#Coordenadas da bolinha
altura_bola = (tela.height/2)-(bola.height/2)
largura_bola = (tela.width/2) - (bola.width/2)

bola.set_position(largura_bola ,altura_bola)

#Velocidades
velx = 400
vely = 500


while True:
    #Movimentação da bola
    bola.x += velx * tela.delta_time()
    bola.y += vely * tela.delta_time()

    #Impedir da bola sair e resolvendo o problema da patinação
    if (bola.x + bola.width >= tela.width) or bola.x <= 0:
        velx = -(velx)
    if (bola.y + bola.height >= tela.height) or bola.y <= 0:
        vely = -(vely)

    tela.set_background_color([255,255,255])
    bola.draw()
    tela.update()
