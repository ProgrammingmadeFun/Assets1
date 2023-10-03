import pygame

pygame.init()

screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Keyboard input + movement")
screenIcon = pygame.image.load("LaughEmoji.png")
pygame.display.set_icon(screenIcon)

img = pygame.image.load("LaughEmoji.png")
img = pygame.transform.scale(img, (140, 150))

x = 400
y = 300


def img_display(x,y):
    screen.blit(img, (x,y))


while True:
    screen.fill("lightyellow")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    key_press = pygame.key.get_pressed()

    if key_press[pygame.K_w]:
        y -= 5
    if key_press[pygame.K_s]:
        y += 5
    if key_press[pygame.K_a]:
        x -= 5
    if key_press[pygame.K_d]:
        x += 5

    img_display(x,y)
    pygame.time.delay(10)

    pygame.display.update()
