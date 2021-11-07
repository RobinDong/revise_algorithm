# Travel from top-left to bottom-right position of a rectangle


def grid_travel(rows, cols, memory):
    if (rows, cols) in memory:
        return memory[(rows, cols)]

    if rows == 0 or cols == 0:
        return 0
    if rows == 1 and cols == 1:
        return 1
    down = grid_travel(rows - 1, cols, memory)
    memory[(rows - 1, cols)] = down
    right = grid_travel(rows, cols - 1, memory)
    memory[(rows, cols - 1)] = right
    return down + right


if __name__ == "__main__":
    print(grid_travel(18, 18, {}))
