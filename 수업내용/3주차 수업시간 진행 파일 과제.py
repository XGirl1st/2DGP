from pico2d import*
Pico2d is prepared.

os.getcwd()
'C:\\Users\\이화수\\AppData\\Local\\Programs\\Python\\Python38'

os.chdir('c:\\2D\\lab01')
os.listdir()
['character.png', 'grass.png']
open_canvas()
hide_lattice()
show_lattice()
close_canvas()

open_canvas()
image=load_image('character.png')
image.draw_now(300,200)
image.draw_now(500,400)
image.draw_now(700,600)
close_canvas()
open_canvas(800,600)

		
image=load_image('character.png')
for x in range(0,9):
    for y in range(0,7):
        image.draw_now(x*100,y*100)

		

clear_canvas_now()


character=load_image('character.png')

grass=load_image('grass.png')
grass.draw_now(400,30)
character.draw_now(400,85)

delay(5)

close_canvas()

open_canvas()

os.getcwd()
'C:\\Users\\이화수\\AppData\\Local\\Programs\\Python\\Python38'
os.chdir('c:\\2D\\lab01')

os.listdir()
['character.png', 'grass.png']

grass=load_image('grass.png')
character=load_image('character.png')

x=0
while(x<800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,85)
    x+=2
    delay(0.01)

	
close_canvas()

open_canvas()
character=load_image('character.png')
character.draw(100,100)
character.draw_now(100,100)
clear_canvas()

clear_canvas_now()

character.draw(100,100)
character.draw(200,200)

update_canvas()
clear_canvas()
update_canvas()

x=0
while(x<800):
    clear_canvas()
    grass.draw(400,30)
    character.draw(x,85)
    x+=2
    update_canvas()
    delay(0.01)
    get_events()

	


close_canvas()
open_canvas()
grass=load_image('grass.png')
ch=load_image('character.png')
 
x=0
while(x<800):
    clear_canvas()
    grass.draw(400,300)
    ch.draw(x,85)
    x+=2
    update_canvas()
    delay(0.01)
    get_events()

	

x=0
clear_canvas()
update_canvas()

grass.draw_now(400,30)
clear_canvas_now()
grass.draw(400,30)
update_canvas()
clear_canvas()

update_canvas()
 
x=0
while(x<800):
    clear_canvas()
    grass.draw(400,30)
    ch.draw(x,85)
    x+=2
    update_canvas()
    delay(0.01)
    get_events()

	


close_canvas()

os.getcwd()
'c:\\2D\\lab01'
os.chdir('c:\\2D\\lab01')

os.listdir()
['character.png', 'grass.png', 'run_animation.png']


open_canvas()
g=load_image('grass.png')
ch=load_image('run_animation.png')

x=0
frame=0
while(x<800):
    clear_canvas()
    g.draw(400,30)
    ch.clip_draw(frame*100,0,100,100,x,85)
    update_canvas()
    frame=(frame+1)%8
    x+=5
    delay(0.05)
    get_events()

	

close_canvas()

