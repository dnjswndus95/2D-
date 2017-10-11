import os
import random
from pico2d import*
import game_framework
import title_state
import numbers

os.chdir('C:\\Temp\\lab01')

Index = 0


def exit():
    clear_canvas()
    global boy, grass
    del(boy)
    del(grass)

def enter():
    open_canvas()
    global boy, grass, team
    team = [Boy() for i in range(1000)]
    grass = Grass()

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:

    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[self.state](self)

    def handle_left_run(self):
        self.x -= 5
        self.run_frames += 1

        if self.x < 0:
            self.state = self.RIGHT_RUN
            self.x = 0

        if self.run_frames == 100:
            self.state = self.LEFT_STAND
            self.stand_frames = 0

    def handle_left_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.LEFT_RUN
            self.run_frames = 0

    def handle_right_run(self):
        self.x += 5
        self.run_frames = 0

        if self.x > 800:
            self.state = self.LEFT_RUN
            self.x = 800

        if self.run_frames == 100:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0

    def handle_right_stand(self):
        self.stand_frames += 1

        if self.stand_frames == 50:
            self.state = self.RIGHT_RUN
            self.run_frames = 0

    def __init__(self):
        self.x, self.y = random.randint(100, 700), random.randint(90, 500)
        self.frame = random.randint(0, 7)
        self.dir = 1
        self.state = self.RIGHT_RUN

        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[self.state](self)

    def draw(self):
        self.image.clip_draw(self.frame*100, self.state * 100, 100, 100, self.x, self.y)

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand
    }


def handle_events():
    events = get_events()
    global running
    global Index
    global Boy

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
            team[Index].x, team[Index].y = event.x, 600 - event.y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            Index += 1
            if event.type == SDL_MOUSEMOTION:
                team[Index].x, team[Index].y = event.x, 600 - event.y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            Index -= 1
            if event.type == SDL_MOUSEMOTION:
                team[Index].x, team[Index].y = event.x, 600 - event.y




def update():
    for boy in team:
        boy.update()

def draw():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()

    numbers.draw(Index + 1, 740, 540)
    update_canvas()
    delay(0.05)



def main():
    enter()

    running = True

    while running:
        handle_events()
        update()
        draw()

        delay(0.05)

    exit()

if __name__ == '__main__':
    main()


