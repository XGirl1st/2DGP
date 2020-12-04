from pico2d import*
import gfw
import game_state_gameplay
from background import Background

canvas_width=1200
canvas_height=600
smallfont = None

def enter():
    gfw.world.init(['bg'])

    global bg

    bg=Background('Start.jpg')
    gfw.world.add(gfw.layer.bg,bg)



def update():
    gfw.world.update()

def draw():
    global smallfont

    gfw.world.draw()
    if smallfont == None:
        smallfont = load_font('ENCR10B.TTF', 20)

    smallfont.draw(400,100, "Press Button 알아서 수정해", (255,255,255))

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