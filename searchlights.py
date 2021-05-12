import math
# 已知圆心，半径，求指定角度的座标
def pointIn(x, y, r, a):
    x1 = x if a == 180 or a == 360 else x + r * math.sin(math.radians(a)) 
    y1 = y if a == 90 or a == 270 else y + r * math.cos(math.radians(a))    
    return x1, y1

# 两点距离
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt(math.pow(y2 - y1, 2) + math.pow(x2 - x1, 2))

# 求多个圆与多个多边形的交点
def searchlights(polygons, lights):
    count = 0
    p_list = []
    for lx, ly, lr in lights:
        for top_x, top_y, leng, num in polygons:
            r = (leng / 2) / (math.sin(math.radians((360 / num) / 2)))
            for p in range(0, num):
                x1, y1 = pointIn(top_x, top_y - r, r, p / num * 360)
                if x1 < 0 or y1 < 0: continue 
                if distance((x1, y1), (lx, ly)) < lr:p_list.append((x1, y1))
    return len(set(p_list))

if __name__ == '__main__':
    print("Example:")
    
    
    # print(f"角度{a}, 坐标（{x1}, {y1}）")
    # print (searchlights([(2, 3, 2, 3)], [(1, 2, 1)]))

    # # These "asserts" are used for self-checking and not for an auto-testing
    assert(searchlights([(2, 3, 2, 3)], [(1, 2, 1)])) == 1, 'regular triangle'
    assert(searchlights([(4, 5, 2, 4)], [(4, 4, 3)])) == 4, 'square'
    assert(searchlights([(6, 7, 2, 5)], [(2, 3, 2)])) == 0, 'regular pentagon'
    assert(searchlights([(4, 2, 2, 6)], [(4, 2, 3)])) == 3, 'regular hexagon'
    assert(searchlights([(1, 7, 2, 8)], [(0, 5, 4)])) == 5, 'regular octagon'
    assert(searchlights([(4, 2, 2, 6)], [(4, 1, 3)])) == 3, 'regular octagon'
    assert(searchlights([(2, 3, 2, 6), (4, 7, 2, 6)], [(3, 3, 2)])) == 4, 'regular octagon'
    assert(searchlights([
        (2,5,3,3),(6,5,3,3)
        ],
        [(3,4,2),
        (4,2,2)]
        )) == 3, 'ddd'
    
    print("Coding complete? Click 'Check' to earn cool rewards!")
