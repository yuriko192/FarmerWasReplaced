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

pumpkinGroundType = Grounds.Soil
pumpkin = Entities.Pumpkin
GridSize = global_util.getWorldSize()

def PlantPumpkin():
    harvestablePumpkinTotal = 0
    while True:
        currentEntity = get_entity_type()
        if currentEntity == None:
            if get_ground_type() != pumpkinGroundType:
                till()
            plant(pumpkin)
            movement_util.Move()
            harvestablePumpkinTotal = 0
            continue
        if currentEntity == pumpkin:
            if harvestablePumpkinTotal == (GridSize * 3):
                harvest_util.Harvest()
                break
            if can_harvest():
                harvestablePumpkinTotal += 1
            else:
                harvest_util.Water()
            movement_util.Move()
            continue
        harvest_util.Harvest()
        if get_ground_type() != pumpkinGroundType:
            till()
        plant(pumpkin)
        global_util.useFertilizer()
        movement_util.Move()

if __name__ == "__main__":
    while True:
        PlantPumpkin()
