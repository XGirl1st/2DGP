from pico2d import*
import gfw
import arrow_generator
from background import Background
import time
import random
canvas_width=1200
canvas_height=600



def enter():
    gfw.world.init(['bg','note'])

    global bg
    global leftTime, upTime, downTime, rightTime, makenote
    makenote = time.time()
    global LeftCollide, RightCollide, UpCollide, DownCollide

    leftTime, upTime, downTime, rightTime = 0, 0, 0, 0
    LeftCollide = False
    RightCollide = False
    UpCollide = False
    DownCollide = False

    bg=Background('saber.jpg')
    gfw.world.add(gfw.layer.bg,bg)

    global black_left, black_up, black_down, black_right
    global slash_left, slash_down, slash_up, slash_right

    black_left = gfw.image.load('res/black_left.png')
    black_up = gfw.image.load('res/black_up.png')
    black_down = gfw.image.load('res/black_down.png')
    black_right = gfw.image.load('res/black_right.png')

    slash_left = gfw.image.load('res/slash_left.png')
    slash_up = gfw.image.load('res/slash_up.png')
    slash_down = gfw.image.load('res/slash_down.png')
    slash_right = gfw.image.load('res/slash_right.png')


def update():
    global LeftCollide, RightCollide, UpCollide, DownCollide
    global makenote


    if time.time() - makenote > 1:
        noteType = random.randint(0,3)
        arrow_generator.create_arrow(noteType, 300 + 200 * noteType, 100)
        makenote = time.time()



    if time.time() - leftTime > 1:
        LeftCollide = False
    if time.time() - upTime > 1:
        UpCollide = False
    if time.time() - downTime > 1:
        DownCollide = False
    if time.time() - rightTime > 1:
        RightCollide = False

    gfw.world.update()

def draw():
    gfw.world.draw()
    if LeftCollide:
        slash_left.draw(300,500,100,100)
    else:
        black_left.draw(300,500,100,100)

    if UpCollide:
        slash_up.draw(500,500,100,100)
    else:
        black_up.draw(500, 500, 100, 100)

    if DownCollide:
        slash_down.draw(700,500,100,100)
    else:
        black_down.draw(700, 500, 100, 100)

    if RightCollide:
        slash_right.draw(900, 500, 100, 100)
    else:
        black_right.draw(900, 500, 100, 100)



def handle_event(evt):
    global leftTime, upTime, downTime, rightTime
    global LeftCollide

    if evt.type==SDL_QUIT:
        gfw.quit()
    elif evt.type==SDL_KEYDOWN:
        if evt.key==SDLK_ESCAPE:
            gfw.pop()
        if evt.key==SDLK_a:
            arrow_generator.create_arrow(0, 300, 100)

        if evt.key == SDLK_LEFT:
            for game_object in gfw.world.objects_at(gfw.layer.note):
                if gfw.world.collide(game_object, 0):
                    leftTime = time.time()
                    gfw.world.remove(game_object)

        if evt.key == SDLK_UP:
            for game_object in gfw.world.objects_at(gfw.layer.note):
                if gfw.world.collide(game_object, 1):
                    upTime = time.time()
                    gfw.world.remove(game_object)

        if evt.key == SDLK_DOWN:
            for game_object in gfw.world.objects_at(gfw.layer.note):
                if gfw.world.collide(game_object, 2):
                    downTime = time.time()
                    gfw.world.remove(game_object)

        if evt.key == SDLK_RIGHT:
            for game_object in gfw.world.objects_at(gfw.layer.note):
                if gfw.world.collide(game_object, 3):
                    rightTime = time.time()
                    gfw.world.remove(game_object)





    elif evt.type == SDLK_UP:
        arrow_generator.create_arrow(0, 100, 100)








def exit():
    gfw.world.remove(bg)

if __name__ =='__main__':
    gfw.run_main()