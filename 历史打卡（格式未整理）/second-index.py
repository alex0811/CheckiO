def second_index(text, symbol):
    if symbol not in text or text.count(symbol) == 1: return None
    index = text.index(symbol)+1
    return str(text[index:]).index(symbol) + index


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    assert second_index("three occurrences","r") == 10
    print('You are awesome! All tests are done! Go Check it!')

