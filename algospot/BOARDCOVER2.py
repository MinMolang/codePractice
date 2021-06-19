
# 2
# 4 7 2 3
# ##.##..
# #......
# #....##
# #..####
# ###
# #..
# 5 10 3 3
# ..........
# ..........
# ..........
# ..........
# ..........
# .#.
# ###
# ..#


# 3
# 8

# code ref. hunu's code
def set_block(y, x, rot):
    for dy, dx in rot:
        if not (0 <= y + dy < H) or not (0 <= x + dx < W) or board[y + dy][x + dx]:
            return False

    for dy, dx in rot:
        board[y + dy][x + dx] = True
    return True


def unset_block(y, x, rot):
    for dy, dx in rot:
        board[y + dy][x + dx] = False
    return False


def search(num_blocks, num_white):
    global best, block_size

    # best case
    if (num_white // block_size) + num_blocks <= best:
        return

    # find position to set
    for y in xrange(H):
        for x in xrange(W):
            if not board[y][x]:
                break
        else:
            continue
        break
    else:
        best = max(best, num_blocks)
        return

    for rot in rotations:
        if set_block(y, x, rot):
            search(num_blocks + 1, num_white - block_size)
            unset_block(y, x, rot)

    board[y][x] = True
    search(num_blocks, num_white - 1)
    board[y][x] = False
    return


def rotate_block(block):
    return zip(*reversed(block))
    #[(True, True), (False, True), (False, True)]
    #[(False, False, True), (True, True, True)]
    #[(True, False), (True, False), (True, True)]

    #[(False, True, False), (False, True, True), (True, True, False)]
    #[(True, False, False), (True, True, True), (False, True, False)]
    #[(False, True, True), (True, True, False), (False, True, False)]


def binarize(x):
    return x == '#'


for _ in xrange(input()):
    H, W, R, C = map(int, raw_input().split())
    board = [map(binarize, raw_input()) for _ in xrange(H)] #[[True, True, False, True, True, False, False], [True, False, False, False, False, False, False],
    block = tuple(map(binarize, raw_input()) for _ in xrange(R)) # ([True, True, True], [True, False, False])

    # rotations
    rotations = []
    for _ in xrange(4):
        rotation = []
        origin_x = origin_y = None
        for h, row in enumerate(block):
            for w, cell in enumerate(row):
                if cell and origin_x is None:
                    origin_y, origin_x = h, w
                    rotation.append((0, 0))
                elif cell:
                    rotation.append((h - origin_y, w - origin_x))
        if rotation not in rotations:
            rotations.append(rotation)
        block = rotate_block(block)

    best = 0
    num_white = H * W - sum(sum(row) for row in board) #15 len of '.'
    block_size = len(rotations[0])

    search(0, num_white)
    print(best)
