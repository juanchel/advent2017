def get_value(grid_dict, x, y):
    if x in grid_dict and y in grid_dict[x]:
        return grid_dict[x][y]
    else:
        return 0


UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

last_num = 1
current_x = 0
current_y = 0
current_dir = LEFT

grid = {
    0: {
        0: 1,
    }
}

while last_num < 277678:
    new_x = current_x
    new_y = current_y
    if current_dir == LEFT:
        new_x -= 1
    elif current_dir == RIGHT:
        new_x += 1
    elif current_dir == UP:
        new_y += 1
    elif current_dir == DOWN:
        new_y -= 1

    new_num = get_value(grid, new_x + 1, new_y)
    new_num += get_value(grid, new_x - 1, new_y)
    new_num += get_value(grid, new_x + 1, new_y + 1)
    new_num += get_value(grid, new_x - 1, new_y - 1)
    new_num += get_value(grid, new_x + 1, new_y - 1)
    new_num += get_value(grid, new_x - 1, new_y + 1)
    new_num += get_value(grid, new_x, new_y + 1)
    new_num += get_value(grid, new_x, new_y - 1)

    if new_x in grid:
        grid[new_x][new_y] = new_num
    else:
        grid[new_x] = { new_y: new_num }

    last_num = new_num
    current_x = new_x
    current_y = new_y

    if current_dir == LEFT and get_value(grid, new_x, new_y - 1) == 0:
        current_dir = DOWN
    elif current_dir == RIGHT and get_value(grid, new_x, new_y + 1) == 0:
        current_dir = UP
    elif current_dir == UP and get_value(grid, new_x - 1, new_y) == 0:
        current_dir = LEFT
    elif current_dir == DOWN and get_value(grid, new_x + 1, new_y) == 0:
        current_dir = RIGHT

print last_num
