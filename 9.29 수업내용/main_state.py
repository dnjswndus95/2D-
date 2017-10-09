import os
import random
import game_framework
import title_state

from pico2d import *
os.chdir('C:\\Temp\\lab01')

running = True;

def handle_events():
    events = get_events()
    
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)

        elif event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

        elif event.type == SDL_MOUSEMOTION:
            boy.x, boy.y = event.x, 600 - event.y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            team[0].x, team[0].y = boy.x, boy.y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            team[1].x, team[1].y = boy.x, boy.y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
            team[2].x, team[2].y = boy.x, boy.y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_4:
            team[3].x, team[3].y = boy.x, boy.y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_5:
            team[4].x, team[4].y = boy.x, boy.y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_6:
            team[5].x, team[5].y = boy.x, boy.y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_7:
            team[6].x, team[6].y = boy.x, boy.y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_8:
            team[7].x, team[7].y = boy.x, boy.y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_9:
            team[8].x, team[8].y = boy.x, boy.y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_0:
            team[9].x, team[9].y = boy.x, boy.y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_F1:
            team[10].x, team[10].y = boy.x, boy.y

def enter():
    open_canvas()
    global boy, grass, team
    boy = Boy()
    boy1 = Boy()
    boy2 = Boy()
    boy3 = Boy()
    boy4 = Boy()
    boy5 = Boy()
    boy6 = Boy()
    boy7 = Boy()
    boy8 = Boy()
    boy9 = Boy()
    boy10 = Boy()
    boy11 = Boy()
    team = [boy1, boy2, boy3, boy4, boy5, boy6, boy7, boy8, boy9, boy10, boy11]
    grass = Grass()

def exit():
    clear_canvas()
    global boy, grass
    del(boy)
    del(grass)


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), random.randint(90, 500)
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame+1)%8
        self.x+=2

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def update():
    for boy in team:
        boy.update()

def draw():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
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