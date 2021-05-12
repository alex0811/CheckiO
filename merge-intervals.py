def merge_intervals(intervals):
    if not intervals:return []
    result = [intervals[0]]
    for inter in intervals[1:]:
        c_l, c_r = result[-1]
        i_l, i_r = inter
        if (i_r < c_l - 1 or i_l > c_r + 1):
            result.append(inter)
        else:
            result[-1] = (min(i_l, c_l), max(i_r, c_r))
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)]) == [(1, 6), (8, 10), (12, 19)], "First"
    assert merge_intervals([(1, 12), (2, 3), (4, 7)]) == [(1, 12)], "Second"
    assert merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]) == [(1, 15), (17, 20)], "Third"
    print('Done! Go ahead and Check IT')
    