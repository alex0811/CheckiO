from datetime import datetime
# from typing import List

def sum_light(els):
    return sum(map(
        lambda _: (_[1] - _[0]).total_seconds(),
        zip(*(iter(els),) *2)
    ))


if __name__ == '__main__':
    print("Example:")
    print(sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 12, 11, 10 , 10),
    ]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
    ]) == 610

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 12, 11, 10 , 10),
    ]) == 1220

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 12, 11, 10 , 10),
        datetime(2015, 1, 12, 11, 10 , 10),
        datetime(2015, 1, 12, 12, 10 , 10),
    ]) == 4820

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 0 , 1),
    ]) == 1

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 0 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 13, 11, 0 , 0),
    ]) == 86410

    print("The first mission in series is completed? Click 'Check' to earn cool rewards!")


# import numpy as np

# def except_zero(items):
#     d = np.array(items)
#     d[d!=0] = sorted(d[d!=0])
#     return d

# def except_zero(items):
#     d = list(filter(lambda _: _ !=0, sorted(items)))
#     result = []
#     for (idx, value) in enumerate(items):
#         add = value if value is 0 else d[idx-result.count(0)]
#         result.append(add)
#     return result


# if __name__ == '__main__':
#     print("Example:")
#     print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
#     assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
#     assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
#     assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
#     assert list(except_zero([0, 0])) == [0, 0]
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# def frequency_sorting(numbers):
#     return list(reversed(sorted(
#         sorted(numbers,reverse=1),
#         key=lambda x: numbers.count(x),
#     )))

# if __name__ == '__main__':
#     print("Example:")
#     print(frequency_sorting([1, 2, 3, 4, 5]))

#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
#     assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [4, 4, 4, 3, 3, 11, 11, 7, 13], "Not sorted"
#     assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [10, 10, 21, 21, 55, 55, 99, 99], "Reversed"
#     print("Coding complete? Click 'Check' to earn cool rewards!")
