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
    grid.seek(0)
    return columns

def build_diagonal(grid, start):
    """if start is 'left', then start from the top left corner
    and go towards the bottom right. if start is 'right', then
    start from the top right corner and go towards to bottom left.
    Returns all diagonals with length >= 4."""
    if start == 'left':
        current_row, current_column = 1, 1
    elif start == 'right':
        current_row, current_column = 1, 20
    diagonals = []
    for c in range(20):
        if start == 'left':
            current_row, current_column = 1, c + 1
        elif start == 'right':
            current_row, current_column = 1, 20 - c
        end = False
        current_diagonal = []
        while not end:
            grid.seek((60 * (current_row - 1)) + (3 * (current_column - 1)))
            current_diagonal.append(int(grid.read(2)))
            if start == 'left':
                current_column -= 1
                current_row += 1
                if current_column < 1:
                    end = True
            elif start == 'right':
                current_column += 1
                current_row += 1
                if current_column > 20:
                    end = True
        if len(current_diagonal) >= 4:
            diagonals.append(deepcopy(current_diagonal))
    grid.seek(0)
    return diagonals

def fourproducts_max(current_list, previous_max):
    current_max = previous_max
    for l in current_list:
        for current_pos in range(len(l) - 4):
            current_product = 1
            for i in range(4):
                current_product = current_product * l[i+(current_pos - 1)]
            if current_product > current_max:
                current_max = current_product
    return current_max

twentygrid = open('twentygrid.txt')
row_list = build_rows(twentygrid)
column_list = build_columns(twentygrid)
leftdiagonal_list = build_diagonal(twentygrid, 'left')
rightdiagonal_list = build_diagonal(twentygrid, 'right')
lists = [row_list, column_list, leftdiagonal_list, rightdiagonal_list]
the_max = 0
for l in range(4):
    the_max = fourproducts_max(lists[l], the_max)
print('The maximum product is: {0}'.format(the_max))
