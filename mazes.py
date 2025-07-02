from __builtins__ import *
import cactus
import pumpkin
import movement_util
import harvest_util
import global_util

GridSize = global_util.getWorldSize()
unlockLevel = 2  # num_unlocked(Unlocks.Mazes)

directions = [South, West, North, East]
direction = 0
turnDirection = 1


# < West East >
# ^ North
# v South

# 5
# 4
# 3
# 2
# 1
# 0 1 2 3 4 5

isClearGrid = False


def clearGrid():
    posy = get_pos_y()
    posx = get_pos_x()
    while True:
        if get_entity_type() != Entities.Grass:
            harvest_util.Harvest()
        movement_util.Move()
        if get_pos_y() == posy and get_pos_x() == posx:
            break


def PlantMaze():
    if isClearGrid:
        clearGrid()
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, GridSize * unlockLevel)


def HugRightWallSolver():
    global direction
    while get_entity_type() != Entities.Treasure:
        direction = (direction + 1) % 4
        if not move(directions[direction]):
            direction = (direction - 1) % 4
            if not move(directions[direction]):
                direction = (direction - 1) % 4
                if not move(directions[direction]):
                    direction = (direction - 1) % 4


def RunMaze():
    if get_entity_type() != Entities.Hedge:
        PlantMaze()
    HugRightWallSolver()
    harvest_util.Harvest()


if __name__ == '__main__':
    RunMaze()
