import global_util
from __builtins__ import *
import movement_util
import harvest_util

# < West East >
# ^ North
# v South

# 5
# 4
# 3
# 2
# 1
# 0 1 2 3 4 5

cactusGroundType = Grounds.Soil
cactus = Entities.Cactus
GridSize = global_util.getWorldSize()
cactusGrid = global_util.CreateWorldGrid()


def ClearGrid():
    posy = get_pos_y()
    posx = get_pos_x()
    while True:
        harvest_util.Harvest()
        movement_util.Move()
        if get_pos_y() == posy and get_pos_x() == posx:
            break


def PrepareGrid():
    posy = get_pos_y()
    posx = get_pos_x()
    cactusTotal = 0
    while True:
        movement_util.Move()
        currPossY = get_pos_y()
        currPossX = get_pos_x()
        currentEntity = get_entity_type()

        if currentEntity == cactus:
            cactusTotal += 1
            cactusGrid[currPossY][currPossX] = measure()
            if cactusTotal == GridSize ** 2:
                break
            continue

        if currentEntity != None:
            harvest_util.harvest()

        if get_ground_type() != cactusGroundType:
            till()
        plant(cactus)
        cactusGrid[currPossY][currPossX] = measure()


def MoveToStart():
    while get_pos_y() != 0:
        move(North)
    while get_pos_x() != 0:
        move(West)


def sortColumn():
    while get_pos_y() != 0:
        move(South)
    while get_pos_y() != GridSize - 1:
        move(North)
        while get_pos_y() > 0 and measure(South) > measure():
            swap(South)
            move(South)


def sortRow():
    while get_pos_x() != 0:
        move(West)
    while get_pos_x() != GridSize - 1:
        move(East)
        while get_pos_x() > 0 and measure(West) > measure():
            swap(West)
            move(West)
    pass


def SortGrid():
    for i in range(GridSize):
        sortColumn()
        move(East)
    for i in range(GridSize):
        sortRow()
        move(North)


def PlantCactus():
    PrepareGrid()
    MoveToStart()
    SortGrid()
    harvest_util.Harvest()


if __name__ == '__main__':
    while True:
        PlantCactus()
