import re

def translate(text: str) -> str:
    consonants = 'bcdfgjklmnpqstvxzhrw'
    vowels = 'aeiouy'

    consonantsRule = False
    vowelsRule = False
    vowelsRuleCount = 0

    result = ''
    for t in text:
        print(t)
        if t in consonants:
            consonantsRule = True
        if consonantsRule and t in vowels:
            consonantsRule = False
            continue
        if t in vowels:
            vowelsRule = True
            vowelsRuleCount += 1
        else:
            vowelsRule = False
            vowelsRuleCount = 0

        result += t
        if vowelsRuleCount == 3:
            vowelsRule = False
            vowelsRuleCount = 0
            result = result[:-2]
        print(result)

    print(result)
    return result


if __name__ == '__main__':
    print("Example:")
    print(translate('hieeelalaooo'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert translate('hieeelalaooo') == 'hello'
    assert translate('hoooowe yyyooouuu duoooiiine') == 'how you doin'
    assert translate('aaa bo cy da eee fe') == 'a b c d e f'
    assert translate('sooooso aaaaaaaaa') == 'sos aaa'
    print("Coding complete? Click 'Check' to earn cool rewards!")
