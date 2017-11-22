import os
import random
import game_framework
import title_state
from Player import Player
import enemy
from background import Background

from pico2d import*

os.chdir('C:\\Temp\\lab01')

running = True;
name = "MainState"

player = None
enemy = None
scrolling_background = None
background = None

def create_world():
    global player
    global scrolling_background

    scrolling_background = Background(800, 600)
    player = Player()

def destroy_world():
    global player, enemy

    del(player)
    del(enemy)


def enter():
    global background

    create_world()

def exit():
    destroy_world()

def pause():
    pass

def resume():
    pass

def handle_events(frame_time):

    events = get_events()

    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            player.handle_event(event)

def update(frame_time):
    global player

    scrolling_background.update(frame_time)
    player.update(frame_time)

def draw(frame_time):
    clear_canvas()
    scrolling_background.draw()
    Player.draw(player)
    update_canvas()










