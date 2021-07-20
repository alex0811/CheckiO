def check_pangram(text):
    print(text)
    
    p = set()

    ddd = sum(map(
        lambda c: 'a' <= c.lower() <= 'z',
        text
    ))

    print(ddd)
    
    for c in text:
        if 'a' <= c.lower() <= 'z':
            p.add(c.lower())

    print(p, len(p))
    return len(p) == 26

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    print('If it is done - it is Done. Go Check is NOW!')
