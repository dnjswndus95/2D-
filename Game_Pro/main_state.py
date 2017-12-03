import os
import random
import game_framework
import title_state
from Player import*
import enemy
from background import Background
from Resource import*

from pico2d import*

#os.chdir('C:\\Temp\\lab01')

running = True;
name = "MainState"

player = None
enemy = None
background = None
player_bullet = None


def destroy_world():
    global player, enemy, background, player_bullet

    del(player)
    del(enemy)
    del(background)
    del(player_bullet)


def enter():
    global background, player, background, player_bullet

    background = Background(800, 600)
    player = Player()
    player_bullet = []


def exit():
    destroy_world()

def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    global player_bullet

    events = get_events()

    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            player.handle_event(event)

def update(frame_time):
    global player
    global player_bullet

    background.update(frame_time)
    player.update(frame_time)

    for new_attack in bullets:
        new_attack.update(frame_time)
        if new_attack.x > 800 or new_attack.x < 0:
            del (new_attack)

def draw(frame_time):

    clear_canvas()
    background.draw()
    player.draw()
    for attack in bullets:
        attack.draw()

    update_canvas()












