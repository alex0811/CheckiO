from typing import Iterable

# def can_balance(weights: Iterable) -> int:
#     for i in range(0, len(weights)):
#         leftWeight = sum((i - n) * w for n, w in enumerate(weights[0:i]))
#         rightWeight = sum(n * w for n, w in enumerate(weights[i:]))
#         if leftWeight == rightWeight: return i
#     return -1

def can_balance(weights: Iterable) -> int:
    p = sum(idx * value for idx, value in enumerate(weights)) / sum(weights)
    return p if int(p) == p else -1


if __name__ == '__main__':
    print("Example:")
    # print(can_balance([6, 1, 10, 5, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert can_balance([6, 1, 10, 5, 4]) == 2
    assert can_balance([10, 3, 3, 2, 1]) == 1
    assert can_balance([7, 3, 4, 2, 9, 7, 4]) == -1
    assert can_balance([42]) == 0