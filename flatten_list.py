from collections.abc import Iterable
# 支持过滤字符串
# def flatten(items):
#     for x in items:
#         print(x)
#         if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
#             for sub_x in flatten(x):
#                 yield sub_x
#         else:
#             yield x

# import re
# def flat_list(array):
#     return [int(x) for x in re.findall(r"-?\d+", str(array))]

def flatten(items):
    for item in items:
        if not isinstance(item, Iterable):
            yield item
        else:
            for x in flatten(item):
                yield x

def flat_list(array): return list(flatten(array))

if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')