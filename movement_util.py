from __builtins__ import *


def Move():
    if get_pos_y() < 1:
        move(West)
    move(South)

if __name__ == '__main__':
       run_tasks()