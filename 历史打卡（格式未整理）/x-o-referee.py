from typing import List, get_origin

def checkio(game_result: List[str]) -> str:
    result = 'D'
    for idx, value in enumerate(game_result):
        if len(value) == 3 and len(set(value)) == 1:
            result = value[0]
            break
        else:
            range = [0,1,2]
            range.pop(idx)
            for i, v in enumerate(value):
                if game_result[range[0]][i] is game_result[range[1]][i] is v:
                    result = v
                    break
        if result != 'D': break
        else:
            if game_result[0][0] is game_result[1][1] is game_result[2][2]:
                result = game_result[0][0]
            elif game_result[2][0] is game_result[1][1] is game_result[0][2]:
                result = game_result[2][0]
    return result if result != '.' else 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert checkio([
    #     "X.O",
    #     "XX",
    #     "XOO"]) == "X", "Xs wins"
    # assert checkio([
    #     "OO.",
    #     "XOX",
    #     "XOX"]) == "O", "Os wins"
    # assert checkio([
    #     "OOX",
    #     "XXO",
    #     "OXX"]) == "D", "Draw"
    # assert checkio([
    #     "O.X",
    #     "XX.",
    #     "XOO"]) == "X", "Xs wins again"
    assert checkio(["OXO","XOX","OXO"]) == 'O'
    assert checkio([".OX",".XX",".OO"]) == 'D'
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
