from pico2d import*
import gfw
import game_state
import game_state_gameplay
from background import Background

canvas_width=1200
canvas_height=600
smallfont = None
bfont = None
mfont = None
nfont = None
blink = True
blinktime = 0
Btime = 0

def enter():
    gfw.world.init(['bg'])

    global bg

    bg=Background('end.jpg')
    gfw.world.add(gfw.layer.bg,bg)



def update():
    global mfont
    global blink
    global blinktime, Btime

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
    global bfont
    global mfont
    global nfont
    global blink
    global blinktime, Btime

    gfw.world.draw()
    if smallfont == None:
       smallfont = load_font('ENCR10B.TTF', 300)


    game_state_gameplay.Rank()
    smallfont.draw(500,450, "%s" %game_state_gameplay.rank, (255,255,255))

    if bfont == None:
        bfont = load_font('ENCR10B.TTF', 100)

    bfont.draw(300, 220, "Miss:   %d" %game_state_gameplay.miss, (255, 255, 255))

    if nfont == None:
        nfont = load_font('ENCR10B.TTF', 70)
    nfont.draw(300, 300, "Max Combo:  %d" % game_state_gameplay.MaxC, (255, 255, 255))

    if mfont == None:
        mfont = load_font('ENCR10B.TTF', 20)

    if blink:
        mfont.draw(350, 30, "Press Enter Key to return to Main.", (255, 255, 255))



def handle_event(evt):
    if evt.type==SDL_QUIT:
        gfw.quit()
        return

    elif evt.type==SDL_KEYDOWN:
        if evt.key==SDLK_RETURN:
            gfw.change(game_state)
            game_state_gameplay.missReset()




def exit():
    gfw.world.remove(bg)

if __name__ =='__main__':
    gfw.run_main()