def checkio(text, word):
    p = text.replace(' ', '').split('\n')
    for r, s in enumerate(p):
        if word in s:
            w_index = s.find(word)
            return [r + 1, w_index + 1, r + 1, w_index + len(word)]

    for r, s in enumerate(p):
        for c, w in enumerate(s):
            if w.lower() == word[0].lower():
                compare = ''
                for stitch in range(len(word)):
                    try:
                        compare += p[r+stitch][c]
                    except:
                        break
                if compare.lower() == word.lower():
                    return[r + 1, c + 1, r + len(word), c + 1]
    return [0, 0, 0, 0]



if __name__ == '__main__':
#     assert checkio("""DREAMING of apples on a wall,
# And dreaming often, dear,
# I dreamed that, if I counted all,
# -How many would appear?""", "ten") == [2, 14, 2, 16]

#     assert checkio("""He took his vorpal sword in hand:
# Long time the manxome foe he sought--
# So rested he by the Tumtum tree,
# And stood awhile in thought.
# And as in uffish thought he stood,
# The Jabberwock, with eyes of flame,
# Came whiffling through the tulgey wood,
# And burbled as it came!""", "noir") == [4, 16, 7, 16]
# print("Coding complete? Click 'Check' to earn cool rewards!")

    assert checkio("Hi all!\nAnd all goodbye!\nOf course goodbye.\nor not","haoo") == [1,1,4,1]