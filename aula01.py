from PPlay.window import *
from PPlay.sprite import *

janela = Window(1400, 1140)
janela.set_title("Exercício 2")
janela.set_background_color((255, 0, 255))

bolinhe = Sprite('boly.png')
bolinhe.x, bolinhe.y = 600, 300
barra_esq = Sprite('traço.png')
barra_esq.x = 0
barra_esq.y = 500

barra_dir = Sprite('traço.png')
barra_dir.x = janela.width - barra_dir.width
barra_dir.y = 500

velx = 1
vely = 2

while True:
    janela.set_background_color((255, 0, 255))

    bolinhe.x += velx
    bolinhe.y += vely

    if (bolinhe.x + bolinhe.width >= janela.width) or bolinhe.x <= 0:
        velx = -velx
    if (bolinhe.y + bolinhe.height >= janela.height) or bolinhe.y <= 0:
        vely = -vely

    bolinhe.draw()
    barra_dir.draw()  
    barra_esq.draw()  

    janela.update()