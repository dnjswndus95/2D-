from pico2d import *
import Game_framework
import Title_state

name = "StartState"
image = None
logo_time = 0.0

def enter():
    global image
    open_canvas()
    image = load_image('kpu_credit.png')

def exit():
    global image
    del(image)
    close_canvas()

def update():
    global logo_time

    if(logo_time > 1.0):
        logo_time = 0
        Game_framework.push_state(Title_state)

    delay(0.01)
    logo_time += 0.01

def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
    pass

def pause():
    pass

def resume():
    pass