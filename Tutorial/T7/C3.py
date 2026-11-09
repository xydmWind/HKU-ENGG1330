def copy_grid(grid: list) -> list:
    new_grid = []

    for row in grid:
        tmp_row = [col for col in row]
        new_grid.append(tmp_row)

    return new_grid


rows = int(input())
columns = int(input())
grid = []
for r in range(rows):
    row = []
    for c in range(columns):
        row.append(int(input()))
    grid.append(row)
row_index = int(input())
column_index = int(input())
replacement = int(input())
trial = copy_grid(grid)
trial[row_index][column_index] = replacement
print(grid)
print(trial)
print(trial[row_index] is grid[row_index])