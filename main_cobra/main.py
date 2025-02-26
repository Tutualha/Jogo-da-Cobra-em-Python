from tkinter import *
import random

JOGO_LARGURA = 800
JOGO_ALTURA = 800 # espaço_size / altura e largura = 16
VEL = 50
ESPACO_SIZE = 50
PART_CORPO = 3
COBRA_COLOR = "#128912"
COMIDA_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Cobra:
    def __init__(self):
        self.parte_corpo = PART_CORPO
        self.coordinatess = []
        self.square = []
        
        for i in range(0, PART_CORPO):
            self.coordinatess.append([0, 0])
            
        for x, y in self.coordinatess:
            retangulo = canvas.create_rectangle(x, y, x + ESPACO_SIZE, y + ESPACO_SIZE, fill=COBRA_COLOR, tag="cobra")
            self.square.append(retangulo)
        
class Comida:
    def __init__(self):
        x = random.randint(0, (JOGO_LARGURA // ESPACO_SIZE)-1) * ESPACO_SIZE
        y = random.randint(0, (JOGO_ALTURA // ESPACO_SIZE) - 1) * ESPACO_SIZE
        
        self.coordinatess = [x,y]
        canvas.create_oval(x, y, x + ESPACO_SIZE, y + ESPACO_SIZE, fill=COMIDA_COLOR, tag="comida")
       

def prox_fase(cobra, comida):
    
    x, y = cobra.coordinatess[0]
    
    if dir == "up":
        y -= ESPACO_SIZE
    
    elif dir == "down":
        y += ESPACO_SIZE
        
    elif dir == "left":
        x -= ESPACO_SIZE
    
    elif dir == "right":
        x += ESPACO_SIZE
        
    cobra.coordinatess.insert(0, (x, y))
    retangulo = canvas.create_rectangle(x, y, x + ESPACO_SIZE, y + ESPACO_SIZE, fill= COBRA_COLOR)
    
    cobra.square.insert(0, retangulo) 
    janela.after(VEL, prox_fase, cobra, comida)
        

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
dir = 'down'

label = Label(janela, text="Pontos: {}".format(pontos), font=('Verdana', 40))
label.pack()

canvas = Canvas(janela, bg=BACKGROUND_COLOR, height=JOGO_ALTURA, width=JOGO_LARGURA)
canvas.pack()

janela.update()

janela_largura = janela.winfo_width()
janela_altura = janela.winfo_height()
screen_altura = janela.winfo_screenwidth()
screen_largura = janela.winfo_screenwidth()
screen_altura = janela.winfo_screenheight()

x = int((screen_largura/2) - (janela_largura/2))
y = int((screen_altura/2) - (janela_altura/2))

janela.geometry(f"{janela_largura}x{janela_altura}+{x}+{y}")

cobra= Cobra()
comida= Comida()
prox_fase(cobra, comida)

janela.mainloop()
