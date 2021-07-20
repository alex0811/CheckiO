import re

def get_cookie(cookie, name):
    # pattern = (re.compile(f'(?<={name}=).*?(?=;)')).findall(cookie+';')[0]
    return (re.compile(f'(?<={name}=).*?(?=;)')).findall(cookie+';')[0]

    # ff = cookie.split(name+'=')
    # # print(ff)
    # ggg = ff[-1].split(';')
    # # print(ggg)
    # return ggg[0]


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert get_cookie('theme=light; sessionToken=abc123', 'theme') == 'light', 'theme=light'
    assert get_cookie('_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true', 'ffo') == 'true', 'ffo=true'
    print("Looks like you know everything. It is time for 'Check'!")
