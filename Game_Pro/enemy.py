from pico2d import*
import random
import main_state

enemy1_time = 0
enemy2_time = 0
enemy3_time = 0
enemy4_time = 0




# enemy의 크기 = 200x40에 네마리 == 50 x 40 size
class Enemy1:
    PIXEL_PER_METER = (10.0 / 0.2)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 7

    image = None

    def __init__(self):
        self.x, self.y = random.randint(700, 790), random.randint(100, 500)
        self.frame = 0
        self.total_frames = 0
        self.dir = -1 # -1은 앞으로 1은 뒤로

        if Enemy1.image is None:
            self.image = load_image('EnemyOne.png')
        self.hp = 20
        self.x_runspeed = self.dir * self.RUN_SPEED_PPS
        self.y_runspeed = random.choice([-1, 1]) * self.RUN_SPEED_PPS

    def update(self, frame_time):
        self.total_frames += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 7

        self.x += self.x_runspeed * frame_time
        self.y += self.y_runspeed * frame_time
        if self.x > 800:
            self.x_runspeed = -self.x_runspeed
        if self.x < 500:
            self.x_runspeed = -self.x_runspeed
        if self.y > 550:
            self.y_runspeed = -self.y_runspeed
        if self.y < 50:
            self.y_runspeed = -self.y_runspeed

    def draw(self):
        self.image.clip_draw((self.frame % 4) * 50, 0, 50, 40, self.x, self.y)
        # clip_draw_to_origin(self, left, botton, width, height, x, y, w, h)

    def get_bb(self):
        return self.x - 35, self.y -35, self.x + 35, self.y + 35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Enemy2:
    pass

class Enemy3:
    pass

class Enemy4:
    pass

class Dead_Enemy1:
    TIME_PER_ACTION = 1.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __int__(self):
        self.image = load_image("EnemyOne(attacked).png")
        self.frame = 0
        self.total_frames = 0
        self.x, self.y = 0, 0

    def update(self, frame_time):
        self.total_frames += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames)

    def draw(self):
        self.image.clip_draw((self.frame % 3) * 50, 0, 50, 40, self.x, self.y)
        #self.character_image.clip_draw((self.frame%3) * 60, 0, 60, 68, self.x, self.y)




