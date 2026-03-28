from PPlay.window import *

from PPlay.sprite import *


janela = Window(2000, 1500)
janela.set_title("Exercício 2")
janela.set_background_color((255, 0, 255))

bolinhe = Sprite('boly.png')
bolinhe.x, bolinhe.y = 1000, 500

while True:
    bolinhe.x, bolinhe.y = (janela.width/2)- (bolinhe.width/2), (janela.height/2) - (bolinhe.height/2)
    bolinhe.draw()
    janela.update()