from pico2d import*
import gfw
import game_state_gameplay
from background import Background

canvas_width=1200
canvas_height=600
smallfont = None
mfont = None
blink = True
blinktime = 0
Btime = 0

def enter():
    gfw.world.init(['bg'])

    global bg

    bg=Background('Start.jpg')
    gfw.world.add(gfw.layer.bg,bg)

    global music_bg
    music_bg = load_music('res/DDR.mp3')
    music_bg.repeat_play()


def update():
    global smallfont
    global mfont
    global blink
    global blinktime,Btime

    gfw.world.update()

    if blink == True:
        blinktime += gfw.delta_time
        if blinktime >= 0.5:
            blink = False
            Btime = 0

    elif blink == False:
        Btime += gfw.delta_time
        if Btime >= 0.5:
            blink = True
            blinktime = 0


def draw():
    global smallfont
    global mfont
    global blink
    global blinktime,Btime

    gfw.world.draw()

    if smallfont == None:
        smallfont = load_font('ENCR10B.TTF', 50)

    if blink:
        smallfont.draw(250, 150, "Press Space Key to Play.", (255, 255, 255))

    if mfont == None:
        mfont = load_font('ENCR10B.TTF', 20)
    mfont.draw(370, 25, "Use headphones for better experience.", (255, 255, 255))


def handle_event(evt):
    if evt.type==SDL_QUIT:
        gfw.quit()
        return

    elif evt.type==SDL_KEYDOWN:
        if evt.key==SDLK_SPACE:
            gfw.change(game_state_gameplay)




def exit():
    gfw.world.remove(bg)

if __name__ =='__main__':
    gfw.run_main()