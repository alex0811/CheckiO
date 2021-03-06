from typing import Tuple

def follow(instructions: str) -> Tuple[int, int]:
    dx, dy = 0, 0
    for c in instructions:
        if c == 'f': dy += 1
        if c == 'b': dy -= 1
        if c == 'l': dx -=1
        if c == 'r': dx += 1
    return (dx, dy)


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
