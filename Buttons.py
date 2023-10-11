import pygame as pyg
from pygame import mixer

pyg.init()
screen = pyg.display.set_mode((900,700))
pyg.display.set_caption("Buttons In Pygame")

mixer.init()
mixer.music.load("ClockRing.mp3")
mixer.music.play()

font = pyg.font.SysFont("Open Sauce", 60)
sizePos = pyg.Rect(150,320,250,130)
sizePos1 = pyg.Rect(600, 320, 250, 130)


while True:
    screen.fill("white")
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            quit()
    if event.type == pyg.MOUSEBUTTONDOWN:
        if sizePos.collidepoint(event.pos):
            mixer.music.pause()
        if sizePos1.collidepoint(event.pos):
            mixer.music.unpause()


    pyg.draw.rect(screen, (0,0,0), sizePos)
    pyg.draw.rect(screen, "red", sizePos1)

    text = font.render("Pause", True, "gray")
    text2 = font.render("Unpause", True, "white")

    screen.blit(text, (215, 370))
    screen.blit(text2, (640, 370))
    pyg.display.update()
