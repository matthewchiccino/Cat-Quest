import pygame
import os
from sys import exit
import random

# install screen
pygame.init()

pygame.display.set_caption("Suki's Adventure to Save Papaya")
LENGTH, WIDTH = 500, 500
screen = pygame.display.set_mode((LENGTH, WIDTH))

clock = pygame.time.Clock()

BLUE = (70, 123, 183)
PINK = (242, 135, 247)

# Initalize widgets
font = pygame.font.Font(os.path.join("misc assets", "Pixeltype.ttf"), 40)
small_font = pygame.font.Font(os.path.join("misc assets", "Pixeltype.ttf"), 28)
med_font = pygame.font.Font(os.path.join("misc assets", "Pixeltype.ttf"), 55)
big_font = pygame.font.Font(os.path.join("misc assets", "Pixeltype.ttf"), 75)
text_equal_sign = font.render("=", False, "black")
text_plus_sign = font.render("+", False, "black")
price = font.render("$ :   25 ", False, "black")
price_2 = font.render("50", False, "black")
price_3 = font.render("75", False, "black")
start_message = med_font.render("Help Suki find his sister", False, "black")
start_message_rect = start_message.get_rect(center = (LENGTH / 2, 150))
start_message_2 = med_font.render("Press SPACE to start", False, "black")
start_message_2_rect = start_message_2.get_rect(center = (LENGTH / 2, 195))
help_bubble = pygame.image.load(os.path.join("misc assets", "help text bubble.png")).convert_alpha()
win_message = big_font.render("CONGRATULATIONS!", False, "black")
win_message_rect = win_message.get_rect(center = (LENGTH / 2, 100))
win_message_2 = big_font.render("You've saved Papaya", False, "black")
win_message_2_rect = win_message_2.get_rect(center = (LENGTH / 2, 165))
win_message_3 = small_font.render("Made by Matthew Chiccino, for Mariangela Morreale", False, "black")
m_r_f = pygame.transform.scale(
    pygame.image.load(os.path.join("misc assets", "More rare fish.png")).convert_alpha(), (65, 65))


rectangle = pygame.Rect(0, 0, LENGTH, 100)

frame = pygame.transform.scale(
    pygame.image.load(os.path.join("misc assets", "bg frame.png")).convert_alpha(), (75, 75))
gold_frame = pygame.transform.scale(
    pygame.image.load(os.path.join("misc assets", "gold bg frame.png")).convert_alpha(), (75, 75))
mark = pygame.image.load(os.path.join("misc assets", "Check mark.png")).convert_alpha()
heart = pygame.image.load(os.path.join("misc assets", "heart.png")).convert_alpha()
heart_rect = heart.get_rect(center = (LENGTH / 2, 325))


play_button = pygame.image.load(os.path.join("misc assets", "play again button.png")).convert_alpha()
gold_play_button = pygame.image.load(os.path.join("misc assets", "gold play again button.png")).convert_alpha()
play_button_rect = play_button.get_rect(center = (400, 400))

door = pygame.transform.scale(
    pygame.image.load(os.path.join("misc assets", "Door.png")).convert_alpha(), (100, 100))
door_rect = door.get_rect(bottomright = (LENGTH, 120))

platform = pygame.image.load(os.path.join("misc assets", "Platform.png")).convert_alpha()
platform_rect = platform.get_rect(topright = (LENGTH, 120))

frame1_rect = frame.get_rect(topleft = (50, 125))
frame2_rect = frame.get_rect(topleft = (50, 225))
frame3_rect = frame.get_rect(topleft = (50, 325))

# outside bg
bg1_1 = pygame.image.load(os.path.join("misc assets", "bg1.1.png")).convert_alpha()
bg1_2 = pygame.image.load(os.path.join("misc assets", "bg1.2.png")).convert_alpha()
bg1_3 = pygame.image.load(os.path.join("misc assets", "bg1.3.png")).convert_alpha()
bg1_4 = pygame.image.load(os.path.join("misc assets", "bg1.4.png")).convert_alpha()

bg2_1 = pygame.image.load(os.path.join("misc assets", "bg2.1.png")).convert_alpha()
bg2_2 = pygame.image.load(os.path.join("misc assets", "bg2.2.png")).convert_alpha()
bg2_3 = pygame.image.load(os.path.join("misc assets", "bg2.3.png")).convert_alpha()
bg2_4 = pygame.image.load(os.path.join("misc assets", "bg2.4.png")).convert_alpha()

bg3_1 = pygame.image.load(os.path.join("misc assets", "bg3.1.png")).convert_alpha()
bg3_2 = pygame.image.load(os.path.join("misc assets", "bg3.2.png")).convert_alpha()
bg3_3 = pygame.image.load(os.path.join("misc assets", "bg3.3.png")).convert_alpha()
bg3_4 = pygame.image.load(os.path.join("misc assets", "bg3.4.png")).convert_alpha()


#starting
bg1 = bg1_1
bg2 = bg2_1
bg3 = bg3_1


bg4 = pygame.image.load(os.path.join("misc assets", "House wall.png")).convert_alpha()
bg5 = pygame.image.load(os.path.join("misc assets", "ocean.png")).convert_alpha()
bg6 = pygame.image.load(os.path.join("misc assets", "start screen.png")).convert_alpha()

bg7 = pygame.transform.scale(
    pygame.image.load(os.path.join("misc assets", "Castles (1).png")).convert_alpha(), (500, 500))
bg8 = pygame.transform.scale(
    pygame.image.load(os.path.join("misc assets", "Castles (2).png")).convert_alpha(), (500, 500))
bg9 = pygame.transform.scale(
    pygame.image.load(os.path.join("misc assets", "Castles (3).png")).convert_alpha(), (500, 500))

bg_width = bg1_1.get_width()
bg_scroll = 0

pig = pygame.image.load(os.path.join("misc assets", "Piggy Bank.png")).convert_alpha()
gold_pig = pygame.image.load(os.path.join("misc assets", "gold piggy Bank.png")).convert_alpha()
pig_rect = pig.get_rect(midright=(WIDTH - 30, 350))

exit_sign = pygame.image.load(os.path.join("misc assets", "exit sign.png")).convert_alpha()
gold_exit_sign = pygame.image.load(os.path.join("misc assets", "gold exit sign.png")).convert_alpha()
exit_sign_rect = exit_sign.get_rect(center=(WIDTH // 4, LENGTH // 6))


fish1 = pygame.image.load(os.path.join("misc assets", "fish1.png")).convert_alpha()
fish2 = pygame.image.load(os.path.join("misc assets", "fish2.png")).convert_alpha()
fish3 = pygame.image.load(os.path.join("misc assets", "fish3.png")).convert_alpha()
fish1_rect_list_r = []
fish1_rect_list_l = []
fish2_rect_list_r = []
fish2_rect_list_l = []
fish3_rect_list_r = []
fish3_rect_list_l = []


fish1_score = 0
fish2_score = 0
fish3_score = 0


trap_door_1 = pygame.transform.scale(
    pygame.image.load(os.path.join("misc assets", "trap door 1.png")).convert_alpha(), (100, 100))
trap_door_2 = pygame.transform.scale(
    pygame.image.load(os.path.join("misc assets", "trap door 2.png")).convert_alpha(), (100, 100))
trap_door_rect = trap_door_1.get_rect(topleft=(400, 400))

key = pygame.image.load(os.path.join("misc assets", "key.png")).convert_alpha()
key_rect = key.get_rect(midbottom=(50, 400))
posion = pygame.transform.scale(pygame.image.load(
    os.path.join("misc assets", "posion.png")).convert_alpha(), (75, 75))
posion_rect = key.get_rect(midbottom=(random.randint(50, 450), 450))
dungeon = pygame.image.load(os.path.join("misc assets", "dungeon.png")).convert_alpha()



front_cat_1 = pygame.transform.scale(
    pygame.image.load(os.path.join("Cats", "front cat 1.png")).convert_alpha(), (100, 100))
front_cat_2 = pygame.transform.scale(
    pygame.image.load(os.path.join("Cats", "front cat 2.png")).convert_alpha(), (100, 100))

stand_cat_1 = pygame.transform.scale(
    pygame.image.load(os.path.join("Cats", "Right Sitting cat 1.png")).convert_alpha(), (100, 100))
stand_cat_2 = pygame.transform.scale(
    pygame.image.load(os.path.join("Cats", "Right Sitting cat 2.png")).convert_alpha(), (100, 100))
stand_cat_3 = pygame.transform.scale(
    pygame.image.load(os.path.join("Cats", "Right Sitting cat 3.png")).convert_alpha(), (100, 100))
stand_cat_4 = pygame.transform.scale(
    pygame.image.load(os.path.join("Cats", "Right Sitting cat 4.png")).convert_alpha(), (100, 100))

walk_cat_1 = pygame.transform.scale(
    pygame.image.load(os.path.join("Cats", "Right walk cat 1.png")).convert_alpha(), (100, 100))
walk_cat_2 = pygame.transform.scale(
    pygame.image.load(os.path.join("Cats", "Right walk cat 2.png")).convert_alpha(), (100, 100))
walk_cat_3 = pygame.transform.scale(
    pygame.image.load(os.path.join("Cats", "Right walk cat 3.png")).convert_alpha(), (100, 100))
walk_cat_4 = pygame.transform.scale(
    pygame.image.load(os.path.join("Cats", "Right walk cat 4.png")).convert_alpha(), (100, 100))

swim_cat_1 = pygame.transform.scale(
    pygame.image.load(os.path.join("Cats", "cat-sheet.png")).convert_alpha(), (100, 100))
swim_cat_2 = pygame.transform.scale(
    pygame.image.load(os.path.join("Cats", "cat swim 2.png")).convert_alpha(), (100, 100))
swim_cat_3 = pygame.transform.scale(
    pygame.image.load(os.path.join("Cats", "cat swim 3.png")).convert_alpha(), (100, 100))
swim_cat_4 = pygame.transform.scale(
    pygame.image.load(os.path.join("Cats", "cat swim 4.png")).convert_alpha(), (100, 100))
swim_cat_5 = pygame.transform.scale(
    pygame.image.load(os.path.join("Cats", "cat swim 5.png")).convert_alpha(), (100, 100))

jump_cat_1 = pygame.transform.scale(
    pygame.image.load(os.path.join("Cats", "cat_jump_1.png")).convert_alpha(), (100, 100))
jump_cat_2 = pygame.transform.scale(
    pygame.image.load(os.path.join("Cats", "cat_jump_2.png")).convert_alpha(), (100, 100))
jump_cat_3 = pygame.transform.scale(
    pygame.image.load(os.path.join("Cats", "cat_jump_3.png")).convert_alpha(), (100, 100))

laying_dead_cat = pygame.transform.scale(
    pygame.image.load(os.path.join("Cats", "laying dead cat.png")).convert_alpha(), (100, 100))

cat_index = 0
wag_cat_list = [stand_cat_1, stand_cat_2, stand_cat_3, stand_cat_4]
walk_cat_list = [walk_cat_1, walk_cat_2, walk_cat_3, walk_cat_4]
swim_cat_list = [swim_cat_1, swim_cat_2, swim_cat_3, swim_cat_4, swim_cat_5, swim_cat_5]
jump_cat_list = [jump_cat_1, jump_cat_2, jump_cat_3, jump_cat_1]
cat = stand_cat_1
cat_rect = cat.get_rect(center=(LENGTH // 2, 315))


cat_speed = 3
gravity = 0
time = 0


wag_left = False
swim_left = False
outside = False
in_house = False
in_bank = False
in_castle = False
win_screen = False
underwater = False
on_platform = False
start_screen = True
in_dungeon = False

frame1_selected = False
frame2_selected = False
frame3_selected = False

item1_bought = False
item2_bought = False
item3_bought = False

has_key = False
has_posion = False
cat_dead = False

swim_speed = 3

def walk_ani(direction):
    global cat_index, cat
    cat_index += 0.1
    if not direction:
        cat = walk_cat_list[int(cat_index)]
    else:
        cat = pygame.transform.flip(walk_cat_list[int(cat_index)], True, False)
    if cat_index >= 3.9:
        cat_index = 0

def tail_wag_ani(direction):
    global cat_index, cat
    cat_index += 0.1
    if not direction:
        cat = wag_cat_list[int(cat_index)]
    else:
        cat = pygame.transform.flip(wag_cat_list[int(cat_index)], True, False)
    if cat_index >= 3.9:
        cat_index = 0

def swim_ani(direction):
    global cat_index, cat, swim_right
    cat_index += 0.1
    if not direction:
        cat = swim_cat_list[int(cat_index)]
    else:
        cat = pygame.transform.flip(swim_cat_list[int(cat_index)], True, False)
    if cat_index >= 5.9:
        cat_index = 0

def jump_ani(direction):
    global cat_index, cat, wag_left
    cat_index += 0.1
    if direction == False:
        cat = jump_cat_list[int(cat_index)]
    else:
        cat = pygame.transform.flip(jump_cat_list[int(cat_index)], True, False)
    if cat_index >= 1.9:
        cat_index = 0

def swim_control():
    global swim_left
    if keys[pygame.K_LEFT]:
        cat_rect.x -= swim_speed
        swim_ani(True)
        swim_left = True
    if keys[pygame.K_RIGHT]:
        cat_rect.x += swim_speed
        swim_ani(False)
        swim_left = False
    if keys[pygame.K_UP]:
        cat_rect.y -= swim_speed
        swim_ani(swim_left)
    if keys[pygame.K_DOWN]:
        cat_rect.y += swim_speed
        swim_ani(swim_left)

    if cat_rect.x >= LENGTH - 100:
        cat_rect.x = LENGTH - 100
    if cat_rect.x < 0:
        cat_rect.x = 0
    if cat_rect.y > WIDTH - 100:
        cat_rect.y = WIDTH - 100

def walk_control():

    global wag_left, bg_scroll, cat_rect, gravity, cat
    if keys[pygame.K_UP] and item3_bought:
        if keys[pygame.K_LEFT]:
            jump_ani(True)
            wag_left = True
            bg_scroll += 3
            if in_house:
                cat_rect.x -= 3
                if cat_rect.x <= -10: cat_rect.x = -10
        elif keys[pygame.K_RIGHT]:
            jump_ani(False)
            wag_left = False
            bg_scroll -= 3
            if in_house:
                cat_rect.x += 3
                if cat_rect.x >= 410: cat_rect.x = 410

        elif wag_left:
            jump_ani(True)

        else:
            jump_ani(False)
    elif keys[pygame.K_LEFT]:
        walk_ani(True)
        wag_left = True
        bg_scroll += 3
        if in_house:
            cat_rect.x -= 3
            if cat_rect.x <= -10: cat_rect.x = -10

    elif keys[pygame.K_RIGHT]:
        walk_ani(False)
        wag_left = False
        bg_scroll -= 3
        if in_house:
            cat_rect.x += 3
            if cat_rect.x >= 410: cat_rect.x = 410
    else:
        tail_wag_ani(wag_left)

    if cat_dead:
        cat = laying_dead_cat

def fish_function():
    global fish1_score, fish2_score, fish3_score
    if fish1_rect_list_r or fish1_rect_list_l:
        for i in fish1_rect_list_r:
            i.x -= 2
            screen.blit(pygame.transform.flip(fish1, True, False), i)
            if i.colliderect(cat_rect):
                fish1_rect_list_r.remove(i)
                fish1_score += 1
                if i.x <= -1200: fish1_rect_list_r.remove(i)

        for i in fish1_rect_list_l:
            i.x += 2
            screen.blit(fish1, i)
            if i.colliderect(cat_rect):
                fish1_rect_list_l .remove(i)
                fish1_score += 1
                if i.x >= 1200: fish1_rect_list_l.remove(i)

    if fish2_rect_list_r or fish2_rect_list_l:
        for j in fish2_rect_list_r:
            j.x -= 3.5
            screen.blit(pygame.transform.flip(fish2, True, False), j)
            if j.colliderect(cat_rect):
                fish2_score += 1
                fish2_rect_list_r.remove(j)
            if j.x <= -1200: fish2_rect_list_r.remove(j)
        for j in fish2_rect_list_l:
            j.x += 3.5
            screen.blit(fish2, j)
            if j.colliderect(cat_rect):
                fish2_score += 1
                fish2_rect_list_l.remove(j)
            if j.x >= 1200: fish2_rect_list_l.remove(j)
    if fish3_rect_list_r or fish3_rect_list_l:
        for i in fish3_rect_list_r:
            i.x -= 5
            screen.blit(pygame.transform.flip(fish3, True, False), i)
            if i.colliderect(cat_rect):
                fish3_score += 1
                fish3_rect_list_r.remove(i)
            if i.x <= -1200: fish3_rect_list_r.remove(i)
        for i in fish3_rect_list_l:
            i.x += 5
            screen.blit(fish3, i)
            if i.colliderect(cat_rect):
                fish3_score += 1
                fish3_rect_list_l.remove(i)
            if i.x >= 1200: fish3_rect_list_l.remove(i)

def store_function():
    global fish2_time, fish3_time, frame1_rect, frame2_rect, frame3_rect, item1_bought, item2_bought, item3_bought
    global frame1_selected, frame2_selected, frame3_selected, fish1_score, fish2_score, fish3_score, swim_speed
    if frame1_rect.collidepoint(pygame.mouse.get_pos()) and item1_bought == False:
        frame1_selected = True
    else:
        frame1_selected = False
    if frame2_rect.collidepoint(pygame.mouse.get_pos()) and item2_bought == False:
        frame2_selected = True
    else:
        frame2_selected = False
    if frame3_rect.collidepoint(pygame.mouse.get_pos()) and item3_bought == False:
        frame3_selected = True
    else:
        frame3_selected = False

    if frame1_selected == True and mouse_down:
        if fish1_score >= 25:
            fish1_score -= 25
            if fish1_score < 0: fish1_score = 0
            print("item 1 bought")
            item1_bought = True
            pygame.time.set_timer(fish2_timer, 0)
            fish2_time = 1500
            pygame.time.set_timer(fish2_timer, fish2_time)

            pygame.time.set_timer(fish3_timer, 0)
            fish3_time = 6000
            pygame.time.set_timer(fish3_timer, fish3_time)

    if frame2_selected == True and mouse_down:
        if fish2_score >= 25:
            fish2_score -= 25
            if fish2_score < 0: fish2_score = 0
            print("item 2 bought")
            item2_bought = True
            swim_speed = 5
    if frame3_selected == True and mouse_down:
        if fish3_score >= 25 and fish2_score >= 50 and fish1_score >= 75:
            fish3_score -= 25
            fish2_score -= 50
            fish1_score -= 75
            if fish1_score < 0: fish1_score = 0
            if fish2_score < 0: fish2_score = 0
            if fish3_score < 0: fish3_score = 0
            print("item 3 bought")
            item3_bought = True

fish1_time = 1500
fish2_time = 7500
fish3_time = 15000

fish1_timer = pygame.USEREVENT + 1
pygame.time.set_timer(fish1_timer, fish1_time)

fish2_timer = pygame.USEREVENT + 2
pygame.time.set_timer(fish2_timer, fish2_time)

fish3_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fish3_timer, fish3_time)

day_cycle_timer = pygame.USEREVENT + 4
pygame.time.set_timer(day_cycle_timer, 10000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        keys = pygame.key.get_pressed()
        # regular jump
        if keys[pygame.K_UP] and has_posion:
            if in_castle:
                gravity = -15
            elif in_house or outside:
                gravity = -15
        if keys[pygame.K_UP] and item3_bought and cat_rect.y == 265 and (in_house or outside) and has_posion == False:
            gravity = -20
        # jump in castle
        if keys[pygame.K_UP] and in_castle and cat_rect.y == 275 and has_posion == False:
            gravity = -17

        # time_cycle
        if event.type == day_cycle_timer:
            if time < 11:
                time += 1
            else:
                time = 0
            if time == 0 or time == 1 or time == 10 or time == 11:
                bg1 = bg1_1
                bg2 = bg2_1
                bg3 = bg3_1
            elif time == 2 or time == 3 or time == 8 or time == 9:
                bg1 = bg1_2
                bg2 = bg2_2
                bg3 = bg3_2
            elif time == 4 or time == 7:
                bg1 = bg1_3
                bg2 = bg2_3
                bg3 = bg3_3
            elif time == 5 or time == 6:
                bg1 = bg1_4
                bg2 = bg2_4
                bg3 = bg3_4


        if underwater:
            if event.type == fish1_timer:
                print("fish1 event")
                l_or_r = random.randint(0, 1)
                if l_or_r == 0:
                    fish1_rect_list_r.append(fish1.get_rect(center=(
                        700, random.randint(100, 400))))
                else:
                    fish1_rect_list_l.append(fish1.get_rect(center=(
                        -200, random.randint(100, 400))))
            if event.type == fish2_timer:
                print("fish2 event")

                l_or_r = random.randint(0, 1)
                if l_or_r == 0:
                    fish2_rect_list_r.append(fish2.get_rect(center=(
                        700, random.randint(100, 400))))
                else:
                    fish2_rect_list_l.append(fish2.get_rect(center=(
                        -200, random.randint(100, 400))))
            if event.type == fish3_timer:
                print("fish3_event")
                l_or_r = random.randint(0, 1)
                if l_or_r == 0:
                    fish3_rect_list_r.append(fish3.get_rect(center=(
                        700, random.randint(100, 400))))
                else:
                    fish3_rect_list_l.append(fish3.get_rect(center=(
                        -200, random.randint(100, 400))))

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_down = True
    else:
        mouse_down = False
    # gravity
    if underwater == False and on_platform == False\
            and in_castle == False and in_dungeon == False:
        gravity += 0.7
        cat_rect.y += gravity
        if cat_rect.y >= 265:
            cat_rect.y = 265
    elif in_castle:
        gravity += 0.7
        cat_rect.y += gravity
        if cat_rect.y >= 275 and (bg_scroll > -160 or bg_scroll < -450):
            cat_rect.y = 275

    if outside:
        screen.blit(bg1, (0 + bg_scroll, 0))
        screen.blit(bg2, (-WIDTH + bg_scroll, 0))
        screen.blit(bg3, (WIDTH + bg_scroll, 0))
        screen.blit(cat, cat_rect)
        walk_control()

        if bg_scroll < -650:
            in_house = True
            outside = False
        if bg_scroll > 650:
            underwater = True
            outside = False
            cat_rect.y = 350

    if in_house:
        screen.blit(bg4, (0, 0))
        screen.blit(pig, pig_rect)
        screen.blit(cat, cat_rect)
        screen.blit(exit_sign, exit_sign_rect)
        screen.blit(door, door_rect)
        screen.blit(platform, platform_rect)
        if exit_sign_rect.collidepoint(pygame.mouse.get_pos()):  # and pygame.mouse.get_pressed():
            screen.blit(gold_exit_sign, exit_sign_rect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                bg_scroll = -500
                cat_rect = cat.get_rect(center=(LENGTH // 2, 315))
                in_house = False
                outside = True
                wag_left = True
        if pig_rect.collidepoint(pygame.mouse.get_pos()):  # and pygame.mouse.get_pressed():
            screen.blit(gold_pig, pig_rect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                in_house = False
                in_bank = True
                exit_sign_rect = exit_sign.get_rect(center=(100, WIDTH - 50))
        if cat_rect.colliderect(platform_rect) and cat_rect.y <= 25:
            on_platform = True
            cat_rect.y = 25
            screen.blit(cat, cat_rect)
        else: on_platform = False
        if cat_rect.colliderect(platform_rect) and cat_rect.y >= 50:
            cat_rect.y = 200
            on_platform = False
        #screen.blit(cat, cat_rect)
        if cat_rect.colliderect(door_rect) and keys[pygame.K_UP]:
            # win_screen = True
            in_castle = True
            bg_scroll = 0
            cat_rect.x = 200
            cat_rect.y = 275
            in_house = False
            on_platform = False
        walk_control()

    if in_bank:
        screen.fill(PINK)
        screen.blit(exit_sign, exit_sign_rect)
        pygame.draw.rect(screen, (230, 230, 230), rectangle)

        screen.blit(fish1, (30, 40))
        screen.blit(fish2, (195, 40))
        screen.blit(fish3, (360, 40))

        screen.blit(text_equal_sign, (40 + fish1.get_width(), 40))
        screen.blit(text_equal_sign, (205 + fish1.get_width(), 40))
        screen.blit(text_equal_sign, (370 + fish1.get_width(), 40))

        fish1_num = font.render(str(fish1_score), False, "black")
        fish2_num = font.render(str(fish2_score), False, "black")
        fish3_num = font.render(str(fish3_score), False, "black")

        screen.blit(fish1_num, (130, 43))
        screen.blit(fish2_num, (295, 43))
        screen.blit(fish3_num, (460, 43))

        screen.blit(price, (150, 155))
        screen.blit(price, (150, 255))
        screen.blit(price, (150, 355))

        screen.blit(fish1, (225, 155))
        screen.blit(fish2, (225, 255))
        screen.blit(fish3, (225, 355))

        screen.blit(price_2, (295, 355))
        screen.blit(fish2, (330, 355))
        screen.blit(price_3, (395, 355))
        screen.blit(fish1, (430, 355))


        store_function()

        if frame1_selected:
            screen.blit(gold_frame, frame1_rect)
        else:
            screen.blit(frame, frame1_rect)
        if frame2_selected:
            screen.blit(gold_frame, frame2_rect)
        else:
            screen.blit(frame, frame2_rect)
        if frame3_selected:
            screen.blit(gold_frame, frame3_rect)
        else:
            screen.blit(frame, frame3_rect)

        screen.blit(m_r_f, (52, 135))
        screen.blit(text_plus_sign, (60, 233))
        screen.blit(pygame.transform.scale(swim_cat_2, (75, 75)), (50, 208))
        screen.blit(pygame.transform.scale(jump_cat_2, (75, 75)), (48, 311))

        if item1_bought:
            screen.blit(mark, (38, 115))
        if item2_bought:
            screen.blit(mark, (38, 215))
        if item3_bought:
            screen.blit(mark, (38, 315))


        # exit button
        if exit_sign_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(gold_exit_sign, exit_sign_rect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                in_bank = False
                in_house = True
                exit_sign_rect = exit_sign.get_rect(center=(WIDTH // 4, LENGTH // 6))

    if underwater:
        screen.blit(bg5, (0, 0))
        if has_key:
            screen.blit(trap_door_2, trap_door_rect)
        else:
            screen.blit(trap_door_1, trap_door_rect)
        screen.blit(cat, cat_rect)
        keys = pygame.key.get_pressed()
        swim_control()
        fish_function()

        if cat_rect.colliderect(trap_door_rect) and has_key:
            in_dungeon = True
            underwater = False
            cat_rect.x = 175
            cat_rect.y = 175

        if cat_rect.y <= -100:
            cat_index = 0
            underwater = False
            outside = True
            bg_scroll = 500
            cat_rect = cat.get_rect(center = (LENGTH // 2, 315))
            fish1_rect_list_r = []
            fish1_rect_list_l = []
            fish2_rect_list_r = []
            fish2_rect_list_l = []
            fish3_rect_list_r = []
            fish3_rect_list_l = []

    if in_dungeon:
        screen.blit(dungeon, (0, 0))
        screen.blit(cat, cat_rect)
        keys = pygame.key.get_pressed()
        swim_control()
        if not has_posion:
            screen.blit(posion, posion_rect)
        if cat_rect.colliderect(posion_rect):
            has_posion = True
        if cat_rect.y <= -100:
            in_dungeon = False
            underwater = True
            cat_rect.x = 300
            cat_rect.y = 400

    if in_castle:
        screen.blit(bg7, (0 + bg_scroll, 0))
        screen.blit(bg8, (WIDTH + bg_scroll, 0))
        screen.blit(bg9, (WIDTH*2 + bg_scroll, 0))
        screen.blit(cat, cat_rect)
        if not has_key: screen.blit(key, key_rect)
        walk_control()

        # allows cat to walk close to the edges
        if bg_scroll > 0 or cat_rect.x < 200:
            bg_scroll = 0
            if keys[pygame.K_LEFT]:
                cat_rect.x -= 3
        if bg_scroll < -1000 or cat_rect.x > 200:
            bg_scroll = -1000
            if keys[pygame.K_RIGHT]:
                cat_rect.x += 3
        if cat_rect.x > 200 and keys[pygame.K_LEFT]:
            cat_rect.x -= 3
        if cat_rect.x < 200 and keys[pygame.K_RIGHT]:
            cat_rect.x += 3

        elif cat_rect.y >= 400:
            cat_rect.y = 400
            cat_dead = True
            pygame.time.delay(1500)
            cat_dead = False
            bg_scroll = 0

        # prevents key from sliding
        if bg_scroll < 0:
            key_rect = key.get_rect(midbottom=(50 + bg_scroll, 400))
        if cat_rect.colliderect(key_rect):
            has_key = True

        # back to house
        if cat_rect.x < -10:
            in_castle = False
            in_house = True
            cat_rect.x = 410
            cat_rect.y = 25
            on_platform = True
        if cat_rect.x > 320 and keys[pygame.K_UP] and bg_scroll < -10:
            in_castle = False
            win_screen = True

    if win_screen:
        screen.fill(BLUE)
        screen.blit(front_cat_1, (115, 200))
        screen.blit(pygame.transform.flip(front_cat_2, True, False), (300, 200))
        screen.blit(win_message, win_message_rect)
        screen.blit(win_message_2, win_message_2_rect)
        screen.blit(heart, heart_rect)
        screen.blit(win_message_3, (10, 475))

        screen.blit(play_button, play_button_rect)
        if play_button_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(gold_play_button, play_button_rect)
            if event.type == pygame.MOUSEBUTTONDOWN:
            # restart entire game
                print("restart")
                wag_left = False
                swim_left = False
                outside = False
                in_house = False
                in_bank = False
                in_dungeon = False
                in_castle = False
                has_key = False
                has_posion = False
                underwater = False
                on_platform = False
                start_screen = True
                print("start screen = True")

                frame1_selected = False
                frame2_selected = False
                frame3_selected = False

                item1_bought = False
                item2_bought = False
                item3_bought = False

                fish1_score = 0
                fish2_score = 0
                fish3_score = 0

                swim_speed = 3

                bg_scroll = 0
                cat_rect = cat.get_rect(center=(LENGTH // 2, 315))

                win_screen = False

    if start_screen:
        screen.fill("white")
        screen.blit(bg6, (0, 0))
        screen.blit(front_cat_1, (300, 300))
        screen.blit(start_message, start_message_rect)
        screen.blit(start_message_2, start_message_2_rect)
        screen.blit(help_bubble, (380, 220))
        if keys[pygame.K_SPACE]:
            outside = True
            start_screen = False
    pygame.display.update()
    clock.tick(60)