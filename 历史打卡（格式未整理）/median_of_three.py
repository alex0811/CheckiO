# from typing import Iterable
from operator import le
import numpy as np

# np.median(_)
def median_three(els):
    return els[:2] + map(
        lambda _: int(np.median(els[_:_+3])),
        range(len(els)-2)
    ) if len(els) >= 3 else els


if __name__ == '__main__':
    print("Example:")
    print(list(median_three([1, 2, 3, 4, 5, 6, 7])))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
    assert list(median_three([1])) == [1]
    assert list(median_three([5,2,9,1,7,4,6,3,8])) == [5,2,5,2,7,4,6,4,6]
    
    print("Coding complete? Click 'Check' to earn cool rewards!")