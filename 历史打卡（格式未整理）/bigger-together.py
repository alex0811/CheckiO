from typing import List
from functools import cmp_to_key

def compare(x, y) -> bool:    
    x_str = str(x)
    y_str = str(y)
    if len(x_str) == len(y_str):
        return x - y
    else:
        a = int(x_str[0])
        b = int(y_str[0])
        return int(x_str + y_str) - int(y_str + x_str) if a == b else a - b
        
def bigger_together(ints: List[int]) -> int:
    reverseInts = sorted(ints, key=cmp_to_key(lambda x,y:compare(x, y)), reverse=True)
    sortedInts = sorted(ints, key=cmp_to_key(lambda x,y:compare(x, y)))
    return int(''.join(list(map(lambda x: str(x), reverseInts)))) - int(''.join(list(map(lambda x: str(x), sortedInts))))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert bigger_together([1,2,3,4]) == 3087, "4321 - 1234"
    assert bigger_together([1,2,3,4, 11, 12]) == 32099877, "43212111 - 11112234"
    assert bigger_together([0, 1]) == 9, "10 - 01"
    assert bigger_together([100]) == 0, "100 - 100"
    assert bigger_together([3,12,22,32]) == 2099889, '3322212 - 1222323'

    3,32,22,12
    print('Done! I feel like you good enough to click Check')