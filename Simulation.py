from __builtins__ import *

SpeedUp = 10
Seed = -1

Globals = {
    "Target": 1000000
}


def RunMaze():
    itemsDict = {
        Items.Weird_Substance: 100000
    }
    run_time = simulate("mazes", Unlocks, itemsDict, Globals, Seed, SpeedUp)
    return run_time


def RunPower():
    itemsDict = {
        Items.Carrot: 100000,
        Items.Water: 100000
    }
    run_time = simulate("Sunflower", Unlocks, itemsDict, Globals, Seed, SpeedUp)
    return run_time


def RunCactus():
    itemsDict = {
        Items.Pumpkin: 1000000,
        Items.Power: 100000
    }
    run_time = simulate("cactus", Unlocks, itemsDict, Globals, Seed, SpeedUp)
    return run_time


if __name__ == '__main__':
    runtime = RunCactus()
    quick_print("Runtime: ", runtime)
