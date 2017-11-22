from pico2d import*
import random

class Player:
    image = None
    shooting_sound = None

    PIXEL_PER_KMETER = (10.0/0.5)
    RUN_SPEED_KMPH = 36000.0
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    STAND, MOVE_RIGHT, MOVE_LEFT, MOVE_UP, MOVE_DOWN = 0, 1, 2, 3, 4

    def __init__(self):
        self.x, self.y = 100, 300
        self.dir = 0  # 0 : stand, 1 : right, 2 : left, 3 : up, 4 : down
        self.state = self.STAND
        self.live = True
        self.shooting = False
        self.image = load_image('character_right.png')


    def you_dead(self):
        self.live = False
        pass

    def update(self, frame_time):
        distance = Player.RUN_SPEED_PPS * frame_time
        if self.state in(self.MOVE_RIGHT, self.MOVE_LEFT):
            self.x += (self.dir * distance)
        elif self.state in(self.MOVE_UP, self.MOVE_DOWN):
            self.y += (self.dir * distance)

    def draw(self):
        frame = 0
        self.image.clip_draw(frame * 40, 0, 40, 40, self.x, self.y)
        self.frame = (frame + 1) % 11
        delay(0.05)
        # clip_draw_to_origin(self, left, botton, width, height, x, y, w, h)

    def handle_event(self, event):
        if(event.type, event.key) ==(SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.STAND, self.MOVE_LEFT):
                self.state = self.MOVE_LEFT
                self.dir = -1

        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in(self.STAND, self.MOVE_RIGHT):
                self.state = self.MOVE_RIGHT
                self.dir = 1

        elif(event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in(self.MOVE_LEFT,):
                self.state = self.STAND
                self.dir = 0

        elif(event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in(self.MOVE_RIGHT,):
                self.state = self.STAND
                self.dir = 0

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.state in (self.STAND, self.MOVE_UP):
                self.state = self.MOVE_UP
                self.dir = 1

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.state in (self.STAND, self.MOVE_DOWN):
                self.state = self.MOVE_DOWN
                self.dir = -1

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            if self.state in (self.MOVE_UP,):
                self.state = self.STAND
                self.dir = 0

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.state in (self.MOVE_DOWN,):
                self.state = self.STAND
                self.dir = 0






