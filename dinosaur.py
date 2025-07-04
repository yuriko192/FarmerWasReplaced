from __builtins__ import *

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

TailSize = 1
GridSize = global_util.getWorldSize()
GridMovementPattern = None
Target = global_util.TARGET


def harvestAndTill():
    entity = get_entity_type()
    if entity == None:
        return

    if get_entity_type() == Entities.Grass:
        till()
        return

    harvest()
    if get_ground_type() == Grounds.Grassland:
        till()


def clearGrid():
    posy = get_pos_y()
    posx = get_pos_x()
    while True:
        harvestAndTill()
        global_util.Move()
        if get_pos_y() == posy and get_pos_x() == posx:
            break


def moveToTarget(targetX, targetY):
    prevPosX, prevPosY = -1, -1
    posX, posY = global_util.GetPosition()
    while not (posX == targetX and posY == targetY):
        if prevPosX == posX and prevPosY == posY:
            return False
        prevPosX, prevPosY = posX, posY
        while posX > targetX:
            if not move(West):
                break
            posX -= 1
        while posX < targetX:
            if not move(East):
                break
            posX += 1
        while posY > targetY:
            if not move(South):
                break
            posY -= 1
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


def createMovementGrid():
    global GridMovementPattern
    GridMovementPattern = global_util.CreateWorldGrid()
    for y in range(GridSize):
        for x in range(GridSize):
            if y == 0:
                GridMovementPattern[y][x] = West
                continue
            if x % 2 == 0:
                if y == GridSize - 1:
                    GridMovementPattern[y][x] = East
                    continue
                GridMovementPattern[y][x] = North
            else:
                if y == 1:
                    GridMovementPattern[y][x] = East
                    continue
                GridMovementPattern[y][x] = South
    x = GridSize - 1
    for y in range(1, GridSize):
        GridMovementPattern[y][x] = South
    GridMovementPattern[0][0] = North


def getNextLoopMove(nextX, nextY):
    global GridMovementPattern
    posX, posY = global_util.GetPosition()
    nextMove = GridMovementPattern[posY][posX]
    if GridSize % 2 == 1:
        # enable skip
        if nextX == GridSize - 1 and posX == GridSize - 2 and posY == GridSize - 1:
            nextMove = East
    return nextMove


def RunSnake():
    global TailSize
    clearGrid()
    change_hat(Hats.Dinosaur_Hat)
    nextX, nextY = measure()
    TailSize = 1
    createMovementGrid()
    while True:
        result = measure()
        if result != None:
            nextX, nextY = result
            TailSize += 1
            if TailSize == GridSize ** 2:
                break
        if TailSize > GridSize * 2 and move(getNextLoopMove(nextX, nextY)):
            continue
            # if not moveLoop(nextX, nextY):
            #     break
        if moveToTarget(nextX, nextY):
            continue
        if move(getNextLoopMove(nextX, nextY)):
            continue
        if randomMove():
            continue
        break

    change_hat(Hats.Straw_Hat)
    return


if __name__ == '__main__':
    change_hat(Hats.Straw_Hat)
    while num_items(Items.Bone) < Target:
        RunSnake()
    quick_print("Final Result : ", global_util.GetAllItemsTotal())
