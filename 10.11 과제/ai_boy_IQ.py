import os
import random
import ai_boy

from pico2d import*
os.chdir('C:\\Temp\\lab01')

def __init__(self):
    self.x, self.y = random.randint(100, 700), 90
    self.frame = random.randint(0, 7)
    self.dir = 1
    if Boy.image == None:
        Boy.image = load_image('run_animation.png')

def update(self):
    self.frame = (self.frame + 1) % 8
    self.x += (self.dir * 5)
    if self.x > 800:

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
    self.stand_framdes += 1
    if self.stand_framdes == 50:
        self.state = self.LEFT_RUN
        self.run_frames = 0

def handle_right_run(self):
    self.x += 5
    self.run_frames += 1

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