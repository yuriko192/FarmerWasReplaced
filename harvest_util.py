from __builtins__ import *


def Water():
    if num_items(Items.Water) < 0:
        return
    if get_ground_type() == Grounds.Grassland:
        return
    if get_entity_type() == None:
        return

    if get_water() < 0.4:
        use_item(Items.Water, 1)
    pass


def Harvest():
    if get_entity_type()==Entities.Hedge:
        return

    if can_harvest():
        harvest()
    else:
        Water()
