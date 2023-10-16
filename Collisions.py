import pygame

pygame.init()

screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Collisions in Pygame")
screenIcon = pygame.image.load("LaughEmoji.png")
pygame.display.set_icon(screenIcon)


pos = [90, 120, 90, 90]
rectPos = pygame.Rect(330, 300, 400, 100)

font = pygame.font.SysFont("Arial", 40, italic = True)

while True:
    screen.fill("lightyellow")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_w]:
        pos[1] -= 5
    if pressed[pygame.K_s]:
        pos[1] += 5
    if pressed[pygame.K_a]:
        pos[0] -= 5
    if pressed[pygame.K_d]:
        pos[0] += 5

    text = font.render("Do not touch the rectangle", True, "red")


    pygame.draw.rect(screen, "blue", pos)
    pygame.draw.rect(screen, "lightblue", rectPos)

    if rectPos.colliderect(pos):
        screen.blit(text, (300, 320))

    pygame.time.delay(10)
    pygame.display.update()
