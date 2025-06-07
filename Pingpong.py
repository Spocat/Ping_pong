from pygame import *

img_back = ('Ping_background.jpg')

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping Pong')
background = transform.scale(image.load(img_back), (win_width, win_height))

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background,(0,0))

    time.delay(50)
    display.update()