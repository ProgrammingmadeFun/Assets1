import pygame

pygame.init()

screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Setting our Pygame Screen")
screenIcon = pygame.image.load("LaughEmoji.png")
pygame.display.set_icon(screenIcon)

while True:
    screen.fill("lightyellow")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
