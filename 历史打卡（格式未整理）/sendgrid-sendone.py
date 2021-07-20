def barcode_reader(barcode):
    dd = list(map(
        lambda x: 1 if x == '_' else 0,
        list(barcode)
        ))
    # print(dd)
    if dd[:3] != [1,0,1] or dd[-3:] != [1,0,1]:return None
    ccc = dd[3:-3]
    if ccc[42:47] != [0,1,0,1,0]: return None

    left_part = ccc[:42]
    right_part = ccc[47:]
    print('左边', left_part)
    print('右边', right_part)
    left_str, left_code = check_left(left_part)
    right_str = check_right(right_part)

    if right_str == None or left_str == None:
        print('左右颠倒')
        left_part = ccc[47:][::-1]
        right_part = ccc[:42][::-1]
        left_str, left_code = check_left(left_part)
        right_str = check_right(right_part)

    if right_str == None or left_str == None:
        return None
    result = left_str + right_str
    right_check_code = ''
    if left_code == 'LLLLLL':
        result = '0' + result
    elif left_code == 'LLGLGG':
        result = '1' + result
    elif left_code == 'LLGGLG':
        result = '2' + result
    elif left_code == 'LLGGGL':
        result = '3' + result
    elif left_code == 'LGLLGG':
        result = '4' + result
    elif left_code == 'LGGLLG':
        result = '5' + result
    elif left_code == 'LGGGLL':
        result = '6' + result
    elif left_code == 'LGLGLG':
        result = '7' + result
    elif left_code == 'LGLGGL':
        result = '8' + result
    elif left_code == 'LGGLGL':
        result = '9' + result
    else:
        print('left_code没有')
        return None
    check_d = 10 - ((int(result[1]) + int(result[3]) + int(result[5]) + int(result[7]) + int(result[9]) + int(result[11])) * 3 + (int(result[0]) + int(result[2]) + int(result[4]) + int(result[6]) + int(result[8]) + int(result[10]))) % 10
    print(result, check_d)
    if check_d == 10: return result
    return result if int(result[-1]) == check_d else None

def check_left(datas):
    result = ''
    left_code = ''
    for code in zip(*(iter(datas),) *7):
        code_str = ''
        for c in code: code_str = code_str + str(c)
        if code_str == '0001101' or code_str == '0100111':
            result = result + '0'
            left_code = left_code + ('L' if code_str == '0001101' else 'G')
        elif code_str == '0011001' or code_str == '0110011':
            result = result + '1'
            left_code = left_code + ('L' if code_str == '0011001' else 'G')
        elif code_str == '0010011' or code_str == '0011011':
            result = result + '2'
            left_code = left_code + ('L' if code_str == '0010011' else 'G')
        elif code_str == '0111101' or code_str == '0100001':
            result = result + '3'
            left_code = left_code + ('L' if code_str == '0111101' else 'G')
        elif code_str == '0100011' or code_str == '0011101':
            result = result + '4'
            left_code = left_code + ('L' if code_str == '0100011' else 'G')
        elif code_str == '0110001' or code_str == '0111001':
            result = result + '5'
            left_code = left_code + ('L' if code_str == '0110001' else 'G')
        elif code_str == '0101111' or code_str == '0000101':
            result = result + '6'
            left_code = left_code + ('L' if code_str == '0101111' else 'G')
        elif code_str == '0111011' or code_str == '0010001':
            result = result + '7'
            left_code = left_code + ('L' if code_str == '0111011' else 'G')
        elif code_str == '0110111' or code_str == '0001001':
            result = result + '8'
            left_code = left_code + ('L' if code_str == '0110111' else 'G')
        elif code_str == '0001011' or code_str == '0010111':
            result = result + '9'
            left_code = left_code + ('L' if code_str == '0001011' else 'G')
        else:
            print('左边没有找到')
            return None, None
    return result, left_code

def check_right(datas):
    result = ''
    for code in zip(*(iter(datas),) *7):
        code_str = ''
        for c in code: code_str = code_str + str(c)
        if code_str == '1110010':
            result = result + '0'
        elif code_str == '1100110':
            result = result + '1'
        elif code_str == '1101100':
            result = result + '2'
        elif code_str == '1000010':
            result = result + '3'
        elif code_str == '1011100':
            result = result + '4'
        elif code_str == '1001110':
            result = result + '5'
        elif code_str == '1010000':
            result = result + '6'
        elif code_str == '1000100':
            result = result + '7'
        elif code_str == '1001000':
            result = result + '8'
        elif code_str == '1110100':
            result = result + '9'
        else:
            print('右边没有找到')
            return None
    return result

if __name__ == '__main__':
    # assert barcode_reader(
    #     '_ _   _ __ _  ___ __  __  _  __ ____ _  ___ _ _ _ __  __ __ __  _    _ _ ___  _  ___ _   _  _ _'
    # ) == '5901234123457', '5901234123457'

    # assert barcode_reader(
    #     '_ _  _  __  _ ___   _ __ _ ____   _  _  _   _ _ _ _ _    __  __ _    _ _ _    _ _    _  ___ _ _'
    # ) == '4299687613665', '4299687613665'

    # assert barcode_reader(
    #     '___  _  __  _ ___   _ __ _ ____   _  _  _   _ _ _ _ _    __  __ _    _ _ _    _ _    _  ___ _ _'
    # ) is None, 'wrong left guard bar'
    
    # assert barcode_reader(
    #     '_ _  _  __  _ ___   _ __ _ ____   _  _  _   _ _ ___ _    __  __ _    _ _ _    _ _    _  ___ _ _'
    # ) is None, 'wrong center bar'

    # assert barcode_reader(
    #     '_ _  _  __  _ ___   _ __ _ ____   _  _  _   _ _ _ _ _    __  __ _    _ _ _    _ _    _  ___ ___'
    # ) == None, 'wrong right guard bar'
    # assert barcode_reader(
    #     '_ _ ___ __  __  _  _  __ ____ _ _   __ __   _ _ _ _ _    _   _  _  _   ___ _  __  __ __ __  _ _'
    # ) is None, '0712345678912 : wrong check digit (right: 1)'

    # assert barcode_reader("_ _ __  __ __  __  _ ___   _  _  _   _    _ _ _ _ _   __ __   _ _ ____ __  _  _  __  __ ___ _ _") == '0712345678911', '错了'
    # assert barcode_reader("_ _   _ __  __  _ _  ___  ___ _  _ ___ ___ __ _ _ _ _    _  ___ _    _ _ _    __  __ ___  _ _ _") == '3910497653610', 'Checksum zero case'
    assert barcode_reader("_ _ ___ __  __  _        ____ _ _   __ __   _ _ _ _ _    _   _  _  _   ___ _  __  __ __  __ _ _")
    print("Check done.")

