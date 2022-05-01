#Week2 - TicTacToe
#Ethan Blake

input_loop = True
row1 = 0
row2 = 0
row3 = 0
column1 = 0
column2 = 0
column3 = 0
grid = []
grid_input = ""

def create_grid(grid, grid_input, player_character):
    grid[grid_input-1] = player_character
    return grid
    
def print_grid(grid):
    print("\n")
    print (f"{grid[0]}|{grid[1]}|{grid[2]}")
    print(f"-+-+-")
    print (f"{grid[3]}|{grid[4]}|{grid[5]}")
    print(f"-+-+-")
    print (f"{grid[6]}|{grid[7]}|{grid[8]}")

def check_for_win(grid):
    win = True
    if grid[0] == grid [1] == grid[2]:
        win = False
    elif grid[3] == grid [4] == grid[5]:
        win = False
    elif grid[6] == grid [7] == grid[8]:
        win = False
    elif grid[0] == grid [3] == grid[6]:
        win = False
    elif grid[1] == grid [4] == grid[7]:
        win = False
    elif grid[2] == grid [5] == grid[8]:
        win = False
    elif grid[0] == grid [4] == grid[8]:
        win = False
    elif grid[2] == grid [4] == grid[6]:
        win = False
    else:
        win = True
    return win

def main():
    grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    win_loop = True
    counter = 0
    while win_loop == True:
        print_grid(grid)
        if (counter % 2) == 0:
            player_character = "X"
        else:
            player_character = "O"
        grid_input = int(input("\n>> "))
        grid = create_grid(grid, grid_input, player_character)
        print_grid(grid)
        win = check_for_win(grid)
        if win == False:
            print("You win!")
            win_loop = False
        else:
            counter += 1

if __name__ == "__main__":
    main()