from tkinter import *
import random

JOGO_LARGURA = 1000
JOGO_ALTURA = 800
VEL = 70
ESPACO_SIZE = 30
PART_CORPO = 3
COBRA_COLOR = "#128912"
COMIDA_COLOR = "#FF0000"
BACKGROUND_COLOR = "#F0F0F0"

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
    
    if x == comida.coordinatess[0] and y == comida.coordinatess[1]:
        global pontos
        pontos +=1
        label.config(text="Pontos: {}".format(pontos))
        canvas.delete("comida")
        comida = Comida()
    
    else:    
        del cobra.coordinatess[-1]
        canvas.delete(cobra.square[-1])
        del cobra.square[-1]
    
    if conf_colisao(cobra):
        game_over()
    else:
        janela.after(VEL, prox_fase, cobra, comida)
        

def muda_dir(nova_dir):
    global dir
    
    if nova_dir == "left":
        if dir != 'right':
            dir = nova_dir
    elif nova_dir == "right":
        if dir != 'left':
            dir = nova_dir
    elif nova_dir == "up":
        if dir != 'down':
            dir = nova_dir
    elif nova_dir == "down":
        if dir != 'up':
            dir = nova_dir
      
            

def conf_colisao(cobra):
    x, y = cobra.coordinatess[0]
    
    if x < 0 or x >= JOGO_LARGURA:
        return True
    elif y < 0 or y >= JOGO_ALTURA:
        print("LOL")
        return True
    
    for PART_CORPO in cobra.coordinatess[1:]:
        if x == PART_CORPO[0] and y == PART_CORPO[1]:
            print("LOL")
            return True

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('Verdana', 70), text="SSSSssSSs", fill="red", tag="gameover")


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

janela.bind('<Left>', lambda event: muda_dir('left'))
janela.bind('<Right>', lambda event: muda_dir('right'))
janela.bind('<Up>', lambda event: muda_dir('up'))
janela.bind('<Down>', lambda event: muda_dir('down'))

cobra= Cobra()
comida= Comida()
prox_fase(cobra, comida)

janela.mainloop()
