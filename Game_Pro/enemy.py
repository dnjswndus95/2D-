from pico2d import*
import random
import main_state

enemy1_time = 0
enemy2_time = 0
enemy3_time = 0
enemy4_time = 0




# enemy의 크기 = 200x40에 네마리 == 50 x 40 size
class Enemy1:
    # 체력은 낮지만 무빙 오지는 몬스터
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
        # clip_draw_to_origin(self, left, bottom, width, height, x, y, w, h)

    def get_bb(self):
        return self.x - 35, self.y -35, self.x + 35, self.y + 35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Enemy2: # 350 x 40 7개
    #느리고 앞뒤로만 움직이는 떡대 몬스터
    PIXEL_PER_METER = (10.0 / 0.2)
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 7

    image = None

    y_init = [150, 300, 450]

    def __init__(self):
        self.x, self.y = random.randint(700, 790), random.randint(100, 500)
        self.frame = 0
        self.total_frames = 0
        self.dir = -1  # -1은 앞으로 1은 뒤로

        if Enemy1.image is None:
            self.image = load_image('EnemyTwo.png')
        self.hp = 40
        self.x_runspeed = self.dir * self.RUN_SPEED_PPS
        self.y_runspeed = 0

    def update(self, frame_time):
        self.total_frames += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 7

        self.x += self.x_runspeed * frame_time
        if self.x > 800:
            self.x_runspeed = -self.x_runspeed
        if self.x < 500:
            self.x_runspeed = -self.x_runspeed

    def draw(self):
        self.image.clip_draw((self.frame % 7) * 50, 0, 50, 40, self.x, self.y)
        # clip_draw_to_origin(self, left, botton, width, height, x, y, w, h)

    def get_bb(self):
        return self.x - 35, self.y -35, self.x + 35, self.y + 35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class Enemy3:
    #앞뒤 이속은 느리지만 펌프로 상하로는 움직임이 빠른 몬스터
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
        self.dir = -1  # -1은 앞으로 1은 뒤로

        if Enemy1.image is None:
            self.image = load_image('EnemyThree.png')
        self.hp = 30
        self.x_runspeed = self.dir * self.RUN_SPEED_PPS / 5
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
        # clip_draw_to_origin(self, left, bottom, width, height, x, y, w, h)

    def get_bb(self):
        return self.x - 35, self.y - 35, self.x + 35, self.y + 35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Enemy4:
    # 빠르지만 상하속도보단 좌우속도가 더 빠른 몬스터
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
        self.dir = -1  # -1은 앞으로 1은 뒤로

        if Enemy1.image is None:
            self.image = load_image('EnemyFour.png')
        self.hp = 20
        self.x_runspeed = self.dir * self.RUN_SPEED_PPS * 1.2
        self.y_runspeed = random.choice([-1, 1]) * self.RUN_SPEED_PPS * 0.7

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
        self.image.clip_draw((self.frame % 6) * 50, 0, 50, 40, self.x, self.y)
        # clip_draw_to_origin(self, left, bottom, width, height, x, y, w, h)

    def get_bb(self):
        return self.x - 35, self.y - 35, self.x + 35, self.y + 35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Dead_Enemy1:
    TIME_PER_ACTION = 1.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):
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


class Dead_Enemy2:
    TIME_PER_ACTION = 1.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):
        self.image = load_image("EnemyTwo(attacked).png")
        self.frame = 0
        self.total_frames = 0
        self.x, self.y = 0, 0

    def update(self, frame_time):
        self.total_frames += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames)

    def draw(self):
        self.image.clip_draw((self.frame % 3) * 50, 0, 50, 40, self.x, self.y)

class Dead_Enemy3:
    TIME_PER_ACTION = 1.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):
        self.image = load_image("EnemyThree(attacked).png")
        self.frame = 0
        self.total_frames = 0
        self.x, self.y = 0, 0

    def update(self, frame_time):
        self.total_frames += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames)

    def draw(self):
        self.image.clip_draw((self.frame % 3) * 50, 0, 50, 40, self.x, self.y)

class Dead_Enemy4:
    TIME_PER_ACTION = 1.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):
        self.image = load_image("EnemyFour(attacked).png")
        self.frame = 0
        self.total_frames = 0
        self.x, self.y = 0, 0

    def update(self, frame_time):
        self.total_frames += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames)

    def draw(self):
        self.image.clip_draw((self.frame % 3) * 50, 0, 50, 40, self.x, self.y)
