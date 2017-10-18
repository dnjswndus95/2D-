import os
import random
import Game_framework
import Title_state

from pico2d import *

os.chdir('C:\\Temp\\lab01')

running = True;


def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            Game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            Game_framework.change_state(Title_state)


def exit():
    clear_canvas()
    global boy, grass
    del (boy)
    del (grass)

class Background:
    def __init__(self):
        self.image=load_image('게임바탕.png')

    def draw(self):
        self.image.draw(400,300)

class Character:
    image = None

    LEFT_RUN, RIGHT_RUN = 0, 1

    def __init__(self):
        self.x, self.y = 50, 400
        self.frame = 0
        self.move_frame = 0
        self.image = load_image('character.png')

        if Character.image == None:
            Character.image = load_image('animation_sheet.png')

    def update(self):

        global move

        self.move_frame = 0
        self.frame = (self.frame + 1) % 8

        if self.state == self.RIGHT_RUN:
            self.frame = (self.frame + 1) % 8
            self.x += (self.dir * 5)
        self.image.clip_draw()

        if self.x > 800:
            self.dir = -1
            self.x = 800
            self.state = self.LEFT_RUN

        if self.state == self.LEFT_RUN:
            self.frame = (self.frame + 1) % 8
            self.x += (self.dir * 5)
        self.image.clip_draw()

        if self.x < 0:
            self.dir = 1
            self.x = 0
            self.state = self.RIGHT_RUN

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

def update():
    global move

def enter():
    global character, background
    open_canvas()
    background = Background()
    character = Character()

def exit():
    global character, background
    del(character)
    del(background)
    close_canvas()

def draw():
    clear_canvas()
    background.draw()
    character.draw()
    update_canvas()
    delay(0.05)


def main():
    enter()
    while running:
        handle_events()
        update()
        draw()
    exit()


if __name__ == '__main__':
    main()