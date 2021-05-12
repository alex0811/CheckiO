def greatest_common_divisor(*args:int) -> int:
    g = args[0]
    for num in range(1, len(args)):
        g = gcd(g, args[num])
    return g

def gcd(a, b):
    while b != 0:
        a,b = (b, a%b)
    return a

if __name__ == '__main__':
    print("Example:")
    print(greatest_common_divisor(6, 4))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert greatest_common_divisor(6, 4) == 2
    assert greatest_common_divisor(2, 4, 8) == 2
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1
    assert greatest_common_divisor(3, 9, 3, 9) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
