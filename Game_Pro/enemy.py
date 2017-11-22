from pico2d import*
import random

class Enemy:
    image = None

    def __init__(self):
        self.x, self.y = 0, 0
        self.arr_x, self.arr_y = 0, 0
        self.dir_x = 1
        self.dir_y = 0
        self.is_dead = False
        self.shooting = False
        self.image = load_image('character.png')
        self.x = 800 - self.arr_x * 40
        self.y = 600 - self.arr_y * 30

    def set_location(self, in_arr_x, in_arr_y):
        self.arr_x = in_arr_x
        self.arr_y = in_arr_y
        self.x = 800 - self.arr_x * 40
        self.y = 600 - self.arr_y * 30

    def set_shooting(self, is_shoot):
        self.shooting = is_shoot


