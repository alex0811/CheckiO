# 根据方向向量，如果x大于0，判断是否碰到右边，小于0，判断是否碰到左边
# 当向量y大于0时，才有可能触顶，
# 进行20次的循环计算，
# your code here
# 计算方程与线段之间的交点，交点是否在d内，交点是否在四角，交点发生位置（垂直线/水平线）
# 设置方程，方向，在这个方向上，是否与线段（点1，点2）有交点

def escape(jar, fly):
    W, H, d = jar
    x0, y0, vx, vy = fly

    print(f'瓶子宽度{W}, 高度{H}, 出口宽度{d}')
    result = False
    for i in range(1, 21):
        print(f'起点座标({x0}, {y0}), 方向向量vx {vx}, vy {vy}')
        if vx == 0:
            if vy > 0:
                touch_x = x0
                touch_y = H
            else:
                touch_x = x0
                touch_y = 0
        elif vy == 0:
            if vx > 0:
                touch_x = -1
                touch_y = y0
            else:
                touch_x = 0
                touch_y = y0
        else:
            k = vy / vx
            b = y0 - k * x0
            touch_y = k * (0 if vx < 0 else W) + b
            if vy >= 0:
                touch_x = (H - b) / k
            else:
                touch_x = -b / k
            # print(k, b)
        
        print(touch_x, touch_y)

        if vy >= 0:
            if 0 <= touch_x <= W:
                if is_valid_top_x(touch_x, W, d):
                    print("escape")
                    result = True
                    break
                elif (touch_x == W or touch_x == 0) and touch_y == H:
                    print("anchor1", touch_x, touch_y)  
                    vx = -vx
                    vy = -vy
                    y0 = H
                    x0 = touch_x
                else:
                    print("折射1")    
                    vy = -vy
                    y0 = H
                    x0 = touch_x
            elif touch_y < H:
                vx = -vx
                y0 = touch_y
                x0 = W
                print("折射", x0, y0)
        elif vy < 0:
            if 0 <= touch_x <= W:
                if touch_x == W or touch_x == 0:
                    print("anchor")     
                    vx = -vx
                    vy = -vy
                    y0 = 0
                    x0 = touch_x
                else:
                    print("折射")  
                    vy = -vy
                    y0 = 0
                    x0 = touch_x  
            elif touch_y < H:
                print("折射")
                vx = -vx
                y0 = touch_y
                x0 = 0
    print('结果', result)
    return result

# 是否可以逃离
def is_valid_top_x(top_x, W, d):
    return abs(top_x - (W / 2)) < d / 2


if __name__ == '__main__':
    print("Example:")
    # print(escape([1000, 1000, 200], [0, 0, 100, 0]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert escape([1000, 1000, 200], [0, 0, 100, 0]) == False, "First"
    assert escape([1000, 1000, 200], [450, 50, 0, -100]) == True, "Second"
    assert escape([1000, 1000, 200], [450, 1000, 100, 0]) == False, "Third"
    assert escape([1000, 1000, 200], [250, 250, -10, -50]) == False, "Fourth"
    assert escape([1000, 2000, 200], [20, 35, 100, 175]) == True, "Fifth"
    print("Coding complete? Click 'Check' to earn cool rewards!")