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
    worldGrid = []
    for y in range(worldSize):
        innerWorldGrid = []
        for x in range(worldSize):
            innerWorldGrid.append(None)
        worldGrid.append(innerWorldGrid)
    return worldGrid


def GetPosition():
    return get_pos_x(), get_pos_y()


worldSize = get_world_size()
worldGrid = CreateWorldGrid()
