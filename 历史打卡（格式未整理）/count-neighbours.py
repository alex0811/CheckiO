def count_neighbours(grid, row, col):
    result = 0
    r = max(row - 1, 0)
    while r <= min(row + 1, len(grid)-1):
        c = max(col - 1, 0)
        while c <= min(col + 1, len(grid[0])-1):
            if r != row or c != col: result = result + grid[r][c]
            c = c + 1
        r = r + 1
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
    count_neighbours([[1,0,1,0,1],
                      [0,1,0,1,0],
                      [1,0,1,0,1],
                      [0,1,0,1,0],
                      [1,0,1,0,1],
                      [0,1,0,1,0]],5,4)
