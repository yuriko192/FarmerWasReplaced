from __builtins__ import *

import movement_util
import harvest_util
import global_util

# < West East >
# ^ North
# v South

# 5
# 4
# 3
# 2
# 1
# 0 1 2 3 4 5

def harvestAndTill():
    entity = get_entity_type()
    if entity == None:
        return

    if get_entity_type() == Entities.Grass:
        till()
        return

    harvest()
    if get_ground_type() ==Grounds.Grassland:
        till()


def clearGrid():
    posy = get_pos_y()
    posx = get_pos_x()
    while True:
        harvestAndTill()
        movement_util.Move()
        if get_pos_y() == posy and get_pos_x() == posx:
            break

def moveToTarget(targetX, targetY):
    prevPosX,prevPosY = -1,-1
    posX, posY = global_util.GetPosition()
    while not (posX==targetX and posY==targetY):
        if prevPosX == posX and prevPosY == posY:
            return False
        prevPosX, prevPosY = posX, posY
        while posX > targetX:
            if not move(West):
                break
            posX-=1
        while posX < targetX:
            if not move(East):
                break
            posX += 1
        while posY > targetY:
            if not move(South):
                break
            posY-=1
        while posY < targetY:
            if not move(North):
                break
            posY += 1
    return True


def randomMove():
    if move(West):
        return True
    if move(East):
        return True
    if move(North):
        return True
    if move(South):
        return True
    return False


def RunSnake():
    clearGrid()
    change_hat(Hats.Dinosaur_Hat)
    nextX, nextY = measure()
    while True:
        if not randomMove():
            break
        if not moveToTarget(nextX, nextY):
            break
        nextX, nextY = measure()
    change_hat(Hats.Straw_Hat)
    return

if __name__ == '__main__':
    while True:
        change_hat(Hats.Straw_Hat)
        RunSnake()