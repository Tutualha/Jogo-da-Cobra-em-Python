from tkinter import *
import random

JOGO_ALTURA = 700
JOGO_LARGURA = 700
VEL = 50
ESPACO_SIZE = 50
PART_CORPO = 3
COBRA_COLOR = "#191F40"
COMIDA_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Cobra:
    pass
class Comida:
    def __init__(self):
        x = random.randint(0, (JOGO_LARGURA/ESPACO_SIZE) - 1) * ESPACO_SIZE
        y = random.randint(0, (JOGO_ALTURA/ESPACO_SIZE) - 1) * ESPACO_SIZE
        
        self.coordinate = [x,y]
        tela.create_oval( x,y,x + ESPACO_SIZE, y + ESPACO_SIZE, fill=COMIDA_COLOR, tag="food")
        
        
        pass

def prox_fase():
    pass

def muda_dir(nova_dir):
    pass

def conf_colisao():
    pass

def game_over():
    pass


janela = Tk()
janela.title("Jogo da Cobra")
janela.resizable(False, False)

pontos = 0
direction = 'down'

label = Label(janela, text="Pontos: {}".format(pontos), font=('Verdana', 40))
label.pack()

tela = Canvas(janela, bg=BACKGROUND_COLOR, height=JOGO_ALTURA, width=JOGO_LARGURA)
tela.pack()

janela.update 
janela_largura = janela.winfo_width()
janela_altura = janela.winfo_height()
tela_altura = janela.winfo_screenwidth()
tela_largura = janela.winfo_screenwidth()
tela_altura = janela.winfo_screenheight()

x = int((tela_largura/2) - (janela_largura/2))
y = int((tela_altura/2) - (janela_altura/2))

janela.geometry(f"{janela_largura}x{janela_altura}+{x}+{y}")

cobra= Cobra()
comida= Comida()

janela.mainloop()