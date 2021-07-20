def caps_lock(text: str) -> str:
    if not text: return ''

    result = text[0]
    lock = 0

    for t in text[1:]:
        isA = t.upper() == 'A'
        lock = abs(lock - isA)
        if not isA:
            result += (t.upper() if lock else t)
            
    return result


if __name__ == '__main__':
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    print("Coding complete? Click 'Check' to earn cool rewards!")
