def aspect_size(size, boundRect):
    w, h = size
    b_x, b_y, b_w, b_h = boundRect
    ratio = w / h
    # verison 1
    # if ratio >= 1:
    #     r_w = b_w	
    #     r_h = r_w / ratio
    #     if (r_h > b_h):
    #         r_h = b_h	
    #         r_w = r_h * ratio
    # else:
    #     r_h = b_h
    #     r_w = r_h * ratio
    #     if (r_w > b_w):
    #         r_w = b_w	
    #         r_h = r_w / ratio

    # ratio = w / h
    # if r1 > r2 => r1的w变化率大，w = w2, h = w / r
    # if r1 < r2 => r1的h变化率大，h = h2, w = h * r

    # version 2
    b_r = b_w / b_h
    return (b_w, b_w / ratio) if ratio > b_r else (b_h * ratio, b_h)

    return result

if __name__ == '__main__':
    # radio = 1 with bounds
    assert aspect_size((1, 1), (0, 0, 200, 200)) == (200, 200)
    assert aspect_size((1, 1), (0, 0, 100, 200)) == (100, 100)
    assert aspect_size((1, 1), (0, 0, 200, 100)) == (100, 100)

    # ratio > 1 with bounds
    assert aspect_size((16, 9), (0, 0, 200, 200)) == (200, 200 / (16/9))
    assert aspect_size((16, 9), (0, 0, 100, 200)) == (100, 100 / (16/9))
    assert aspect_size((16, 9), (0, 0, 200, 100)) == (100 * (16 / 9), 100)

    # ratio < 1 with bounds
    assert aspect_size((9, 16), (0, 0, 200, 200)) == (200 * (9 / 16), 200)
    assert aspect_size((9, 16), (0, 0, 100, 200)) == (100, 100 / (9  /16))
    assert aspect_size((9, 16), (0, 0, 200, 100)) == (100 * (9 / 16), 100)
    


