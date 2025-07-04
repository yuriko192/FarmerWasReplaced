import global_util
from __builtins__ import *
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
Target = global_util.TARGET


def PlantPumpkin():
    harvestablePumpkinTotal = 0
    while True:
        currentEntity = get_entity_type()
        if currentEntity == pumpkin:
            if harvestablePumpkinTotal == (GridSize ** 2):
                harvest_util.Harvest()
                break
            if can_harvest():
                harvestablePumpkinTotal += 1
            else:
                harvest_util.Water()
            global_util.Move()

        else:
            if currentEntity != None:
                harvest()
            if get_ground_type() != pumpkinGroundType:
                till()
            plant(pumpkin)
            harvestablePumpkinTotal = 0
            global_util.Move()


if __name__ == "__main__":
    while num_items(Items.Pumpkin) < Target:
        PlantPumpkin()
    quick_print("Final Result : ", global_util.GetAllItemsTotal())
