def to_encrypt(text, delta):
    return ''.join(list(map( 
        lambda x: ' ' if x == ' ' else chr(ord('a') + (ord(x)+delta - ord('a')) % 26) if x >= 'a' and x <= 'z' else '',
        text
    )))

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
