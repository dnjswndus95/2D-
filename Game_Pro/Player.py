from pico2d import*
import random
import main_state
import os
from Resource import*

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
    FRAMES_PER_ACTION = 8

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
        self.life = 2
        self.total_frame = 0.0
        self.state = self.STAND
        self.character_image = load_image('Ayin.png')
        self.shooting_sound = load_wav("Attack.wav")
        self.shooting_sound.set_volume(60)
        self.special_attack_sound = load_wav("AyinSpecialAttack.wav")
        self.special_attack_sound.set_volume(80)
        self.eat_sound = load_wav("PowerUp.wav")
        self.eat_sound.set_volume(80)
        self.special_attack_count = 2

    def eat(self):
        self.eat_sound.play()

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
        self.frame = int(self.total_frame) % 3
        self.total_frame += Player.FRAMES_PER_ACTION * Player.ACTION_PER_TIME * frame_time

        self.x = clamp(0, self.x, 800)
        self.y = clamp(0, self.y, 600)


    def draw(self):
        self.character_image.clip_draw(self.frame * 60, 0, 60, 68, self.x, self.y)
        # clip_draw_to_origin(self, left, bottom, width, height, x, y, w, h)

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
            self.shooting_sound.play()
            if main_state.Score >= 300:
                new_attack = Moon()
            else:
                new_attack = Arrow()
            new_attack.x, new_attack.y = self.x + 10, self.y
            new_attack.frame = 1
            new_attack.dir = 1
            if new_attack == Arrow():
                main_state.arrows.append(new_attack)
            else:
                main_state.moons.append(new_attack)

        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_d):
            if self.special_attack_count <= 0:
                pass
            else:
                self.special_attack_sound.play()
                self.special_attack_count -= 1
                new_attack = Special_attack()
                print(Special_attack)
                new_attack.x, new_attack.y = self.x +50, self.y
                main_state.special_attack.append(new_attack)

    def get_bb(self):
        return self.x - 30, self.y -31 , self.x + 30, self.y + 31




class Arrow:
    PIXEL_PER_KMETER = (10.0 / 0.5)
    RUN_SPEED_KMPH = 180000.0
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    image = None

    def __init__(self):
        self.dir = 0
        self.frame = 0
        self.x, self.y = 0, 0
        if Arrow.image is None: # 30 x 60 size
            Arrow.image = load_image("AyinMissile_Arrow.png")
        # 미사일 충돌처리 size 70x60 바운딩박스로 ㄱㄱ

    def update(self, frame_time):
        self.distance = self.RUN_SPEED_PPS * frame_time
        self.move()

    def move(self):
        self.x += self.distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 10, self.x + 20, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Moon:
    PIXEL_PER_KMETER = (10.0 / 0.5)
    RUN_SPEED_KMPH = 180000.0
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    image = None

    def __init__(self):
        self.dir = 0
        self.frame = 0
        self.x, self.y = 0, 0
        if Moon.image is None:  # 70 x 15 size
            Moon.image = load_image('AyinMissile_Moon.png')

    def update(self, frame_time):
        self.distance = self.RUN_SPEED_PPS * frame_time
        self.move()

    def move(self):
        self.x += self.distance

    def draw(self):
        self.image.draw(self.x, self.y)
        # self.image2.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 35, self.y - 7.5, self.x + 35, self.y + 7.5

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Bullet_effect():
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 15

    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.frame = 0
        self.total_frame = 0

        if Bullet_effect.image is None:
            self.image = load_image("Explode.png")
            #750 x 50 size

    def update(self, frame_time):
        self.total_frame += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frame % 15)

    def draw(self):
        self.image.clip_draw(self.frame * 50, 0, 50, 50, self.x, self.y)
        #self.character_image.clip_draw((self.frame % 3) * 60, 0, 60, 68, self.x, self.y)

class Special_attack():
    #2200 x 100 size
    PIXEL_PER_KMETER = (10.0 / 0.5)
    RUN_SPEED_KMPH = 180000.0
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    TIME_PER_ACTION = 5.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION  #2
    FRAMES_PER_ACTION = 4

    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.frame = 0
        self.total_frames = 0
        self.distance = 0
        self.plusdistance = 0
        if Special_attack.image is None:
            Special_attack.image = load_image("SpecialAttack.png")

    def update(self, frame_time):
        self.distance = self.RUN_SPEED_PPS * frame_time
        self.plusdistance
        self.x += self.distance
        self.total_frames += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames)


    def draw(self):
        self.image.clip_draw(self.frame * 2200, 0, 2200, 95, self.x, self.y)

    def get_bb(self):
        return self.x - 1100, self.y - 60, self.x + 1100, self.y + 60