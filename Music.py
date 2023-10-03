import pygame as pyg
from pygame import mixer

pyg.init()
screen = pyg.display.set_mode((900,700))
pyg.display.set_caption("Audio/Music in pygame")

mixer.init()
mixer.music.load("ClockRing.mp3")
mixer.music.play()

while True:
    key_press = pyg.key.get_pressed()
    if key_press[pyg.K_k]:
        mixer.music.pause()
    if key_press[pyg.K_l]:
        mixer.music.unpause()

    screen.fill("white")
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            quit()
    pyg.display.update()
