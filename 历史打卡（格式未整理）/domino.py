def domino_chain(tiles: str) -> int:
    # print(tiles.split(','))
    data = tiles.split(',')
    for (idx, value) in enumerate(data):
        item = data[idx]
        l, r = item.split('-')
        print(l, r)
        

    return 0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert domino_chain("0-2, 0-5, 1-5, 1-3, 5-5") == 1
    # assert domino_chain("1-5, 2-5, 3-5, 4-5, 3-4") == 2
    # assert domino_chain("0-5, 1-5, 2-5, 3-5, 4-5, 3-4") == 0
    # assert domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4") == 6
    # assert domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4, 3-0, 0-4") == 0
    # assert domino_chain("1-2, 2-2, 2-3, 3-3, 3-1") == 5
    # assert domino_chain("1-4, 3-4, 0-4, 0-5, 4-5, 2-4, 2-5") == 0
    # assert domino_chain("1-4, 1-5, 0-2, 1-6, 4-6, 4-5, 5-6") == 0
    # assert domino_chain("1-2, 2-3, 2-4, 3-4, 2-5, 2-6, 5-6") == 8
    # assert domino_chain("1-2, 2-3, 3-1, 4-5, 5-6, 6-4") == 0
    # assert domino_chain("1-2, 1-4, 1-5, 1-6, 1-1, 2-5, 4-6") == 28
    print("Basic tests passed.")
