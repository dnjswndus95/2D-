from pico2d import*
import random
import os
from Resource import*


bullets = []

#os.chdir('C:\\Temp\\lab01')

class Player:
    character_image = None
    shoot_image = None
    shooting_sound = None

    PIXEL_PER_KMETER = (10.0/0.5)
    RUN_SPEED_KMPH = 36000.0
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 11

    MOVE_UP = False
    MOVE_DOWN = False
    MOVE_RIGHT = False
    MOVE_LEFT = False
    STAND = False

    def __init__(self):
        self.x, self.y = 100, 300
        self.dir = 1  # 0 : stand, 1 : right, 2 : left, 3 : up, 4 : down
        self.live = True
        self.frame = 0
        self.total_frame = 0.0
        self.state = self.STAND
        self.character_image = load_image('character_right.png')


    def you_dead(self):
        self.live = False
        pass

    def move(self):
        if self.MOVE_RIGHT:
            self.x += self.distance
        if self.MOVE_LEFT:
            self.x -= self.distance
        if self.MOVE_UP:
            self.y += self.distance
        if self.MOVE_DOWN:
            self.y -= self.distance

    def update(self, frame_time):
        self.distance = self.RUN_SPEED_PPS * frame_time
        self.move()
        self.frame += int(self.total_frame) % 8
        self.total_frame += Player.FRAMES_PER_ACTION * Player.ACTION_PER_TIME * frame_time

        self.x = clamp(0, self.x, 800)
        self.y = clamp(0, self.y, 600)


    def draw(self):
        self.character_image.clip_draw((self.frame%11) * 40, 0, 40, 40, self.x, self.y)
        # clip_draw_to_origin(self, left, botton, width, height, x, y, w, h)

    def handle_event(self, event):
        if(event.type, event.key) ==(SDL_KEYDOWN, SDLK_LEFT):
            self.MOVE_LEFT = True
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.MOVE_RIGHT = True
        if(event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            self.MOVE_LEFT = False
        if(event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            self.MOVE_RIGHT = False
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            self.MOVE_UP = True
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            self.MOVE_DOWN = True
        if (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            self.MOVE_UP = False
        if (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
           self.MOVE_DOWN = False
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            new_attack = Bullet()
            new_attack.x, new_attack.y = self.x + 10, self.y
            new_attack.frame = 1
            bullets.append(new_attack)


class Bullet:
    image = None
    shooting_sound = None

    PIXEL_PER_KMETER = (10.0 / 0.5)
    RUN_SPEED_KMPH = 180000.0
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    def __init__(self):
        self.dir = 0
        self.frame = 0
        self.x, self.y = 0, 0

        if Bullet.image is None:
            Bullet.image = load_image('character_bullet.png')

        self.shooting_sound = load_music('shooting.wav')
        self.shooting_sound.set_volume(60)

    def update(self, frame_time):
        self.distance = self.RUN_SPEED_PPS * frame_time
        self.move()

    def move(self):
        self.x += self.distance

    def draw(self):
        self.image.clip_draw((self.frame % 9) * 24, 0, 24, 18, self.x, self.y)
        #self.character_image.clip_draw((self.frame%11) * 40, 0, 40, 40, self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 10, self.x + 20, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())









