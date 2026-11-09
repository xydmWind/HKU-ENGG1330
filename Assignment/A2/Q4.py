def update_grid(grid):
    rows = len(grid)
    columns = len(grid[0])
    updated_grid = [[0] * columns for _ in range(rows)]

    for row in range(rows):
        for column in range(columns):
            occupied_neighbours = 0
            for neighbour_row in range(max(0, row - 1), min(rows, row + 2)):
                for neighbour_column in range(max(0, column - 1), min(columns, column + 2)):
                    if neighbour_row == row and neighbour_column == column:
                        continue
                    occupied_neighbours += grid[neighbour_row][neighbour_column]
            
            if occupied_neighbours == 3 or (occupied_neighbours == 2 and grid[row][column] == 1):
                updated_grid[row][column] = 1
    
    return updated_grid


if __name__ == "__main__":
    rows = int(input())
    columns = int(input())
    grid = []
    for row in range(rows):
        grid.append([int(value) for value in input().split()])
    updated = update_grid(grid)
    for row in updated:
        print(*row)