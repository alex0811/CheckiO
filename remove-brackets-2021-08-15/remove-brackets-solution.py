brackets = {"(": ")", "{": "}", "[": "]"}

def remove_brackets(line: str) -> str:
    result = removeOneBucket(removeOneBucket(removeOneBucket(line, "(")[0], "[")[0], "{")[0]

    compare = []
    compare.extend(removeOneBucket(result, "(")[1])
    compare.extend(removeOneBucket(result, "[")[1])
    compare.extend(removeOneBucket(result, "{")[1])
    
    delete = []
    for c in compare:
        if c[0] == 0 and (c[1] - c[0] - 1) % 2 != 0:
            delete.extend(c)

    new_result = ""
    for index, value in enumerate(result):
        if index not in delete:
            new_result += value
        

    return new_result

def removeOneBucket(line: str, char: str):
    stack = []
    delete = []
    location = []
    for index, value in enumerate(line):
        if value == char:
            stack.append(index)
        elif len(stack) > 0:
            if brackets[line[stack[-1]]] == value:
                location.append((stack[-1], index))
                stack.pop()
        elif brackets[char] == value:
            delete.append(index)
    result = ""

    for index, value in enumerate(line):
        if index in stack:
            continue
        if index in delete:
            continue
        result += value
    
    return result, location


# def other_char(a_char: str) -> str:
#     if a_char == "(":
#         return ")"
#     elif a_char == "{":
#         return "}"
#     elif a_char == "[":
#         return "]"
#     return ""


if __name__ == '__main__':
    # print("Example:")
    # print(remove_brackets('(()()'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_brackets('(()()') == '()()'
    assert remove_brackets('[][[[') == '[]'
    assert remove_brackets('[[(}]]') == '[[]]'
    assert remove_brackets('[[{}()]]') == '[[{}()]]'
    assert remove_brackets('[[[[[[') == ''
    assert remove_brackets('[[[[}') == ''
    assert remove_brackets('') == ''
    assert remove_brackets("}}{}") == "{}"
    assert remove_brackets("[(])") == "()"
    assert remove_brackets("([)]") == "[]"
    
    print("Coding complete? Click 'Check' to earn cool rewards!")
