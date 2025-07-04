from __builtins__ import *

SpeedUp = 10
Seed = -1

def RunMaze():
    itemsDict = {
        Items.Weird_Substance: 100000
    }
    run_time = simulate("mazes", Unlocks, itemsDict, {}, Seed, SpeedUp)
    return run_time


def RunPower():
    itemsDict = {
        Items.Carrot: 100000,
        Items.Water: 100000
    }
    run_time = simulate("Sunflower", Unlocks, itemsDict, {}, Seed, SpeedUp)
    return run_time


if __name__ == '__main__':
    runtime = RunPower()
    quick_print("Runtime: ", runtime)
