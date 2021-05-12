def get(cmpItem, c, result):
    l_list = cmpItem[0:cmpItem.index(c)]
    r_list = cmpItem[cmpItem.index(c)+1:]
    min_c = ''
    max_c = ''
    for l_item in reversed(l_list):
        if l_item in result:
            min_c = l_item
            break
    for r_item in r_list:
        if r_item in result:
            max_c = r_item
            break
    return min_c, max_c

def checkio(data):
    result = ''
    b_list = []
    for item in data:
        print(item, result)
        for c in item:
            # if c in result: result = result.replace(c,'')
            if c in result: continue
            min_c, max_c = get(item, c, result)
            print(c, min_c, max_c)
            if max_c == '' and min_c != '':
                b_list.append(c)
            if min_c == max_c == '':
                result = result + c
            elif min_c == '':
                if result.index(max_c) == 0:
                    result = c + result
                else:
                    result = result + c       
            else:
                if max_c == '':
                    result = result + c
                else:
                    dd = list(result)
                    dd.insert(result.index(min_c) + 1, c)
                    result = ''.join(dd)
    print(result, b_list)
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio(["acb", "bd", "zwa"]) == "zwacbd",  "Just concatenate it"
    # assert checkio(["klm", "kadl", "lsm"]) == "kadlsm",  "Paste in"
    # assert checkio(["a", "b", "c"]) == "abc",  "Cant determine the order - use english alphabet"
    # assert checkio(["aazzss"]) == "azs",  "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg",  "Concatenate and paste in"

    # assert checkio(["my","name","myke"]) == 'namyke'

    # assert checkio(["qwerty","asdfg","zxcvb","yagz"]) == 'qwertyasdfgzxcvb'

