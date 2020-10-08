def create():
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def first_player_move(field, x, y):
    if not field[x][y]:
        field[x][y] = 1
        return f"Player 1 successfully placed X on (x, y)"
    if field[x][y]:
        return f"You can't place X there."


def second_player_move(field, x, y):
    if not field[x][y]:
        field[x][y] = 2
        return f"Player 1 successfully placed O on (x, y)"
    if field[x][y]:
        return f"You can't place O there."


def check_endgame(field):
    if (field[0], field[1], field[2]) == (1, 1, 1) or (field[3], field[4], field[5]) == (1, 1, 1) or (field[6], field[7], field[8]) == (1, 1, 1)\
        or (field[0], field[3], field[6]) == (1, 1, 1) or (field[1], field[4], field[7]) == (1, 1, 1) or (field[2], field[5], field[8]) == (1, 1, 1) \
            or (field[0], field[4], field[8]) == (1, 1, 1) or (field[2], field[4], field[6]) == (1, 1, 1):
        return 1
    elif (field[0], field[1], field[2]) == (2, 2, 2) or (field[3], field[4], field[5]) == (2, 2, 2) or (field[6], field[7], field[8]) == (2, 2, 2)\
        or (field[0], field[3], field[6]) == (2, 2, 2) or (field[1], field[4], field[7]) == (2, 2, 2) or (field[2], field[5], field[8]) == (2, 2, 2) \
            or (field[0], field[4], field[8]) == (2, 2, 2) or (field[2], field[4], field[6]) == (2, 2, 2):
        return 2
    elif not field[0].count(0) and not not field[1].count(0) and not not field[2].count(0):
        return 3
    else:
        return 0