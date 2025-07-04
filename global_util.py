from __builtins__ import *

USE_FERTILIZER = True

ITEM_LIST = [
    Items.Carrot,
    Items.Fertilizer,
    Items.Gold,
    Items.Hay,
    Items.Power,
    Items.Pumpkin,
    Items.Water,
    Items.Weird_Substance,
    Items.Wood,
    Items.Cactus,
    Items.Bone
]

def GetAllItemsTotal():
    result = {}
    for item in ITEM_LIST:
        result[item] =num_items(item)
    return result

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

def Move():
    if get_pos_y() < 1:
        move(West)
    move(South)


def MoveBackward():
    if get_pos_y() == getWorldSize() - 1:
        move(East)
    move(North)

def ClearGrid():
    posy = get_pos_y()
    posx = get_pos_x()
    while True:
        if get_entity_type() != Entities.Grass:
            harvest()
        Move()
        if get_pos_y() == posy and get_pos_x() == posx:
            break

worldSize = get_world_size()
worldGrid = CreateWorldGrid()
LastItem = Items.Hay