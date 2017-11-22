from pico2d import*
import random

class Player_Bullet:
    image = None
    shooting_sound = None

    PIXEL_PER_KMETER = (10.0 / 0.5)
    RUN_SPEED_KMPH = 180000.0
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 9

    def __init__(self):
        self.x, self.y = -100, -50 # 화면밖에서 일단 객체 생성
        self.shooting = False
        self.shoot_start = False
        self.shoot_dir = -1
        self.frame = 0

        if Player_Bullet.image == None:
            Player_Bullet.image = load_image('character_bullet.png')

    def update(self, frame_time, player_x, player_y):
        if self.shooting is True:
            if self.shoot_start is True:
                self.x = player_x + 10
                self.y = player_y
                self.shoot_start = False
            if self.x > 800:
                self.x = self.shoot_dir * 30
                self.shooting = False

        distance = self.RUN_SPEED_PPS * frame_time
        self.x += distance

    def draw(self):
        if self.shooting == True:
            self.image.clip_draw((self.frame%9) * 24, 0, 24, 18, self.x, self.y)
        #self.character_image.clip_draw((self.frame%11) * 40, 0, 40, 40, self.x, self.y)

    def handle_event(self, event):
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            if self.shooting is False:
                self.x = -30
                self.shooting = True
                self.shoot_start = True



