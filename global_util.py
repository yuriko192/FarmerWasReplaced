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


worldSize = get_world_size()
worldGrid = CreateWorldGrid()
LastItem = Items.Hay