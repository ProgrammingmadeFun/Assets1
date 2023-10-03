import pygame

pygame.init()

screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Drawing Shapes in Pygame")


while True:
    screen.fill("lightyellow")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.draw.rect(screen, "lightblue", (250,300,400,100), width = 0)
    pygame.draw.circle(screen, "black", (500,100), 40)
    pygame.draw.ellipse(screen, "yellow", (200, 150, 150, 75))
    pygame.draw.line(screen, (0,0,255), (20,100), (10,5), width = 18)
    # RGB values range from 0-255
    pygame.display.update()
