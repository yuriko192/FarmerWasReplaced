import global_util
from __builtins__ import *


def Move():
    if get_pos_y() < 1:
        move(West)
    move(South)


def MoveBackward():
    if get_pos_y() == global_util.getWorldSize() - 1:
        move(East)
    move(North)


if __name__ == '__main__':
    Move()
