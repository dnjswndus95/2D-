from pico2d import *
import Game_framework
import main_state
import Characters

name = "TitleState"
image = None

def enter():
    global image
    image = load_image('MainScreen.jpg')

def exit():
    global image
    del(image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                Game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                Game_framework.change_state(Characters)

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def update():
    pass