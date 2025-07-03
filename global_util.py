from __builtins__ import *

USE_FERTILIZER = True


def useFertilizer():
    if USE_FERTILIZER:
        use_item(Items.Fertilizer)


def getWorldGrid():
    return worldGrid


def getWorldSize():
    return worldSize


def CreateWorldGrid():
    newGrid = []
    for y in range(worldSize):
        innerGrid = []
        for x in range(worldSize):
            innerGrid.append(None)
        newGrid.append(innerGrid)
    return newGrid


def GetPosition():
    return get_pos_x(), get_pos_y()


worldSize = get_world_size()
worldGrid = CreateWorldGrid()
LastItem = Items.Hay