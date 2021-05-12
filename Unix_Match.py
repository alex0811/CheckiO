# from re import search
# from typing import Match
import re

# # def unix_match(filename: str, pattern: str) -> bool:
# #     ddd = pattern.replace('.', '\.').replace('*', '.*').replace('?', '.').replace('[]', '\[!]').replace('[!', '[^',)
#     # print(pattern, ddd, search(ddd, filename))
# #     return search(ddd, filename) != None

# def unix_match(filename, pattern):
#     print('befor:',filename, pattern)
#     filename = filename.replace('[!]', '')
#     pattern = pattern.replace('[!]', '').replace('*', '.*').replace('?','.').replace('[!','[^').replace('[]','').replace('[.]','.').replace('[.*]','.*')
#     # .replace('[?]', '').replace('[*]', '').replace('?','.').replace('[!', '[^',).replace('**','*').replace('*','.*')
#     # [::-1].replace('*', '*.', 1)[::-1]
#     print('after:', filename, pattern)
#     try:
#         print(re.match(pattern, filename))
#         return bool(re.match(pattern, filename))
#     except re.error:
#         return False


# if __name__ == '__main__':
#     print("Example:")
#     # print(unix_match('somefile.txt', '*'))
    
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert unix_match('somefile.txt', '*') == True
#     assert unix_match('other.exe', '*') == True
#     assert unix_match('my.exe', '*.txt') == False
#     assert unix_match('log1.txt', 'log?.txt') == True
#     assert unix_match('log1.txt', 'log[1234567890].txt') == True
#     assert unix_match('log12.txt', 'log?.txt') == False
#     assert unix_match('log12.txt', 'log??.txt') == True
#     assert unix_match("1name.txt","[!abc]name.txt") == True
#     assert unix_match("1name.txt","[!1234567890]*") == False
#     assert unix_match("[!]check.txt","[!]check.txt") == True
#     assert unix_match("[?*]","[[][?][*][]]") == True
#     assert unix_match("nametxt","name[]txt") == False
#     assert unix_match("log12.txt","**") == True
#     assert unix_match("apache12.log","*[1234567890].*") == True
#     assert unix_match("apache.1log","*[1234567890].*") == False
#     assert unix_match("12apache1","*.*") == False
#     assert unix_match("[check].txt","[][]check[][].txt") == True
#     print("Coding complete? Click 'Check' to earn cool rewards!")
def unix_match(filename, pattern):
    # return re.search(pattern.replace('.', '\.').replace('[!', '[^').replace('[^]', '\[!]'), filename) is not None

    return re.match(pattern.replace('*', '\\*').replace('.', '\\.').replace('[!', '[^').replace('[]', '[^.]').replace('[^]', '\[!\]'), filename) != None


if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', 'somefile.txt') == True
    assert unix_match('1name.txt', '[!abc]name.txt') == True
    assert unix_match('log1.txt', 'log[!0].txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log1.txt', 'log[!1].txt') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
