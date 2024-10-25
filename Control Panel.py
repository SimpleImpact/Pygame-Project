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
holder = 0
buttons = [(20, 20, 50, 50)]
font = pygame.font.SysFont("consolas", 60, True)
button = (20, 20, 50, 50)

# ================== || Grid Setings || ======================

def button(x, y, w, h):
    mouseX, mouseY = pygame.mouse.get_pos()
    if mouseX >= x and mouseX <= x + w and mouseY >= y and mouseY <= y+h:
        
        print('New Button')
        return("New Button")

#def addbutton():
#    x
#    y
#    w
#    h

while running:
    # ================== || Variables || =====================
    screen.fill("White")
    keys = pygame.key.get_pressed()
    text = pygame.font.Font.render(font, "+", True, (0, 0, 0))
    # =================== || Buttons || ======================
    l, m, r = pygame.mouse.get_pressed(3)
    if l and holder == 1:
        button(20, 20, 21, 33)
        holder = 0
    elif l == False:
        holder = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_e]:
            running = False
    # =================== || Renderer || =====================
    screen.blit(text, (20, 20))
    pygame.display.update()
    dt = clock.tick(240) / 1000
    # ========================================================

pygame.quit()
