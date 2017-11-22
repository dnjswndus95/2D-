import os
import random
import game_framework
import title_state
from Player import*
import enemy
from background import Background
from bullet import Player_Bullet

from pico2d import*

os.chdir('C:\\Temp\\lab01')

running = True;
name = "MainState"

player = None
enemy = None
background = None
player_bullet = None

def create_world():
    global player
    global background
    global player_bullet

    background = Background(800, 600)
    player = Player()
    player_bullet = Player_Bullet()

def destroy_world():
    global player, enemy, background, player_bullet

    del(player)
    del(enemy)
    del(background)
    del(player_bullet)


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
    global player_bullet

    events = get_events()

    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            player.handle_event(event)
            player_bullet.handle_event(event)

def update(frame_time):
    global player
    global player_bullet

    background.update(frame_time)
    player.update(frame_time)
    player_bullet.update(frame_time, player.x, player.y)

def draw(frame_time):

    clear_canvas()
    background.draw()
    Player.draw(player)
    player_bullet.draw()
    update_canvas()










