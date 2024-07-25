
import pygame
from FractalRenderer import FractalRenderer

# pygame setup
pygame.init()
screen = pygame.display.set_mode((320, 200))
pygame.display.set_caption("Apfelsee")
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

running = True
coly = 0

renderer = FractalRenderer()
renderer.setup()
renderer.drawClouds(screen)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEWHEEL:
            renderer.moveInOut(event.y)
            
    dx,dy = pygame.mouse.get_rel()
    renderer.rotate(dx, dy)

    # RENDER YOUR GAME HERE
    renderer.render(screen)        

    # flip() the display to put your work on screen
    pygame.display.flip()

    #print("fps: ",clock.get_fps())
    
    clock.tick(60)  # limits FPS to 60

pygame.quit()