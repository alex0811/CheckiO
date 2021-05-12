import re

def repeat_inside(line):
    if len(set(line)) == 1: return line
    matchObj = re.findall(r"(.+)(?=.*\1.*)", line)
    result = ''
    if len(matchObj) > 0:
        num = 0
        temp = ['']
        while len(temp) > 0:
            num = num + 1
            search = re.search("(%s){%d}" % (max(matchObj, key=len), num), line)
            if search:
                result = search.group() 
            else:
                temp = []
        return result
    else:
        return result

    
    
    # your code here

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    assert repeat_inside("rghtyjdfrtdfdf56r") == "dfdf"
    print('"Run" is good. How is "Check"?')
