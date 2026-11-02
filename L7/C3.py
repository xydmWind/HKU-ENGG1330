def make_grid(rows: int, columns: int, initial: int) -> list:
    grid = []
    for _ in range(rows):
        row = []
        for _ in range(columns):
            row.append(initial)
        grid.append(row)
    return grid


rows = int(input())
columns = int(input())
initial = int(input())
row_index = int(input())
column_index = int(input())
replacement = int(input())
grid = make_grid(rows, columns, initial)
grid[row_index][column_index] = replacement
for row in grid:
    print(row)
