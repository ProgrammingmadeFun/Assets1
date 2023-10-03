import pygame

pygame.init()

screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Setting our Pygame Screen")


image = pygame.image.load("Prisoner.png")
image = pygame.transform.scale(image, (400, 300))

def background():
    screen.blit(image,(250,400))

while True:
    screen.fill("lightyellow")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #screen.blit(image,(250,400))
    background()
    pygame.display.update()
