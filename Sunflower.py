from __builtins__ import *
import cactus
import pumpkin
import harvest_util
import global_util

GridSize = global_util.getWorldSize()

directions = [South, West, North, East]
direction = 0
turnDirection = 1
targetIteration = 299
withUpdatePos = True


# < West East >
# ^ North
# v South

# 5
# 4
# 3
# 2
# 1
# 0 1 2 3 4 5




def RunSunFlower():
    clearGrid()
    PlantMaze()
    SmartSolver()
    harvest_util.Harvest()


if __name__ == '__main__':
    harvest()
    RunSunFlower()
    quick_print("Final Result : ", global_util.GetAllItemsTotal())
