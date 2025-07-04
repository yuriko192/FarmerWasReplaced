from __builtins__ import *
import cactus
import pumpkin
import harvest_util
import global_util
from global_util import MoveTo

GridSize = global_util.getWorldSize()
sunflowerGroundType = Grounds.Soil
sunflower = Entities.Sunflower
WorldGrid = global_util.CreateWorldGrid()
WorldDict = dict()
Target = global_util.TARGET


# < West East >
# ^ North
# v South

# 5
# 4
# 3
# 2
# 1
# 0 1 2 3 4 5

def MeasurePosition():
    currPosX, currPosY = global_util.GetPosition()
    currentWeight = measure()
    WorldGrid[currPosY][currPosX] = currentWeight
    if currentWeight not in WorldDict:
        WorldDict[currentWeight] = []
    WorldDict[currentWeight].append((currPosY, currPosX))


def PrepareGrid():
    startX, startY = global_util.GetPosition()
    while (True):
        if get_ground_type() != sunflowerGroundType:
            till()
        currentEntity = get_entity_type()
        if currentEntity != sunflower:
            if currentEntity != None:
                harvest()
            plant(sunflower)
            harvest_util.Water()

        MeasurePosition()
        global_util.Move()
        if get_pos_x() == startX and get_pos_y() == startY:
            return
    return


def HarvestSunflowerWithChecks():
    for i in range(15, 6, -1):
        if i not in WorldDict:
            continue

        arr = WorldDict[i]
        while len(arr) > 0:
            j = 0
            for x in arr:
                targetY, targetX = arr[j]
                MoveTo(targetX, targetY)
                if harvest_util.Harvest():
                    arr.pop(j)
                    break
                j += 1


def HarvestSunflower():
    for i in range(15, 6, -1):
        if i not in WorldDict:
            continue

        arr = WorldDict[i]
        while len(arr) > 0:
            targetY, targetX = arr.pop()
            MoveTo(targetX, targetY)
            harvest()


def RunSunFlower():
    PrepareGrid()
    # quick_print("WorldGrid: ", WorldGrid)
    # quick_print("WorldDict: ", WorldDict)
    HarvestSunflowerWithChecks()


if __name__ == '__main__':
    while num_items(Items.Power) < Target:
        RunSunFlower()
    quick_print("Final Result : ", global_util.GetAllItemsTotal())
