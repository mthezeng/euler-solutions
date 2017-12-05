#INCOMPLETE

from copy import deepcopy

def build_rows(grid):
    #grid is a file object
    rows = []
    for l in range(20):
        current_row = []
        for i in range(20):
            current_row.append(int(grid.read(2)))
            grid.read(1) #skips over the space
        rows.append(deepcopy(current_row))
    grid.seek(0)
    return rows

def build_columns(grid):
    columns = []
    for c in range(20):
        current_column = []
        for r in range(20):
            current_column.append(int(grid.read(2)))
            grid.seek((60*(r+1))+(3*c))
        columns.append(deepcopy(current_column))
        grid.seek(3*c)
    return columns


twentygrid = open('twentygrid.txt')
row_list = build_rows(twentygrid)
#print(row_list)
column_list = build_columns(twentygrid)
print(column_list)
