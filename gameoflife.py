# Game Of Life in Python 

import random
import numpy as np

# Initializes the board, with each cell randomly set to either DEAD (0) or ALIVE (1)
def random_state(rows, columns):
    state = np.full((rows, columns), -1, dtype=int)
    
    # Sets a random value of each cell in the 2D array
    for i in range(rows):
        for j in range(columns):
            status = random.randint(0, 1)
            state[i][j] = status
 
    return state

# Returns the next state of the board after one life cycle has passed.
def next_board_state(state):
    rows = state.shape[0]
    columns = state.shape[1]
    new_state = dead_state(rows, columns)
    
    # RULES: 
    # A cell can have up to 4 valid neighbors. Diagonals are not supported at the moment.
    # Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
    # Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
    # Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
    # Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
    for i in range(rows):
        for j in range(columns):
            numNeighbors = findLiveNeighbors(state, i, j)
            if state[i][j] == 0: # DEAD cell
                if numNeighbors == 3:
                    new_state[i][j] = 1
            else: # LIVE cell
                if numNeighbors == 0 or numNeighbors == 1:
                    new_state[i][j] = 0 
                elif numNeighbors == 2 or numNeighbors == 3:
                    new_state[i][j] = 1
                else:
                    new_state[i][j] = 0
    return new_state


# Helper function for next_board_state. Returns the number of live neighbors a cell has, given the state of the board and the cell's position.
def findLiveNeighbors(state, rowNo, colNo):
    neighbors = 0
    rows = state.shape[0]
    columns = state.shape[1]
    
    # Brute-force neighbor checking. There is an alternate way of doing this by first classifying corner, edge and interior cells.

    # check up
    if rowNo != 0:
        if state[rowNo-1][colNo] == 1:
            neighbors += 1
    
    # check left
    if colNo != 0:
        if state[rowNo][colNo-1] == 1:
            neighbors += 1
    
    # check right 
    if colNo != columns - 1:
        if state[rowNo][colNo+1] == 1:
            neighbors += 1
    
    # check down
    if rowNo != rows - 1:
        if state[rowNo+1][colNo] == 1:
            neighbors += 1
    
    # check top-left
    if rowNo != 0 and colNo != 0:
        if state[rowNo-1][colNo-1] == 1:
            neighbors += 1

    # check top-right
    if rowNo != 0 and colNo != columns - 1:
        if state[rowNo-1][colNo+1] == 1:
            neighbors += 1
    
    # check bottom-left
    if rowNo != rows - 1 and colNo != 0:
        if state[rowNo+1][colNo-1] == 1:
            neighbors += 1
    
    # check bottom-right
    if rowNo != rows-1 and colNo != columns-1:
        if state[rowNo+1][colNo+1] == 1:
            neighbors += 1

    return neighbors

# Helper function. Initializes a board with all cells set to DEAD (0).
def dead_state(rows, columns):
    state = np.full((rows, columns), 0, dtype=int)
    return state     

# Helper function for debugging. Displays the grid in an easy-to-read format.
def render(grid):
    rows = grid.shape[0]
    columns = grid.shape[1]
    currentRow = "|"
    for i in range(rows):
        for j in range(columns):
            currentRow = currentRow + "  " + str(grid[i][j])
        print(currentRow + "  |")
        currentRow = "|"

# Driver code of the program
def main():
    # At the moment, I made it so that the interface only allows users to make nxn grids. However, the code is usable for any number of rows and columns.
    
    # Startup code
    print("Welcome to the Game Of Life!")
    size = int(input("Please enter a number: "))
    initialState = random_state(size, size)
    print("Here is the initial state of your game!")
    render(initialState)
    
    # Main code
    currentState = initialState
    numCycles = 0
    while True:
        print("Number of cycles: " + str(numCycles))
        next = input("Would you like to keep going? (Y/N) ")
        if next == "Y":
            numCycles += 1
            next_state = next_board_state(currentState)
            render(next_state)
            currentState = next_state           
        elif next == "N":
            break
        else:
            print("Sorry, that wasn't a valid response. Please try again.")    

main()
