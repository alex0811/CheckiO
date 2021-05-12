import math

def is_h(p1, p2):return p1[1] == p2[1]
def is_v(p1, p2):return p1[0] == p2[0]
def get_k_b(p1, p2):
    p1_x, p1_y = p1
    p2_x, p2_y = p2

    k = (p2_y - p1_y) / (p2_x - p1_x)
    b = p1_y - k * p1_x
    return (k, b)
    

def shot(wall1, wall2, shot_point, later_point):
    wall1_x, wall1_y = wall1
    wall2_x, wall2_y = wall2

    shot1_x, shot1_y = shot_point
    shot2_x, shot2_y = later_point

    #靶子中心点
    target_x = (wall1_x + wall2_x) / 2.0
    target_y = (wall1_y + wall2_y) / 2.0

    #墙的长度
    wall_len = math.sqrt(math.pow(wall2_y - wall1_y, 2) + math.pow(wall2_x - wall1_x, 2))

    #考虑垂直线的做法
    is_wall_v, is_wall_h = is_v(wall1, wall2), is_h(wall1, wall2)
    is_shot_v, is_shot_h = is_v(shot_point, later_point), is_h(shot_point, later_point)
    is_wall_c = is_wall_v or is_wall_h
    is_shot_c = is_shot_v or is_shot_h

    if is_wall_c and is_shot_c:
        if is_wall_h and is_shot_h or is_wall_v and is_shot_v:return -1
        else:
            if is_wall_h:
                y = wall1_y
                x = shot1_x
            else:
                y = shot1_y
                x = wall1_x
    elif is_wall_c:
        k2, b2 = get_k_b(shot_point, later_point)
        if is_wall_v:
            x = wall1_x
            y = k2 + x + b2
        else:
            y = wall2_y
            x = (y - b2) / k2
    elif is_shot_c:
        k1, b1 = get_k_b(wall1, wall2) #墙的方程式
        if is_shot_v:
            x = shot1_x
            y = k1 * x + b1
        else:
            y = shot1_y
            x = (y - b1) / k1
    else:
        k1, b1 = get_k_b(wall1, wall2)
        k2, b2 = get_k_b(shot_point, later_point)
        if k1 == k2: return -1            
        x = (b2 - b1) / (k1 - k2)
        y = k1 * x + b1
    
    # 交点是否在延长线上
    len_shot = math.sqrt(math.pow(y - shot1_y, 2) + math.pow(x - shot1_x, 2))
    len_later = math.sqrt(math.pow(y - shot2_y, 2) + math.pow(x - shot2_x, 2))
    if len_later >= len_shot:return -1

    #交点与靶心的距离
    dis = math.sqrt(math.pow(x - target_x, 2) + math.pow(y - target_y, 2))
    core = dis / (wall_len / 2)
    return round(100-core*100) if core <= 1 else -1

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert shot((2, 2), (5, 7), (11, 2), (8, 3)) == 100, "1st case"
    assert shot((2, 2), (5, 7), (11, 2), (7, 2)) == 0, "2nd case"
    assert shot((2, 2), (5, 7), (11, 2), (8, 4)) == 29, "3th case"
    assert shot((2, 2), (5, 7), (11, 2), (9, 5)) == -1, "4th case"
    assert shot((2, 2), (5, 7), (11, 2), (10.5, 3)) == -1, "4th case again"
    assert shot((2,2),(5,7),(8,3),(11,2)) == -1
    assert  shot((10,10),(10,90),(70,60),(50,60)) == 75
    shot((2,2),(10,2),(5,10),(3,5))