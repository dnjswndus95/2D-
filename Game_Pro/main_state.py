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
Score = 0

current_time = get_time()

player = None
background = None
player_bullet = None
bullets = None
bullet_effects = None
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

def collision_bullet_enemy():
    global player_bullet, enemies1, enemies2, enemies3, enemies4, bullets, basic_attack_effects, special_attack_effects, \
        dead_enemy1, dead_enemy2, dead_enemy3, dead_enemy4
    All_enemies = enemies1 + enemies2 + enemies3 + enemies4

    for new_attack in player_bullet:
        for enemy in All_enemies:
            if collision_check(new_attack, enemy):
                new_attack_effect = Bullet_effect()
                new_attack_effect.x, new_attack_effect.y = new_attack.x, new_attack.y
                bullet_effects.append(new_attack_effect)
                if new_attack in player_bullet:
                    player_bullet.remove(new_attack)
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
    collision_bullet_enemy()
    player.update(frame_time)
    update_all_attack(frame_time)
    make_enemy(frame_time)
    update_all_enemy(frame_time)
    dead_effect_update(frame_time)

    current_time += frame_time

def draw_all():
    global player, dead_enemy1, dead_enemy2, dead_enemy3, dead_enemy4, enemies1, enemies2, enemies3, enemies4\
    ,player_bullet, bullet_effects

    all_attack = player_bullet, bullet_effects
    all_dead_enemy = dead_enemy1 + dead_enemy2 + dead_enemy3 + dead_enemy4
    all_enemy = enemies1 + enemies2 + enemies3 + enemies4

    player.draw()
    for attack in all_attack:
        attack.draw()
    for dead_enemy in all_dead_enemy:
        dead_enemy.draw()
    for enemy in all_enemy:
        enemy.draw()


def draw(frame_time):
    global background
    clear_canvas()
    background.draw()
    draw_all()
    update_canvas()

def update_all_attack(frame_time):
    global player_bullet, bullet_effects

    for new_attack in player_bullet:
        new_attack.update(frame_time)
        if new_attack.x > 800 or new_attack.x < 0:
            del (new_attack)

    for attack_effect in bullet_effects:
        attack_effect.update(frame_time)
        if attack_effect.frame == 5:
            bullet_effects.remove(attack_effect)


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
        enemy1_time =0

    if enemy2_time > 5:
        if current_time > 30:
            new_enemy2 = Enemy2()
            enemies2.append(new_enemy2)
        new_enemy2 = Enemy2()
        enemies2.append(new_enemy2)
        enemy2_time =0

    if enemy3_time > 20:
        if current_time > 30:
            for i in range (3):
                new_enemy3 = Enemy3()
                enemies3.append(new_enemy3)
        new_enemy3 = Enemy3()
        enemies3.append(new_enemy3)
        enemy3_time =0

    if enemy4_time > 3:
        if current_time > 20:
            new_enemy4 = Enemy4()
            enemies4.append(new_enemy4)
        new_enemy4 = Enemy4()
        enemies4.append(new_enemy4)
        enemy4_time =0

# 적 update, 적이 죽으면 이펙트 좌표에 추가
def update_all_enemy(frame_time):
    global enemies1, enemies2, enemies3, enemies4, dead_enemy1, dead_enemy2, dead_enemy3, dead_enemy4

    for new_enemy1 in enemies1:
        new_enemy1.update(frame_time)
        if new_enemy1.hp <= 0:
            new_dead_enemy = Dead_Enemy1()
            new_dead_enemy.x, new_dead_enemy.y = new_enemy1.x, new_enemy1.y
            dead_enemy1.append(new_dead_enemy)
            enemies1.remove(new_enemy1)

    for new_enemy2 in enemies2:
        new_enemy2.update(frame_time)
        if new_enemy2.hp <= 0:
            new_dead_enemy = Dead_Enemy2()
            new_dead_enemy.x, new_dead_enemy.y = new_enemy2.x, new_enemy2.y
            dead_enemy2.append(new_dead_enemy)
            enemies2.remove(new_enemy2)

    for new_enemy3 in enemies3:
        new_enemy3.update(frame_time)
        if new_enemy3.hp <= 0:
            new_dead_enemy = Dead_Enemy1()
            new_dead_enemy.x, new_dead_enemy.y = new_enemy3.x, new_enemy3.y
            dead_enemy3.append(new_dead_enemy)
            enemies3.remove(new_enemy3)

    for new_enemy4 in enemies4:
        new_enemy4.update(frame_time)
        if new_enemy4.hp <= 0:
            new_dead_enemy = Dead_Enemy4()
            new_dead_enemy.x, new_dead_enemy.y = new_enemy4.x, new_enemy4.y
            dead_enemy4.append(new_dead_enemy)
            enemies4.remove(new_enemy4)


def dead_effect_update(frame_time):
    global dead_enemy1, dead_enemy2, dead_enemy3, dead_enemy4

    for dead_em1 in dead_enemy1:
        dead_em1.update(frame_time)
        if dead_em1.frame >= 10:
            dead_enemy1.remove(dead_em1)

    for dead_em2 in dead_enemy2:
        dead_em2.update(frame_time)
        if dead_em2.frame >= 10:
            dead_enemy2.remove(dead_em2)

    for dead_em3 in dead_enemy3:
        dead_em3.update(frame_time)
        if dead_em3.frame >= 10:
            dead_enemy3.remove(dead_em3)

    for dead_em4 in dead_enemy4:
        dead_em4.update(frame_time)
        if dead_em4.frame >= 10:
            dead_enemy4.remove(dead_em4)


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
    del bullet_effects


def enter():
    global background, player, background, player_bullet, enemies1, enemies2, enemies3, enemies4, \
        dead_enemy1, dead_enemy2, dead_enemy3, dead_enemy4, bullet_effects

    background = Background(800, 600)
    player = Player()
    player_bullet = []
    enemies1 = []
    enemies2 = []
    enemies3 = []
    enemies4 = []
    bullet_effects = []
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







