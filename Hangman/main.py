from tkinter import EventType
import pygame 
import random 
import os 



pygame.init()
pygame.font.init()

btn_font = pygame.font.SysFont("arial", 20)
guess_font = pygame.font.SysFont("monospace", 24)
lost_font = pygame.font.SysFont('arial', 45)

FPS = 60

WIDTH = 1200
HEIGHT = 800

ALPHABETS = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

XVALUE = (100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 100, 200, 300, 400)
XLETTERVALUE = (95, 195, 295, 395, 495, 595, 695, 795, 895, 995, 1095, 1095, 995, 895, 795, 695, 595, 495, 395, 295, 195, 95, 95, 195, 295, 395)
YVALUE = (50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 250, 250, 250, 250)
YLETTERVALUE = (40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 240, 240, 240, 240)



WHITE = (255,255,255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)

RADIUS = 40

BUTTONHIT = pygame.USEREVENT + 1 

HANGMANNONE = pygame.image.load(os.path.join('Hangman', 'Assets', 'hangman0.png'))
HANGMANONE = pygame.image.load(os.path.join('Hangman', 'Assets', 'hangman1.png'))
HANGMANTWO = pygame.image.load(os.path.join('Hangman', 'Assets', 'hangman2.png'))
HANGMANTHREE = pygame.image.load(os.path.join('Hangman', 'Assets', 'hangman3.png'))
HANGMANFOUR = pygame.image.load(os.path.join('Hangman', 'Assets', 'hangman4.png'))
HANGMANFIVE = pygame.image.load(os.path.join('Hangman', 'Assets', 'hangman5.png'))
HANGMANSIX = pygame.image.load(os.path.join('Hangman', 'Assets', 'hangman6.png'))

hangmanpngs = (HANGMANONE, HANGMANTWO, HANGMANTHREE, HANGMANFOUR, HANGMANFIVE, HANGMANSIX)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hangman')

def buttons(): 
    p = 0 
    o = 0 
    pygame.event.get()
    while p < 26 and o < 26: 
        pygame.draw.circle(WIN, CYAN, (XVALUE[p], YVALUE[o]), RADIUS, 0)
        p += 1 
        o += 1 

def letters(): 
    a=0
    b=0
    c=0
    pygame.event.get()
    while a < 26 and a < 26 and c < 26:  
        WIN.blit(btn_font.render(ALPHABETS[a], False, BLACK), (XLETTERVALUE[a], YLETTERVALUE[c]))
        a += 1 
        b += 1
        c += 1 
    
    
def buttonhit(): 
   #Check python server - help PINEAPPLE 
    print("This is to stop indent error")

def draw():
    WIN.fill(WHITE)

    buttons()
    letters()

    pygame.display.update()

def main(): 


    clock = pygame.time.Clock()
    run = True 


    while run:
        clock.tick(FPS) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False 
                pygame.quit()
    
        draw()


if __name__ == "__main__":
    main()
