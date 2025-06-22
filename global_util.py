from __builtins__ import *

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

worldSize = get_world_size()
worldGrid = CreateWorldGrid()