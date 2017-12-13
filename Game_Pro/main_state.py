import os
import random
import game_framework
import title_state
from Player import*
from enemy import*
from background import Background
from Resource import*

from pico2d import*

#os.chdir('C:\\Temp\\lab01')

running = True;
name = "MainState"

current_time = get_time()

player = None
background = None
player_bullet = None
enemies1 = None
enemies2 = None
enemies3 = None
enemies4 = None
dead_enemy1 = None
dead_enemy2 = None
dead_enemy3 = None
dead_enemy4 = None



# 충돌 체크 함수
def collision_check(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True

def collision_missile_enemy():
    global player_bullet, enemies1, enemies2, enemies3, enemies4
    All_enemies = enemies1 + enemies2 + enemies3 + enemies4
    global dead_enemy1, dead_enemy2, dead_enemy3, dead_enemy4

    for new_attack in bullets:
        for enemy in enemies1:
            if collision_check(new_attack, enemy):
                new_dead_enemy1 = Dead_Enemy1()
                new_dead_enemy1.x, new_dead_enemy1.y = enemy.x, enemy.y
                dead_enemy1.append(new_dead_enemy1)
                if new_attack in bullets:
                    bullets.remove(new_attack)
                enemy.hp -= 5

def handle_events(frame_time):
    events = get_events()

    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            player.handle_event(event)

def update(frame_time):
    global current_time

    background.update(frame_time)
    collision_missile_enemy()
    player.update(frame_time)
    update_all_attack(frame_time)
    make_enemy(frame_time)
    update_enemy(frame_time)
    dead_effect_update(frame_time)
    current_time += frame_time


def draw(frame_time):
    global background
    all_enemies = enemies1 + enemies2 + enemies3 + enemies4
    clear_canvas()
    background.draw()
    player.draw()
    for attack in bullets:
        attack.draw()
        attack.draw_bb()
    for enemy in enemies1:
        enemy.draw()
        enemy.draw_bb()
    update_canvas()

def update_all_attack(frame_time):
    global bullets

    for new_attack in bullets:
        new_attack.update(frame_time)
        if new_attack.x > 800 or new_attack.x < 0:
            del (new_attack)


def make_enemy(frame_time):
    global enemies1, enemies2, enemies3, enemies4, enemy1_time, enemy2_time, enemy3_time, enemy4_time
    enemy1_time += frame_time
    enemy2_time += frame_time
    enemy3_time += frame_time
    enemy4_time += frame_time
    if enemy1_time > 5:
        if current_time > 30:
            new_enemy1 = Enemy1()
            enemies1.append(new_enemy1)
        new_enemy1 = Enemy1()
        enemies1.append(new_enemy1)
        enemy1_time = 0

# 적 update, 적이 죽으면 이펙트 좌표에 추가
def update_enemy(frame_time):
    global enemies1, enemies2, enemies3, enemies4, dead_enemy1, dead_enemy2, dead_enemy3, dead_enemy4

    for new_enemy1 in enemies1:
        new_enemy1.update(frame_time)
        if new_enemy1.hp <= 0:
            new_dead_enemy = Dead_Enemy1()
            new_dead_enemy.x, new_dead_enemy.y = new_enemy1.x, new_enemy1.y
            dead_enemy1.append(new_dead_enemy)
            enemies1.remove(new_enemy1)

def dead_effect_update(frame_time):
    global dead_enemy1, dead_enemy2, dead_enemy3, dead_enemy4

    for dead_em1 in dead_enemy1:
        dead_em1.update(frame_time)
        if dead_em1.frame >= 10:
            dead_enemy1.remove(dead_em1)

def destroy_world():
    global player, enemies1, enemies2, enemies3, enemies4, background, player_bullet
    all_enemies = enemies1 + enemies2 + enemies3 + enemies4

    del(player)
    del(all_enemies)
    del(background)
    del(player_bullet)
    del dead_enemy1
    del dead_enemy2
    del dead_enemy3
    del dead_enemy4
    del enemies1
    del enemies2
    del enemies3
    del enemies4
    del bullets


def enter():
    global background, player, background, player_bullet, enemies1, enemies2, enemies3, enemies4, dead_enemy1, dead_enemy2, dead_enemy3, dead_enemy4

    background = Background(800, 600)
    player = Player()
    player_bullet = []
    enemies1 = []
    enemies2 = []
    enemies3 = []
    enemies4 = []
    dead_enemy1 = []
    dead_enemy2 = []
    dead_enemy3 = []
    dead_enemy4 = []

def exit():
        destroy_world()

def pause():
        pass

def resume():
        pass







