
# import datetime

# def most_frequent_days(a):
#     week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#     weak_days = []
#     for i in range(1,8):
#         d = datetime.date(a, 1, i)
#         weak_days.append(d.strftime('%A'))
#         if d.weekday() == 6:break

#     for i in range(31, 24, -1):
#         d = datetime.date(a, 12, i)
#         weak_days.append(d.strftime('%A'))
#         if d.weekday() == 0: break

#     x = list(filter(lambda _: weak_days.count(_), weak_days))
#     result = []
#     for day in x:
#         if weak_days.count(day) == weak_days.count(x[0]):result.append(day)

#     return list(sorted(set(result),key=lambda x: week.index(x) ))


# if __name__ == '__main__':
#     print("Example:")
#     print(most_frequent_days(1084))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert most_frequent_days(1084) == ['Tuesday', 'Wednesday']
#     assert most_frequent_days(1167) == ['Sunday']
#     assert most_frequent_days(1216) == ['Friday', 'Saturday']
#     assert most_frequent_days(1492) == ['Friday', 'Saturday']
#     assert most_frequent_days(1770) == ['Monday']
#     assert most_frequent_days(1785) == ['Saturday']
#     assert most_frequent_days(212) == ['Wednesday', 'Thursday']
#     assert most_frequent_days(1) == ['Monday']
#     assert most_frequent_days(2135) == ['Saturday']
#     assert most_frequent_days(3043) == ['Sunday']
#     assert most_frequent_days(2001) == ['Monday']
#     assert most_frequent_days(3150) == ['Sunday']
#     assert most_frequent_days(3230) == ['Tuesday']
#     assert most_frequent_days(328) == ['Monday', 'Sunday']
#     assert most_frequent_days(2016) == ['Friday', 'Saturday']
#     print("Coding complete? Click 'Check' to earn cool rewards!")


from typing import List
import math

def gcd_many(s):
    g = 0
    for idx,value in enumerate(s):
        g = value if idx == 0 else math.gcd(g,s[idx])
    return g

def evenly_spaced_trees(trees: List[int]) -> int:
    temp = []
    for idx,value in enumerate(trees[0:-1]):
        temp.append((trees[idx + 1] - value))
    return (trees[-1]-trees[0]) / gcd_many(temp) + 1 - len(trees)


if __name__ == '__main__':
    print("Example:")
    # print(evenly_spaced_trees([0, 2, 6]))
    assert evenly_spaced_trees([0, 2, 6]) == 1, 'add 1'
    assert evenly_spaced_trees([1, 3, 6]) == 3, 'add 3'
    assert evenly_spaced_trees([0, 2, 4]) == 0, 'no add'

    assert evenly_spaced_trees([1,52,100]) == 31

    assert evenly_spaced_trees([55,63,83,87,95]) == 6

    print("Coding complete? Click 'Check' to earn cool rewards!")


