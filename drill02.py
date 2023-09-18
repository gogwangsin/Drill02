from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
x = 0
y = 90
def drawRec():
    global x
    global y
    if x >= 790 and y < 550:
        y = y + 2
    elif x < 790 :
        x = x + 2

    if y >= 550:
        x = x - 4
    elif y > 90 and x < 80:
        y = y -4

    


        
    
while( x < 800 ):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    drawRec()
    delay(0.01)

close_canvas()
