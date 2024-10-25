#py -m pip install
import pygame

# pygame setup
pygame.init()
pygame.font.init()
screenx = 1080
screeny = 720
screen = pygame.display.set_mode((screenx, screeny))
clock = pygame.time.Clock()
running = True
dt = 0

button = (20, 20, 50, 50)

while running:
    screen.fill("White")
    keys = pygame.key.get_pressed()
    #pygame.draw.rect(screen, "Black", button)
    font = pygame.font.SysFont("Algerian", 60, False)
    text = pygame.font.Font.render(font, "+", True, (0, 0, 0))
    screen.blit(text, (20, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_e]:
            running = False
          
    # Put all code here
    pygame.display.update()
    dt = clock.tick(240) / 1000

pygame.quit()
