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
    grid[grid_input] = player_character
    return grid
    
def print_grid(grid):
    print (f"{grid[0]}|{grid[1]}|{grid[2]}")
    print (f"{grid[3]}|{grid[4]}|{grid[5]}")
    print (f"{grid[6]}|{grid[7]}|{grid[8]}")

def check_for_win(grid,):
    win = create_rows_columns(grid)
    return win


def create_rows_columns(grid):
    if grid[0:3] or grid[3:6] == "xxx" or "ooo":
        win = False
    else:
        win = True
    return win

def main():
    grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    counter = 0
    print("hi")
    win_loop = True
    while win_loop == True:
        print_grid(grid)
        if (counter % 2) == 0:
            player_character = "x"
        else:
            player_character = "o"
        grid_input = int(input(">>"))
        grid = create_grid(grid, grid_input, player_character)
        win = check_for_win(grid)
        if win == True:
            counter += 1
        else:
            win_loop = False
    print("You win!")

    
if __name__ == "__main__":
    main()