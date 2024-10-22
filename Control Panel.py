#py -m pip install
import pygame
import config

# pygame setup
pygame.init()
pygame.font.init()
screenx = 1080
screeny = 720
screen = pygame.display.set_mode((screenx, screeny))
clock = pygame.time.Clock()
running = True
dt = 0
holder = 0

button = (20, 20, 50, 50)

def button(x, y, w, h):
    mouseX, mouseY = pygame.mouse.get_pos()
    if mouseX >= x and mouseX <= x + w and mouseY >= y and mouseY <= y+h:
        
        print('New Button')
        return("New Button")

while running:
    screen.fill("White")
    keys = pygame.key.get_pressed()
    #pygame.draw.rect(screen, "Black", button)
    font = pygame.font.SysFont("Algerian", 60, False)
    text = pygame.font.Font.render(font, "+", True, (0, 0, 0))
    screen.blit(text, (20, 20))
    l, m, r = pygame.mouse.get_pressed(3)
    print(pygame.mouse.get_pressed(3))
    if l:
        button(20, 20, 21, 33)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_e]:
            running = False
          
    # Put all code here
    pygame.display.update()
    dt = clock.tick(240) / 1000

pygame.quit()
