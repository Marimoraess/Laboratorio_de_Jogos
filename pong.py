
#Importando a biblioteca
from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*

#Passando os parametros de tamanho da tela
tela = Window(800,800)

#Oque será escrito
tela.set_title("Exercício 3")


#Desenho da bolinhe na tela
bolinhe = Sprite("boly.png")

#Coordenadas da bolinha
altura_bolinhe = (tela.height/2)-(bolinhe.height/2)
largura_bolinhe = (tela.width/2) - (bolinhe.width/2)

bolinhe.set_position(largura_bolinhe ,altura_bolinhe)

#Velocidades
velx = 400
vely = 500


while True:
    #Movimentação da bolinhe
    bolinhe.x += velx * tela.delta_time()
    bolinhe.y += vely * tela.delta_time()

    #Impedir da bolinhe sair e resolvendo o problema da patinação
    if (bolinhe.x + bolinhe.width >= tela.width) or bolinhe.x <= 0:
        velx = -(velx)
    if (bolinhe.y + bolinhe.height >= tela.height) or bolinhe.y <= 0:
        vely = -(vely)

    tela.set_background_color([255,255,255])
    bolinhe.draw()
    tela.update()
