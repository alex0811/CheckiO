# def replace_last(line):
#     return line[-1:] + line[:-1]


# if __name__ == '__main__':
#     print("Example:")
#     print(replace_last([2, 3, 4, 1]))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
#     assert replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
#     assert replace_last([1]) == [1]
#     assert replace_last([]) == []
#     print("Coding complete? Click 'Check' to earn cool rewards!")
# import math

# def index_power(array, n):
#     try: return array[n] ** n 
#     except:return -1

# if __name__ == '__main__':
#     print('Example:')
#     print(index_power([1, 2, 3, 4], 2))
    
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert index_power([1, 2, 3, 4], 2) == 9, "Square"
#     assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
#     assert index_power([0, 1], 0) == 1, "Zero power"
#     assert index_power([1, 2], 3) == -1, "IndexError"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# def is_majority(items):
#     return items.count(True) > items.count(False)

# is_majority = lambda _: _.count(True)<<1>len(_)

# if __name__ == '__main__':
#     print("Example:")
#     print(is_majority([True, True, False, True, False]))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_majority([True, True, False, True, False]) == True
#     assert is_majority([True, True, False]) == True
#     assert is_majority([True, True, False, False]) == False
#     assert is_majority([True, True, False, False, False]) == False
#     assert is_majority([False]) == False
#     assert is_majority([True]) == True
#     assert is_majority([]) == False
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# import Iterable
# from typing import Iterable


# def remove_all_after(items, border):
#     print(str(items))
    
#     return items[:border-1]


# if __name__ == '__main__':
#     print("Example:")
#     print(list(remove_all_after([1, 2, 3, 4, 5], 3)))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
#     assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
#     assert list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2]
#     assert list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
#     assert list(remove_all_after([], 0)) == []
#     assert list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7]
#     print("Coding complete? Click 'Check' to earn cool rewards!")
import math

import numpy as np

checkio = lambda _: np.median(_)
# def checkio(data):
#     return np.median(data)
    # print(np.median(data))
    # data = sorted(data)
    # if len(data) % 2 == 0:
    #     index = len(data) / 2 - 1
    #     return sum(data[index: index + 2]) / 2.0
    # else:
    #     index = int(math.ceil(len(data) / 2.0)) - 1
    #     return sum(data[index: index + 1]) / 1.0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([1, 2, 3, 4, 5, 6]))

    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("Coding complete? Click 'Check' to earn cool rewards!")

