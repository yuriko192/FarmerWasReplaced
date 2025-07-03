from __builtins__ import *
import cactus
import pumpkin
import movement_util
import harvest_util
import global_util

GridSize = global_util.getWorldSize()

directions = [South, West, North, East]
direction = 0
turnDirection = 1
targetIteration = 30


# < West East >
# ^ North
# v South

# 5
# 4
# 3
# 2
# 1
# 0 1 2 3 4 5

def UseWeirdSubstance():
    use_item(Items.Weird_Substance, GridSize * num_unlocked(Unlocks.Mazes))


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
    if global_util.LastItem == Items.Wood or global_util.LastItem == Items.Carrot:
        clearGrid()
    plant(Entities.Bush)
    UseWeirdSubstance()


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


def getNextValidMove():
    global direction

    # RIGHT
    direction = (direction + 1) % 4
    if move(directions[direction]):
        return direction

    # UP
    direction = (direction - 1) % 4
    if move(directions[direction]):
        return direction

    # LEFT
    direction = (direction - 1) % 4
    if move(directions[direction]):
        return direction

    # DOWN
    direction = (direction - 1) % 4
    if move(directions[direction]):
        return direction


def getNextNode(startX, startY, possibleDirection):
    if possibleDirection == 0:
        return startX, startY - 1
    if possibleDirection == 1:
        return startX - 1, startY
    if possibleDirection == 2:
        return startX, startY + 1
    return startX + 1, startY


def getDirection(previousX, previousY, currX, currY):
    if previousX < currX:
        return East
    if previousX > currX:
        return West
    if previousY < currY:
        return North
    return South


def moveToTarget(mazeGrid, targetX, targetY):
    startX, startY = global_util.GetPosition()
    if startX == targetX and startY == targetY:
        return

    visitedGrid = global_util.CreateWorldGrid()  # (visitedFrom, weight)
    reachableNode = []  # (prevPos, nextPos, distance )
    currDistance = 0

    def AddPositionToReachableNode(posX, posY, distance):
        for possibleDirection in mazeGrid[posY][posX]:
            nextX, nextY = getNextNode(posX, posY, possibleDirection)  # Get Neighbour
            if visitedGrid[nextY][nextX] == None:
                # quick_print("adding ", ((posY, posX), (nextY, nextX), distance))
                reachableNode.append(((posY, posX), (nextY, nextX), distance))
            # else:
                # quick_print("skipping ", ((posY, posX), (nextY, nextX), distance))

    currX, currY = startX, startY
    visitedGrid[currY][currX] = [(currY, currX), 0]
    AddPositionToReachableNode(startX, startY, currDistance + 1)

    # Find Target
    # quick_print("starting ", startY, startX)
    while len(reachableNode) > 0:
        # Update Position
        # quick_print("")
        # quick_print("reachableNode State", reachableNode)
        (currY, currX), (nextY, nextX), nodeDistance = reachableNode.pop(0)
        # quick_print("Possible From", (currY, currX), (nextY, nextX))
        visitedGrid[nextY][nextX] = [(currY,currX), nodeDistance]
        # quick_print("Grid State ", visitedGrid)
        currDistance = nodeDistance
        currX, currY = nextX, nextY

        # Found
        if currX == targetX and currY == targetY:
            break

        AddPositionToReachableNode(currX, currY, currDistance + 1)

    # Backtrace
    moves = []
    # quick_print("Checking From ", currY, currX)
    while not (currX == startX and currY == startY):
        (previousY, previousX ), _ = visitedGrid[currY][currX]
        # quick_print("Moving From", previousY, previousX, "To", currY, currX)
        moves.append(getDirection(previousX, previousY, currX, currY))
        currX, currY = previousX, previousY


    quick_print("moves: ", moves)
    for moveDirection in moves[::-1]:
        move(moveDirection)
    pass


def SmartSolver():
    global direction
    startX, startY = global_util.GetPosition()
    targetX, targetY = -1, -1
    nextX, nextY = -1, -1
    grid = global_util.CreateWorldGrid()
    visitedNode = 0
    # Create Grid
    posX, posY = startX, startY
    while True:
        if get_entity_type() == Entities.Treasure:
            targetX, targetY = global_util.GetPosition()
            nextX, nextY = measure()
            # quick_print("Found Target")
            # quick_print("target X: ", targetX, ", target Y: ", targetY)
            # quick_print("next X: ", nextX, ", nextX Y: ", nextY)

        nextMove = getNextValidMove()
        if grid[posY][posX] == None:
            grid[posY][posX] = []
            visitedNode += 1
        grid[posY][posX].append(nextMove)

        posX, posY = global_util.GetPosition()
        # if posX ==0 and posY == 0:
        #     return
        if visitedNode == GridSize ** 2 and posX == startX and posY == startY:
            break

    quick_print("Result Grid")
    quick_print(grid)
    for i in range(targetIteration):
        moveToTarget(grid, targetX, targetY)
        nextX, nextY = measure()
        targetX, targetY = nextX, nextY
        UseWeirdSubstance()
    moveToTarget(grid, targetX, targetY)
    harvest()


def RunMaze():
    PlantMaze()
    SmartSolver()
    harvest_util.Harvest()


if __name__ == '__main__':
    # RunMaze()
    harvest()
