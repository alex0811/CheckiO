def to_camel_case(name: str) -> str:
    result = ""
    needUpNext = False

    for i,v in enumerate(name):
        if i == 0:
            result += v.upper()
            continue

        if v == "_":
            needUpNext = True
            continue

        if needUpNext:
            result += v.upper()
            needUpNext = False
            continue

        result += v
    
    return result

if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('name'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")

