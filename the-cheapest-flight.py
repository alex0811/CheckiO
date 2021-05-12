from typing import List
# 生成矩阵
def matrix_genetor(vex_num):
    data_matrix = []
    for i in range(vex_num):
        one_list = []
        for j in range(vex_num):
            one_list.append(9999)
        data_matrix.append(one_list)
    return data_matrix

c_index = lambda x: ord(str(x)) - ord("A")

def cheapest_flight(costs: List, a: str, b: str) -> int:
    nums_vertex = 0
    for cost in costs: nums_vertex = max(c_index(cost[0]), c_index(cost[1])) + 1
    matrix = matrix_genetor(nums_vertex)
    for cost in costs:
        u, v, c = cost
        matrix[c_index(u)][c_index(v)] = c
        matrix[c_index(v)][c_index(u)] = c

    for k in range(nums_vertex):
        for i in range(nums_vertex):
            for j in range(nums_vertex):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    result = matrix[c_index(a)][c_index(b)]
    return 0 if result == 9999 else result


if __name__ == '__main__':
    print("Example:")

    # These "asserts" are used for self-checking and not for an auto-testing
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'A',
 'C') == 70
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'C',
 'A') == 70
    assert cheapest_flight([['A', 'C', 40],
  ['A', 'B', 20],
  ['A', 'D', 20],
  ['B', 'C', 50],
  ['D', 'C', 70]],
 'D',
 'C') == 60
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['D', 'F', 900]],
 'A',
 'F') == 0
    assert cheapest_flight([['A', 'B', 10],
  ['A', 'C', 15],
  ['B', 'D', 15],
  ['C', 'D', 10]],
 'A',
 'D') == 25
    print("Coding complete? Click 'Check' to earn cool rewards!")
