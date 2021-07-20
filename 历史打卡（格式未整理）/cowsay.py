import textwrap
import re

COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

# def cowsay(text):
#     text = re.sub(' +', ' ', text)
#     ddd = textwrap.fill(text, 39)
#     para = ddd.split('\n')
#     if text == " 0123456789012345678901234567890123456789 ":
#         para = [' ', '012345678901234567890123456789012345678', '9']
#     print(para)

    

#     # if ddd[0] == ' ' and len(para[0]) >= 39:
#     #     text = re.sub(' +', ' ', text)
#     #     text = text.replace(' ', '\n')
#     #     ddd = textwrap.fill(text, 39)
#     #     print(ddd)
#     #     # para = ddd.split('\n')
    
#     if ddd.count('\n') == 0:
#         new_t = f'< {text} >'
#         up_l = "_" * (len(new_t) - 2)
#         down_l = "-" * len(up_l)
#     else:
#         first_l = para[0]
#         last_l = para[-1]
#         max_l = max(para, key=len)
#         fff = f"/ {first_l}{' '* (len(max_l) - len(first_l))} \\"
#         dddddd = f"\ {last_l}{' '* (len(max_l) - len(last_l))} /"
#         result = fff
#         for m_l in para[1:-1]:
#             temp = f"| {m_l}{' '* (len(max_l) - len(m_l))} |"
#             result = f"{result}\n{temp}"
#         result = f"{result}\n{dddddd}"
#         up_l = "_" * (len(max_l) + 2)
#         down_l = "-" * (len(max_l) + 2)
#         new_t = result
#     r = f'''
#  {up_l}
# {new_t}
#  {down_l}{COW}'''
#     print(r)
#     return r
def cowsay(text):
    text, temp = [''] * (text[0] == ' ') + text.split() + [''] * (text[-1] == ' '), []
    while text:
        s = ''
        while text and len(s) + len(text[0]) < 40: 
            s, text = s + text[0] + ' ', text[1:]
        if not s: 
            s, text[0] = s + text[0][:39] +' ',text[0][39:]
        temp.append(s[:-1])
    sentence_num, max_sentence_len = len(temp), max(map(len,temp))
    f = sentence_num == 1 and ['< {} >'] or ['/ {} \\'] + ['| {} |'] * (sentence_num-2) + ['\\ {} /']
    return '\n '+ '_' * (max_sentence_len + 2) + '\n' + '\n'.join(f[i].format(temp[i].ljust(max_sentence_len)) for i in range(sentence_num))+ '\n '+ '-' * (max_sentence_len + 2) + COW

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    # cowsay_one_line = cowsay('Checkio rulezz')
    # assert cowsay_one_line == expected_cowsay_one_line    

    # cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    # assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines

    # cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
    #                             'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    # assert cowsay_many_lines == expected_cowsay_many_lines

    # cowsay("spaces                           inside")
    cowsay("looooooooooooooooooooooooooooooooooooong")
    # cowsay(" a")
    # cowsay(" 0123456789012345678901234567890123456789 ")
    
