def checkio(data):
    # 数据驱虫
    data_list = []
    for d in data:data_list.append(''.join(sorted(set(list(d)), key=d.index)))
    data_list = sorted(data_list)
    
    print('待识别数据源：', data_list)

    result = ''
    for (idx, inset_items) in enumerate(data_list):
        if result == '':
            result = inset_items
            continue
        result = order(inset_items, result, data_list[idx:])
        print('组合结果', result)
    return result

def order(inset_str, base_str, pattens):
    result_str = base_str
    for (idx, one_str) in enumerate(list(inset_str)):
        if one_str in result_str: continue
        print('字符：', one_str, "-> ", result_str, "条件数组", pattens)
        before = []
        after = []
        # 发散查找
        # 找after
        for str in inset_str[idx:]:
            for patten in pattens:
                if str not in patten: continue
                index_one_str = patten.index(str)
                new_a = patten[index_one_str+1:]
                if len(new_a) != 0 and new_a not in after:
                    after.append(new_a)
        # 找before
        for str in inset_str[:idx+1]:
            for patten in pattens:
                if str not in patten: continue
                index_one_str = patten.index(str)
                new_b = patten[:index_one_str+1]
                # print(new_b, index_one_str)
                if len(new_b) != 0 and new_b not in before:
                    before.append(new_b)
        print('before:', before, 'after:', after)

        # 如果无法找到比字符大的元素，说明这个字符要从头添加
        inset_head_index = 999
        for str in result_str:
            is_str_after_target = False
            for c in after:
                if str in c:
                    is_str_after_target = True
                    break
            if is_str_after_target:
                # 当前字符，比待插入的字符小，插入字符放在当前字符前
                inset_head_index = result_str.index(str)
                print(str, result_str.index(str))
                break
        # 从尾部开始接入
        inset_index = 999
        for str in result_str[::-1]:
            is_str_befor_target = False
            for c in before:
                if str in c:
                    is_str_befor_target = True
                    break
            if is_str_befor_target:
                # 当前字符，比待插入的字符大，直接插入当前字符后面
                print(str, result_str.index(str))
                inset_index = result_str.index(str)+1
                break
        print('字符', one_str, '从头部插入位置', inset_head_index)
        print('字符', one_str, '从尾部插入位置', inset_index, result_str)

        if inset_index == 999 and inset_head_index == 999:
            #都没有
            result_str = result_str + one_str
            print(result_str)
        elif inset_head_index != 999 and inset_index == 999 or inset_head_index == 999 and inset_index != 999:
            #其中有一个
            list_str = list(result_str)
            list_str.insert(min(inset_index, inset_head_index), one_str)
            result_str = ''.join(list_str)
            print(result_str)
        elif (inset_head_index - inset_index) > 0:
            # 说明有冲突，存在争议空间,按照字母顺序排列
            space = result_str[inset_index:inset_head_index]
            inset = -1
            for (i,s) in enumerate(space):
                print(one_str >= s, one_str, s)
                if one_str >= s:
                    inset = i
            print('存在争议空间', one_str, space, inset)
            # print(result_str.index(space[inset]))
            if inset < 0:
                inset = result_str.index(space[inset])
            else:
                inset = result_str.index(space[inset]) + 1
            
            list_str = list(result_str)
            list_str.insert(inset, one_str)
            result_str = ''.join(list_str)
            print(result_str)
            pass
        elif inset_head_index != 999 and inset_index != 999:
            list_str = list(result_str)
            list_str.insert(max(inset_index, inset_head_index), one_str)
            result_str = ''.join(list_str)
            print(result_str)
            
    return result_str

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm",  "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", "Concatenate and paste in"
    assert checkio(["qwerty","asdfg","zxcvb","yagz"]) ==  "qwertyasdfgzxcvb"
    checkio(["b","d","a"]) == 'abd'
    assert checkio(["hello","low","lino","itttnosw"]) == "helitnosw"
    assert checkio(["is","not","abc","nots","iabcn"]) == "iabcnots" 
    assert checkio(["jhgfdba","jihcba","jigedca"]) == "jihgefdcba"
    assert checkio(["jhgedba","jihcba","jigfdca"]) == "jihgefdcba"

    