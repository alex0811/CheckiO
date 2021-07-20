import unicodedata

def checkio(in_string):
    return ''.join(filter(
        lambda c: not unicodedata.combining(c),
        unicodedata.normalize('NFKD', in_string)
    ))

    #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    # print('Done')
