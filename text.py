import pygame

pygame.init()

screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Adding Text in Pygame")
screenIcon = pygame.image.load("LaughEmoji.png")
pygame.display.set_icon(screenIcon)

font = pygame.font.SysFont(" Times New Roman ", 90, bold = True, italic = True )

while True:
    screen.fill("lightyellow")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    text = font.render("I like Ice Cream", True, "red")
    screen.blit(text, (200,300))
    pygame.display.update()
