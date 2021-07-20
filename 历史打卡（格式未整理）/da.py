# def s_match(filename: str, pattern: str) -> bool:
#     p = pattern.split('.')
#     p_n, p_e = p[0], '' if len(p) < 2 else p[1] 
#     f = filename.split('.')
#     f_n, f_e = f[0], '' if len(f) < 2 else f[1] 
#     return (p_n is '*' or p_n == f_n) and (p_e is '*' or p_e == f_e)
    
# def get_condition(pattern: str) ->(bool, str, (int, int)):
#     if '[' and ']' in pattern:
#         r = (pattern.index('['), pattern.index(']'))
#         condition = pattern[r[0]+1:r[1]]
#         logic = not '!' in condition
#         condition = condition.replace('!', '')
#         return(logic, condition, r)
#     return (False, '', (0, 0))

# def unix_match(filename: str, pattern: str) -> bool:
#     logic, contition, location = get_condition(pattern)
#     target = list(filename)[location[0]] if len(pattern) - (location[1]-location[0]+1) != len(filename) else ''
#     print(logic, contition, len(contition), location, target)
#     if len(contition) == 0:
#         return s_match(filename, pattern)
#     else:
#         return (target in contition) is logic

unix_match = lambda f, p: __import__('re').match(p
    .replace('.', r'\.')
    .replace('*', '.*')
    .replace('?', r'.{1}')
    .replace('[!]', r'\[\!\]')
    .replace('[!', '[^')
    .replace('[]', '[^.]'), f) is not None

if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', 'somefile.txt') == True
    assert unix_match('1name.txt', '[!abc]name.txt') == True
    assert unix_match('log1.txt', 'log[!0].txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log1.txt', 'log[!1].txt') == False
    assert unix_match("name.txt","[!abc]name.txt") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
