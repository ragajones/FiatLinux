import random
import pygame as pg
from settings import *
from os import path

pg.init()
pg.font.init()
title_font = pg.font.SysFont('Tahoma', int(35))
game_font = pg.font.SysFont('Tahoma', int(20))
screen = pg.display.set_mode((WIDTH, HEIGHT))


def get_high_score():
    imported_list = []
    with open("high_score.txt") as file:
        for line in file:
            line = line.split(" ")  # preprocess line
            imported_list.append(line)
    # print(imported_list)


def save_high_score(bestscore, movecount):
    try:
        if bestscore < movecount:
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(bestscore))
            high_score_file.close()
        else:
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(movecount))
            high_score_file.close()
    except IOError:
        print("Unable to save the high score.")


def focus(FOCUS_X, FOCUS_Y):
    return FOCUS_X, FOCUS_Y


def focus_left(FOCUS_X, FOCUS_Y):
    if FOCUS_X > 0:
        FOCUS_X -= 1
    focus(FOCUS_X, FOCUS_Y)
    pg.time.delay(100)
    return FOCUS_X


def focus_right(FOCUS_X, FOCUS_Y):
    if FOCUS_X < ARRAY_WIDTH - 1:
        FOCUS_X += 1
    focus(FOCUS_X, FOCUS_Y)
    pg.time.delay(100)
    return FOCUS_X


def focus_up(FOCUS_X, FOCUS_Y):
    if FOCUS_Y > 0:
        FOCUS_Y -= 1
    focus(FOCUS_X, FOCUS_Y)
    pg.time.delay(100)
    return FOCUS_Y


def focus_down(FOCUS_X, FOCUS_Y):
    if FOCUS_Y < ARRAY_HEIGHT - 1:
        FOCUS_Y += 1
    focus(FOCUS_X, FOCUS_Y)
    pg.time.delay(100)
    return FOCUS_Y


def rot_clock(total, FOCUS_X, FOCUS_Y, move_count):
    start_x = FOCUS_X
    start_y = FOCUS_Y

    rotate_counter = True
    bitstobeadded = total[start_y].pop(start_x - 1)  # moving a piece from west to southwest
    total[start_y - 1].insert(start_x - 1, bitstobeadded)  # moving a piece from west to southwest

    bitstobeadded = total[start_y + 1].pop(start_x - 1)  # moving a piece from northwest to west
    total[start_y].insert(start_x - 1, bitstobeadded)  # moving a piece from northwest to west

    bitstobeadded = total[start_y].pop(start_x + 1)
    total[start_y + 1].insert(start_x + 1, bitstobeadded)

    bitstobeadded = total[start_y - 1].pop(start_x + 2)
    total[start_y].insert(start_x + 1, bitstobeadded)
    return total, rotate_counter


def rot_counterclock(total, FOCUS_X, FOCUS_Y, move_count):
    move_count = move_count + 1
    rotate_counter = True
    bitstobeadded = total[start_y].pop(start_x - 1)  # moving a piece from west to southwest
    total[start_y + 1].insert(start_x - 1, bitstobeadded)  # moving a piece from west to southwest
    bitstobeadded = total[start_y - 1].pop(start_x - 1)  # moving a piece from northwest to west
    total[start_y].insert(start_x - 1, bitstobeadded)  # moving a piece from northwest to west
    bitstobeadded = total[start_y].pop(start_x + 1)
    total[start_y - 1].insert(start_x + 1, bitstobeadded)
    bitstobeadded = total[start_y + 1].pop(start_x + 2)
    total[start_y].insert(start_x + 1, bitstobeadded)
    movecounter(move_count)
    return total, rotate_counter


def get_vert(FOCUS_X, FOCUS_Y):
    vertlist = []
    vertcolumn = []
    for x in range(0, ARRAY_WIDTH):
        for y in range(0, ARRAY_HEIGHT):
            vertcolumn.append(total[y][x])
        vertlist.append(vertcolumn)
        vertcolumn = []
    return vertlist


def transcribe(vert_list):
    horz_list = []
    horz_row = []
    for x in range(0, ARRAY_WIDTH):
        for y in range(0, ARRAY_HEIGHT):
            horz_row.append((vert_list[y][x]))
        horz_list.append(horz_row)
        horz_row = []
    return horz_list


def movecounter(move_count):
    move_count += 1
    return move_count


def solve(total):
    DELTAS_LIST = []
    for x in range(5):
        for y in range(5):
            num = abs(MASTER_LIST[x][y] - total[x][y])
            DELTAS_LIST.append(num)

    print(MASTER_LIST)
    print(total)
    print(DELTAS_LIST)


def health_bar():
    DELTAS_LIST = []
    for x in range(ARRAY_WIDTH):
        for y in range(ARRAY_HEIGHT):
            num = abs(MASTER_ARRAY[x][y] - total[x][y])
            DELTAS_LIST.append(num)
    health = sum(DELTAS_LIST)

    return health


def draw_health_bar(screen, x, y, health):
    if health < 0:
        health = 0
    BAR_LENGTH = health
    BAR_HEIGHT = 15
    fill = (health)
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    if BAR_LENGTH > 120:
        fill = 120
    pg.draw.rect(screen, DARK_GREEN, fill_rect)
    pg.draw.rect(screen, GREEN, outline_rect, 2)


def draw_elements():
    pg.draw.rect(screen, DARK_GRAY, (OFFSET, OFFSET, GAMEBOARD_WIDTH + OFFSET, HEIGHT - (2 * OFFSET)), 5)
    pg.draw.line(screen, DARK_GREEN, (NEW_X + OFFSET_II, GAMEBOARD_INSET), (NEW_X + OFFSET_II, HEIGHT - 100), 5)
    pg.draw.line(screen, DARK_GREEN, (GAMEBOARD_INSET + 15, NEW_Y + OFFSET_III), (WIDTH - 365, NEW_Y + OFFSET_III), 5)

    looper = 0
    for x in range(0, ARRAY_WIDTH):
        for y in range(0, ARRAY_HEIGHT):
            # print("count: {} x: {} y:{}".format(looper, x * GRID_SIZE, y * GRID_SIZE))
            looper = looper + 1
            tile_surface = game_font.render('{:02d}'.format(total[y][x]), False,
                                            (255, 255, 255))
            pg.draw.circle(screen, DARK_GRAY, (x * GRID_SIZE + OFFSET_II, y * GRID_SIZE + OFFSET_III), 24, 1)
            screen.blit(tile_surface, (x * GRID_SIZE + OFFSET_II - 10, y * GRID_SIZE + OFFSET_III - 12))
    pg.draw.circle(screen, DARK_GREEN, (NEW_X + GAMEBOARD_INSET_II, NEW_Y + GAMEBOARD_INSET), 35, 4)
    score_write = game_font.render('MOVE COUNT: {}'.format(move_count), False, (255, 255, 255))
    screen.blit(score_write, (WIDTH - 260, HEIGHT / 4))
    high_score_write = game_font.render('RECORD SCORE: {}'.format(best_score), False, (255, 255, 255))
    screen.blit(high_score_write, (WIDTH - 260, HEIGHT - HEIGHT / 6))
    title = title_font.render('TILE BREAKER', False, (255, 255, 255))
    screen.blit(title, (WIDTH - 260, HEIGHT / 12))
    completion_rate = game_font.render('COMPLETION RATE:', False, (255, 255, 255))
    screen.blit(completion_rate, (WIDTH - 260, HEIGHT / 3))
    time_counter = game_font.render('TIME:{:02d} {:02d} secs'.format(round(counting_minutes), round(counting_seconds)),
                                    False, (255, 255, 255))
    screen.blit(time_counter, (WIDTH - 260, HEIGHT - HEIGHT / 4))


background = pg.image.load('circuit.jpg').convert()
background_rect = background.get_rect()

best_score = get_high_score()
all_sprites = pg.sprite.Group()
pg.display.set_caption("Tile Break 2020")
clock = pg.time.Clock()
start_time = pg.time.get_ticks()

running = True
while running:
    rotate_counter = False
    rotate_clock = False
    pull_down = False
    pull_up = False
    pull_left = False
    pull_right = False

    clock.tick(FPS)
    counting_time = pg.time.get_ticks() - start_time
    game_time = counting_time / 1000
    counting_minutes = game_time / 120
    counting_seconds = game_time % 60

    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
        key_state = pg.key.get_pressed()
        if key_state[pg.K_LEFT]:
            FOCUS_X = focus_left(FOCUS_X, FOCUS_Y)

        elif key_state[pg.K_RIGHT]:
            FOCUS_X = focus_right(FOCUS_X, FOCUS_Y)

        elif key_state[pg.K_UP]:
            FOCUS_Y = focus_up(FOCUS_X, FOCUS_Y)

        elif key_state[pg.K_DOWN]:
            FOCUS_Y = focus_down(FOCUS_X, FOCUS_Y)

        elif key_state[pg.K_a or pg.K_A]:
            pull_left = True
            move_count = movecounter(move_count)
            count_it_up = total[FOCUS_Y].pop(0)
            total[FOCUS_Y].append(count_it_up)

        elif key_state[pg.K_d or pg.K_D]:
            pull_right = True
            move_count = movecounter(move_count)
            count_it_up = total[FOCUS_Y].pop(-1)
            total[FOCUS_Y].insert(0, count_it_up)

        elif key_state[pg.K_w or pg.K_W]:
            pull_up = True
            move_count = movecounter(move_count)
            vert_list = get_vert(FOCUS_X, FOCUS_Y)
            count_it_up = vert_list[FOCUS_X].pop(0)
            vert_list[FOCUS_X].append(count_it_up)
            horizontal_again = transcribe(vert_list)
            total = horizontal_again

        elif key_state[pg.K_s or pg.K_S]:
            pull_down = True
            move_count = movecounter(move_count)
            vert_list = get_vert(FOCUS_X, FOCUS_Y)
            count_it_up = vert_list[FOCUS_X].pop(-1)
            vert_list[FOCUS_X].insert(0, count_it_up)
            horizontal_again = transcribe(vert_list)
            total = horizontal_again


        elif key_state[pg.K_q or pg.K_Q]:
            start_x = FOCUS_X
            start_y = FOCUS_Y
            if start_x >= 1 and start_x <= ARRAY_WIDTH - 2 and start_y >= 1 and start_y <= ARRAY_HEIGHT - 2:
                rot_counterclock(total, FOCUS_X, FOCUS_Y, move_count)
                move_count = move_count + 1
                rotate_clock = True

        elif key_state[pg.K_e or pg.K_E]:
            start_x = FOCUS_X
            start_y = FOCUS_Y
            if start_x >= 1 and start_x <= ARRAY_WIDTH - 2 and start_y >= 1 and start_y <= ARRAY_HEIGHT - 2:
                rot_clock(total, FOCUS_X, FOCUS_Y, move_count)
                move_count = move_count + 1
                rotate_clock = True

        elif key_state[pg.K_m or pg.K_M]:
            solve(total)

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    if rotate_clock or rotate_counter == True:
        pg.draw.circle(screen, DARK_GREEN, (NEW_X + GAMEBOARD_INSET_II, NEW_Y + GAMEBOARD_INSET), 100, 25)
    if pull_left == True:
        pg.draw.line(screen, DARK_GREEN, (50, NEW_Y + GAMEBOARD_INSET),
                     (NEW_X + GAMEBOARD_INSET_II, NEW_Y + GAMEBOARD_INSET), 25)
    if pull_right == True:
        pg.draw.line(screen, DARK_GREEN, (NEW_X + GAMEBOARD_INSET + 15, NEW_Y + GAMEBOARD_INSET),
                     (WIDTH - 300, NEW_Y + GAMEBOARD_INSET), 25)
    if pull_up == True:
        pg.draw.line(screen, DARK_GREEN, (NEW_X + GAMEBOARD_INSET + 20, 50),
                     (NEW_X + GAMEBOARD_INSET + 20, NEW_Y + GAMEBOARD_INSET), 25)
    if pull_down == True:
        pg.draw.line(screen, DARK_GREEN, (NEW_X + GAMEBOARD_INSET + 20, NEW_Y + GAMEBOARD_INSET),
                     (NEW_X + GAMEBOARD_INSET + 20, HEIGHT - 50), 25)

    GRID_LOC_X = FOCUS_X * GRID_SIZE
    GRID_LOC_Y = FOCUS_Y * GRID_SIZE
    NEW_X = GRID_LOC_X
    NEW_Y = GRID_LOC_Ys

    if MASTER_ARRAY == total:
        if move_count < best_score:
            score_write = game_font.render('You set high score.'
                                           'the old best score was{} '
                                           'and now its {}'.format(best_score, move_count), False, (255, 255, 255))
            screen.blit(score_write, (WIDTH / 2, HEIGHT / 2))

            save_high_score(best_score, move_count)
            break
        else:
            score_write = game_font.render('Good game! {} is a decent score'.format(move_count), False, (255, 255, 255))
            screen.blit(score_write, (WIDTH / 2, HEIGHT / 2))

    health = health_bar()
    draw_health_bar(screen, WIDTH - 260, HEIGHT / 2.35, health)
    draw_elements()

    # *after* drawing everything, flip the display
    pg.display.flip()

pg.quit()
