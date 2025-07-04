from __builtins__ import *


itemsDict = {
    Items.Weird_Substance: 100000
}
run_time = simulate("mazes", Unlocks, itemsDict, {},-1,100 )
quick_print("Runtime: ", run_time)