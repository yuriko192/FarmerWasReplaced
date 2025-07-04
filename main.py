import Sunflower
from __builtins__ import *

import mazes
import cactus
import pumpkin
import dinosaur
import harvest_util
import global_util

SIZE = "size"
GRID = "grid"
PLAYER = "player"
X = "x"
Y = "y"


# DefaultPlant = (Items.Hay, Grounds.Grassland, None)
DefaultPlant = (Items.Wood, Grounds.Soil, Entities.Tree)

plantables = [
    # (Items.Hay, Grounds.Grassland, None),
    (Items.Power, Grounds.Soil, Entities.Sunflower),
    (Items.Wood, Grounds.Soil, Entities.Tree),
    # (Items.Carrot, Grounds.Soil, Entities.Carrot),
    # (Items.Pumpkin, Grounds.Soil, Entities.Pumpkin),
    # (Items.Cactus, Grounds.Soil, Entities.Cactus),
    # (Items.Weird_Substance, Grounds.Soil, Entities.Cactus),
    # (Items.Gold, Grounds.Soil, Entities.Bush),
    # (Items.Bone, Grounds.Soil, Entities.Bush),
]

world = {
    SIZE: get_world_size(),
    GRID: [],
    PLAYER: {
        X: 0,
        Y: 0
    },
}
for y in range(world[SIZE]):
    innerWorldGrid = []
    for x in range(world[SIZE]):
        innerWorldGrid.append(None)
    world[GRID].append(innerWorldGrid)


def GetGroundType(item):
    if item != Items.Hay:
        return Grounds.Grassland
    return Grounds.Soil


def GetSeed(item):
    if item == Items.Hay:
        return None

    if item == Items.Wood:
        return Entities.Bush

    if item == Items.Carrot:
        return Entities.Carrot

    if item == Items.Pumpkin:
        return Entities.Pumpkin


def PrepareGround(groundType):
    currentGround = get_ground_type()
    if currentGround != groundType:
        till()


def GetNextPlantables():
    pickedItem, pickedGroundType, pickedSeed = DefaultPlant
    pickedI = -1

    i = -1
    for item, groundType, seed in plantables:
        numItems = num_items(item)
        if item == Items.Weird_Substance or item == Items.Power:
            numItems*=100
        i += 1
        if numItems < num_items(pickedItem):
            pickedI = i
            pickedItem, pickedGroundType, pickedSeed = item, groundType, seed
    return pickedI, pickedItem, pickedGroundType, pickedSeed


def PlantSeed():
    pickedI, pickedItem, pickedGroundType, pickedSeed = GetNextPlantables()

    if pickedItem == Items.Power:
        Sunflower.RunSunFlower()
        global_util.LastItem = pickedItem
        return

    if pickedItem == Items.Weird_Substance:
        global_util.USE_FERTILIZER = True
    else:
        global_util.USE_FERTILIZER = False

    if pickedItem == Items.Gold:
        mazes.RunMaze()
        global_util.LastItem = pickedItem
        return

    if pickedItem == Items.Bone:
        dinosaur.RunSnake()
        global_util.LastItem = pickedItem
        return

    PrepareGround(pickedGroundType)

    if pickedSeed == None:
        return

    if pickedSeed == Entities.Tree:
        if (get_pos_y() + get_pos_x()) % 2 == 0:
            plant(Entities.Tree)
            harvest_util.Water()
        else:
            plant(Entities.Bush)
        global_util.LastItem = pickedItem
        return

    if pickedSeed == Entities.Pumpkin:
        pumpkin.PlantPumpkin()
        global_util.LastItem = pickedItem
        return

    if pickedSeed == Entities.Cactus:
        cactus.PlantCactus()
        global_util.LastItem = pickedItem
        return

    plant(pickedSeed)
    global_util.useFertilizer()
    global_util.LastItem = pickedItem


def UpdateWorldGrid():
    y = world[PLAYER][Y]
    x = world[PLAYER][X]
    world[GRID][y][x] = get_entity_type()


def UpdatePosition():
    world[PLAYER][Y] = get_pos_y()
    world[PLAYER][X] = get_pos_x()


while True:
    UpdatePosition()
    harvest_util.Harvest()
    PlantSeed()
    UpdateWorldGrid()
    global_util.Move()
