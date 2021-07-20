def reverse_ascending(items):
    order_list = []
    temp_list = []
    for item in items:
        if len(temp_list) == 0:
            temp_list.append(item)
            continue
        elif item > temp_list[-1]:
            temp_list.append(item)
        else:
            order_list = order_list + list(reversed(temp_list))
            temp_list = [item]
    return order_list + list(reversed(temp_list))


if __name__ == '__main__':
    print("Example:")
    print(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
