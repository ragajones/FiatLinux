import random

WIDTH, HEIGHT = 800, 500
OFFSET, OFFSET_II, OFFSET_III = 50, 120, 100
TITLE = "Tile Breaker 2020"
GAMEBOARD_WIDTH, GAMEBOARD_HEIGHT, GAMEBOARD_INSET, GAMEBOARD_INSET_II = 400, 400, 100, 120
ARRAY_WIDTH, ARRAY_HEIGHT = 5, 5
ARRAY_LENGTH = ARRAY_WIDTH * ARRAY_HEIGHT
GRID_SIZE = int((HEIGHT - (OFFSET_II)) / ARRAY_WIDTH)
FOCUS_X, FOCUS_Y = 0, 0
FPS = 60
BUTTON_SIZE = 40
TILE_SIZE = 100

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 122)
DARK_GRAY = (50, 50, 50)
DARK_GREEN = (0, 50, 0)
BGCOLOR = (40, 40, 40)

EMPTY_LIST_I = []
EMPTY_LIST_II = []
MASTER_LIST = []
MASTER_ARRAY = []
SHUFFLED_LIST = []
SHUFFLED_ARRAY = []
NEG_DELTA = []

DELTAS_LIST = []
HORIZONTAL_LIST = []
total = []

move_count = 0
best_score = 0
best_time = 0
game_loop = False

# LISTS SETUP:
# STEP ONE:
# creates SHUFFLE LIST and shuffles it.
# since 'pop' is used; list gets copied into EMPTY LIST to preserve data
for array_length in range(ARRAY_LENGTH):
    MASTER_LIST.append(array_length)
    SHUFFLED_LIST.append(array_length)
random.shuffle(SHUFFLED_LIST)
EMPTY_LIST_I = SHUFFLED_LIST.copy()
EMPTY_LIST_II = MASTER_LIST.copy()
# STEP TWO - Copies SHUFFLE LIST into SHUFFLE ARRAY
for array_width in range(ARRAY_WIDTH):
    SHUFFLED_ARRAY.append([])
    MASTER_ARRAY.append([])
    for array_height in range(ARRAY_HEIGHT):
        pop_array = SHUFFLED_LIST.pop(0)
        pop_array2 = MASTER_LIST.pop(0)
        SHUFFLED_ARRAY[array_width].append(pop_array)
        MASTER_ARRAY[array_width].append(pop_array2)
SHUFFLED_LIST = EMPTY_LIST_I.copy()
MASTER_LIST = EMPTY_LIST_II.copy()
# STEP THREE: sets up Delta between master list index and shuffle list index
for x in range(ARRAY_LENGTH):
    nums = abs(
        x - SHUFFLED_LIST[x])
    DELTAS_LIST.append(nums)
total = SHUFFLED_ARRAY.copy()
for x in range(ARRAY_LENGTH - 1, 0, -1):
    nums = abs(
        x - SHUFFLED_LIST[x])
    NEG_DELTA.append(nums)

print(SHUFFLED_ARRAY[0])
print(SHUFFLED_ARRAY[1])
print(SHUFFLED_ARRAY[2])
print(SHUFFLED_ARRAY[3])
print(SHUFFLED_ARRAY[4])
print('')
for i in range(ARRAY_WIDTH):
    START_X = 2
    START_Y = 2
    VERT_DISPLACE = 0
    HORZ_DISPLACE = 0
    TOTAL_DISPLACE = VERT_DISPLACE + HORZ_DISPLACE
    GATHERING_LIST = []
    if MASTER_ARRAY[0][0] in SHUFFLED_ARRAY[START_Y]:  # Its in the starting middle row
        if SHUFFLED_ARRAY[START_Y][START_X + HORZ_DISPLACE] == MASTER_ARRAY[0][
            0]:  # check to see if it is in the middle middle
            pass
        else:
            HORZ_DISPLACE = HORZ_DISPLACE + 1  # move to middle row 2 indexes 1 and 3
            if SHUFFLED_ARRAY[START_Y][START_X + HORZ_DISPLACE] == MASTER_ARRAY[0][0] or \
                    SHUFFLED_ARRAY[START_Y][START_X - HORZ_DISPLACE] == MASTER_ARRAY[0][0]:
                pass
            else:
                HORZ_DISPLACE = HORZ_DISPLACE + 1
                pass

    elif MASTER_ARRAY[0][0] in SHUFFLED_ARRAY[START_Y + 1] or MASTER_ARRAY[0][0] in SHUFFLED_ARRAY[
        START_Y - 1]:
        VERT_DISPLACE = VERT_DISPLACE + 1
        if SHUFFLED_ARRAY[START_Y + 1][START_X] == MASTER_ARRAY[0][0] or SHUFFLED_ARRAY[START_Y - 1][START_X] == \
                MASTER_ARRAY[0][0]:
            pass
        elif SHUFFLED_ARRAY[START_Y + 1][START_X + 1] == MASTER_ARRAY[0][0] or \
                SHUFFLED_ARRAY[START_Y + 1][START_X - 1] == MASTER_ARRAY[0][0] or \
                SHUFFLED_ARRAY[START_Y - 1][START_X + 1] == MASTER_ARRAY[0][0] or \
                SHUFFLED_ARRAY[START_Y - 1][START_X - 1] == MASTER_ARRAY[0][0]:
            HORZ_DISPLACE = HORZ_DISPLACE + 1
            pass

        else:
            HORZ_DISPLACE = HORZ_DISPLACE + 2
            pass



    elif MASTER_ARRAY[0][0] in SHUFFLED_ARRAY[START_Y + 2] or MASTER_ARRAY[0][0] in SHUFFLED_ARRAY[
        START_Y - 2]:
        VERT_DISPLACE = VERT_DISPLACE + 2

        if SHUFFLED_ARRAY[START_Y + 2][START_X] == MASTER_ARRAY[0][
            0] or SHUFFLED_ARRAY[START_Y - 2][START_X] == MASTER_ARRAY[0][
            0]:
            pass

        elif SHUFFLED_ARRAY[START_Y + 2][START_X + 1] == MASTER_ARRAY[0][0] or \
                SHUFFLED_ARRAY[START_Y + 2][START_X - 1] == MASTER_ARRAY[0][0] or \
                SHUFFLED_ARRAY[START_Y - 2][START_X + 1] == MASTER_ARRAY[0][0] or \
                SHUFFLED_ARRAY[START_Y - 2][START_X - 1] == MASTER_ARRAY[0][0]:
            pass

            HORZ_DISPLACE = HORZ_DISPLACE + 1
        else:
            pass
            HORZ_DISPLACE = HORZ_DISPLACE + 2
    TOTAL_DISPLACE = VERT_DISPLACE + HORZ_DISPLACE
    print('vert: {}'.format(VERT_DISPLACE))
    print('horz: {}'.format(HORZ_DISPLACE))
    print('tot: {} '.format(TOTAL_DISPLACE))
    print(SHUFFLED_ARRAY[0])
    print(SHUFFLED_ARRAY[1])
    print(SHUFFLED_ARRAY[2])
    print(SHUFFLED_ARRAY[3])
    print(SHUFFLED_ARRAY[4])
    print('')
    GATHERING_LIST.append(TOTAL_DISPLACE)
    print(GATHERING_LIST)
    for i in range(ARRAY_WIDTH):
        numeros = SHUFFLED_ARRAY[i].pop(-1)
        SHUFFLED_ARRAY[i].insert(0, numeros)
